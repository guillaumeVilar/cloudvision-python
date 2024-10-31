# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

import argparse
import grpc

from google.protobuf import wrappers_pb2 as wrapperpb

from arista.connectivitymonitor.v1.services import (
    ProbeStatsServiceStub,
    ProbeStatsStreamRequest,
    ProbeServiceStub,
    ProbeStreamRequest
)
from arista.connectivitymonitor.v1 import models
from cloudvision.Connector.grpc_client import create_query

from arista.inventory.v1 import services
RPC_TIMEOUT = 30  # in seconds

debug = False

parser = argparse.ArgumentParser(add_help=True)


def getSerialNumberToHostnameDict(channel):
    """
    Return a json dict with the mapping S/N --> hostname of all devices known to CVP.
    """
    device_dict = {}
    stub = services.DeviceServiceStub(channel)
    # create a stream request
    get_all_req = services.DeviceStreamRequest()
     # make the GetAll request and loop over the streamed responses
    for resp in stub.GetAll(get_all_req, timeout=RPC_TIMEOUT):
        device_dict[resp.value.key.device_id.value] = resp.value.hostname.value
    return device_dict

def getConnMon(channel, device=None):
    connMonGetAll = ProbeStatsStreamRequest()

    if device:
        connMonKey = models.ProbeStatsKey(
            device_id=wrapperpb.StringValue(value=device)
        )

        connectivityFilter = models.ProbeStats(
            key=connMonKey
        )

        connMonGetAll.partial_eq_filter.append(connectivityFilter)

    connStub = ProbeStatsServiceStub(channel)

    result = {}

    for resp in connStub.GetAll(connMonGetAll):
        vrfName = resp.value.key.vrf.value
        hostName = resp.value.key.host.value
        intf = resp.value.key.source_intf.value

        connMonKeyVals = (
            connMonKey.device_id.value,
            hostName,
            vrfName,
            intf
        )

        device_stats = resp.value

        connMonStats = {
            "latency": device_stats.latency_millis.value,
            "jitter": device_stats.jitter_millis.value,
            "http_response": device_stats.http_response_time_millis.value,
            "packet_loss": device_stats.packet_loss_percent.value
        }

        result[connMonKeyVals] = connMonStats

    return result


def getConnMonCfg(channel, device=None):
    configGetAll = ProbeStreamRequest()

    if device:
        probeKey = models.ProbeKey(
            device_id=wrapperpb.StringValue(value=device)
        )

        configFilter = models.Probe(
            key=probeKey
        )

        configGetAll.partial_eq_filter.append(configFilter)

    configStub = ProbeServiceStub(channel)

    result = {}

    for resp in configStub.GetAll(configGetAll):
        vrfName = resp.value.key.vrf.value
        hostName = resp.value.key.host.value

        probeKeyVals = (
            probeKey.device_id.value,
            hostName,
            vrfName,
        )

        config_data = resp.value

        configData = {
            "ip_addr": config_data.ip_addr.value,
            "host_name": config_data.host_name.value,
            "description": config_data.description.value
        }

        result[probeKeyVals] = configData

    return result


def report(serialNumberToHostnameDict, data, configData, device):
    for k, v in data.items():
        hostname = serialNumberToHostnameDict[k[0]]
        host = k[1]
        vrf = k[2]
        intf = k[3]
        httpResp = v["http_response"]
        jitter = v["jitter"]
        latency = v["latency"]
        pktloss = v["packet_loss"]
        if "ip_addr" in configData[(device, host, vrf)]:
            ipaddr = configData[(device, host, vrf)]["ip_addr"]
        else:
            ipaddr = ""
        hdr_part1 = f"{hostname + ' (' + vrf + '/' + intf + ') to ' + host:<50}"
        hdr_part2 = f"{ipaddr:<30}{str(httpResp) + 'ms':<30}{str(jitter) + 'ms':<30}"
        hdr_part3 = f"{str(latency) + 'ms':<30}{str(pktloss)  + '%':<30}"
        print(hdr_part1 + hdr_part2 + hdr_part3)


def main(apiserverAddr, token=None, certs=None, key=None, ca=None):
    token = token.read().strip()
    callCreds = grpc.access_token_call_credentials(token)

    if certs:
        cert = certs.read()
        channelCreds = grpc.ssl_channel_credentials(root_certificates=cert)
    else:
        channelCreds = grpc.ssl_channel_credentials()
    connCreds = grpc.composite_channel_credentials(channelCreds, callCreds)

    with grpc.secure_channel(apiserverAddr, connCreds) as channel:
        data = getConnMon(channel, args.device)
        configData = getConnMonCfg(channel, args.device)
        serialNumberToHostnameDict = getSerialNumberToHostnameDict(channel)
        report(serialNumberToHostnameDict, data, configData, args.device)


if __name__ == "__main__":
    parser.add_argument(
        "--device", type=str, help="device (by SerialNumber) to subscribe to"
    )
    parser.add_argument(
        "--apiserver", type=str, required=True, help="apiserver address"
    )
    parser.add_argument(
        "--cert", type=argparse.FileType("rb"), required=True, help="cert file"
    )
    parser.add_argument(
        "--token", type=argparse.FileType("r"), required=True, help="token file"
    )
    parser.add_argument(
        "--key", type=argparse.FileType("r"), help="key file"
    )
    parser.add_argument(
        "--ca", type=argparse.FileType("r"), help="ca file"
    )
    args = parser.parse_args()
    exit(
        main(
            args.apiserver,
            certs=args.cert,
            token=args.token,
            key=args.key,
            ca=args.ca,
        )
    )
