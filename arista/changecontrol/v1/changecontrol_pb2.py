# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/changecontrol.v1/changecontrol.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+arista/changecontrol.v1/changecontrol.proto\x12\x17\x61rista.changecontrol.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\"=\n\x16RepeatedRepeatedString\x12#\n\x06values\x18\x01 \x03(\x0b\x32\x13.fmp.RepeatedString\"B\n\x10\x43hangeControlKey\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\x87\x01\n\x06\x41\x63tion\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07timeout\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\"\n\x04\x61rgs\x18\x03 \x01(\x0b\x32\x14.fmp.MapStringString\"\xa9\x01\n\x0bStageConfig\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x1f.arista.changecontrol.v1.Action\x12=\n\x04rows\x18\x03 \x01(\x0b\x32/.arista.changecontrol.v1.RepeatedRepeatedString\"\xaa\x01\n\x0eStageConfigMap\x12\x43\n\x06values\x18\x01 \x03(\x0b\x32\x33.arista.changecontrol.v1.StageConfigMap.ValuesEntry\x1aS\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.arista.changecontrol.v1.StageConfig:\x02\x38\x01\"\xd5\x01\n\x0c\x43hangeConfig\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rroot_stage_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x06stages\x18\x03 \x01(\x0b\x32\'.arista.changecontrol.v1.StageConfigMap\x12+\n\x05notes\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"d\n\nFlagConfig\x12)\n\x05value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05notes\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"m\n\x13TimestampFlagConfig\x12)\n\x05value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x05notes\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x80\x02\n\x13\x43hangeControlConfig\x12\x36\n\x03key\x18\x01 \x01(\x0b\x32).arista.changecontrol.v1.ChangeControlKey\x12\x35\n\x06\x63hange\x18\x02 \x01(\x0b\x32%.arista.changecontrol.v1.ChangeConfig\x12\x32\n\x05start\x18\x03 \x01(\x0b\x32#.arista.changecontrol.v1.FlagConfig\x12>\n\x08schedule\x18\x04 \x01(\x0b\x32,.arista.changecontrol.v1.TimestampFlagConfig:\x06\xfa\x8d\x19\x02rw\"\xe4\x02\n\x05Stage\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x1f.arista.changecontrol.v1.Action\x12=\n\x04rows\x18\x03 \x01(\x0b\x32/.arista.changecontrol.v1.RepeatedRepeatedString\x12\x34\n\x06status\x18\x04 \x01(\x0e\x32$.arista.changecontrol.v1.StageStatus\x12+\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x98\x01\n\x08StageMap\x12=\n\x06values\x18\x01 \x03(\x0b\x32-.arista.changecontrol.v1.StageMap.ValuesEntry\x1aM\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.arista.changecontrol.v1.Stage:\x02\x38\x01\"\x9f\x02\n\x06\x43hange\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rroot_stage_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x06stages\x18\x03 \x01(\x0b\x32!.arista.changecontrol.v1.StageMap\x12+\n\x05notes\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x04user\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xb4\x01\n\x04\x46lag\x12)\n\x05value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05notes\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x04user\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xbd\x01\n\rTimestampFlag\x12)\n\x05value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x05notes\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x04user\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"1\n\x06\x46ilter\x12\'\n\ndevice_ids\x18\x01 \x01(\x0b\x32\x13.fmp.RepeatedString\"\x9d\x01\n\x10\x44\x65viceToStageMap\x12\x45\n\x06values\x18\x01 \x03(\x0b\x32\x35.arista.changecontrol.v1.DeviceToStageMap.ValuesEntry\x1a\x42\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.fmp.RepeatedString:\x02\x38\x01\"\x81\x04\n\rChangeControl\x12\x36\n\x03key\x18\x01 \x01(\x0b\x32).arista.changecontrol.v1.ChangeControlKey\x12/\n\x06\x63hange\x18\x02 \x01(\x0b\x32\x1f.arista.changecontrol.v1.Change\x12.\n\x07\x61pprove\x18\x03 \x01(\x0b\x32\x1d.arista.changecontrol.v1.Flag\x12,\n\x05start\x18\x04 \x01(\x0b\x32\x1d.arista.changecontrol.v1.Flag\x12<\n\x06status\x18\x05 \x01(\x0e\x32,.arista.changecontrol.v1.ChangeControlStatus\x12+\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x08schedule\x18\x07 \x01(\x0b\x32&.arista.changecontrol.v1.TimestampFlag\x12\'\n\ndevice_ids\x18\x08 \x01(\x0b\x32\x13.fmp.RepeatedString\x12I\n\x16\x64\x65vice_id_to_stage_ids\x18\t \x01(\x0b\x32).arista.changecontrol.v1.DeviceToStageMap:\x10\xfa\x8d\x19\x02ro\x8a\x8e\x19\x06\x46ilter\"\xb2\x01\n\rApproveConfig\x12\x36\n\x03key\x18\x01 \x01(\x0b\x32).arista.changecontrol.v1.ChangeControlKey\x12\x34\n\x07\x61pprove\x18\x02 \x01(\x0b\x32#.arista.changecontrol.v1.FlagConfig\x12+\n\x07version\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x06\xfa\x8d\x19\x02rw*\x7f\n\x0bStageStatus\x12\x1c\n\x18STAGE_STATUS_UNSPECIFIED\x10\x00\x12\x18\n\x14STAGE_STATUS_RUNNING\x10\x01\x12\x1a\n\x16STAGE_STATUS_COMPLETED\x10\x02\x12\x1c\n\x18STAGE_STATUS_NOT_STARTED\x10\x03*\xd0\x01\n\x13\x43hangeControlStatus\x12%\n!CHANGE_CONTROL_STATUS_UNSPECIFIED\x10\x00\x12!\n\x1d\x43HANGE_CONTROL_STATUS_RUNNING\x10\x01\x12#\n\x1f\x43HANGE_CONTROL_STATUS_COMPLETED\x10\x02\x12#\n\x1f\x43HANGE_CONTROL_STATUS_SCHEDULED\x10\x03\x12%\n!CHANGE_CONTROL_STATUS_NOT_STARTED\x10\x04\x42TZRgithub.com/aristanetworks/cloudvision-go/api/arista/changecontrol.v1;changecontrolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.changecontrol.v1.changecontrol_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/aristanetworks/cloudvision-go/api/arista/changecontrol.v1;changecontrol'
  _globals['_CHANGECONTROLKEY']._options = None
  _globals['_CHANGECONTROLKEY']._serialized_options = b'\200\216\031\001'
  _globals['_STAGECONFIGMAP_VALUESENTRY']._options = None
  _globals['_STAGECONFIGMAP_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_CHANGECONTROLCONFIG']._options = None
  _globals['_CHANGECONTROLCONFIG']._serialized_options = b'\372\215\031\002rw'
  _globals['_STAGEMAP_VALUESENTRY']._options = None
  _globals['_STAGEMAP_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_DEVICETOSTAGEMAP_VALUESENTRY']._options = None
  _globals['_DEVICETOSTAGEMAP_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_CHANGECONTROL']._options = None
  _globals['_CHANGECONTROL']._serialized_options = b'\372\215\031\002ro\212\216\031\006Filter'
  _globals['_APPROVECONFIG']._options = None
  _globals['_APPROVECONFIG']._serialized_options = b'\372\215\031\002rw'
  _globals['_STAGESTATUS']._serialized_start=3568
  _globals['_STAGESTATUS']._serialized_end=3695
  _globals['_CHANGECONTROLSTATUS']._serialized_start=3698
  _globals['_CHANGECONTROLSTATUS']._serialized_end=3906
  _globals['_REPEATEDREPEATEDSTRING']._serialized_start=179
  _globals['_REPEATEDREPEATEDSTRING']._serialized_end=240
  _globals['_CHANGECONTROLKEY']._serialized_start=242
  _globals['_CHANGECONTROLKEY']._serialized_end=308
  _globals['_ACTION']._serialized_start=311
  _globals['_ACTION']._serialized_end=446
  _globals['_STAGECONFIG']._serialized_start=449
  _globals['_STAGECONFIG']._serialized_end=618
  _globals['_STAGECONFIGMAP']._serialized_start=621
  _globals['_STAGECONFIGMAP']._serialized_end=791
  _globals['_STAGECONFIGMAP_VALUESENTRY']._serialized_start=708
  _globals['_STAGECONFIGMAP_VALUESENTRY']._serialized_end=791
  _globals['_CHANGECONFIG']._serialized_start=794
  _globals['_CHANGECONFIG']._serialized_end=1007
  _globals['_FLAGCONFIG']._serialized_start=1009
  _globals['_FLAGCONFIG']._serialized_end=1109
  _globals['_TIMESTAMPFLAGCONFIG']._serialized_start=1111
  _globals['_TIMESTAMPFLAGCONFIG']._serialized_end=1220
  _globals['_CHANGECONTROLCONFIG']._serialized_start=1223
  _globals['_CHANGECONTROLCONFIG']._serialized_end=1479
  _globals['_STAGE']._serialized_start=1482
  _globals['_STAGE']._serialized_end=1838
  _globals['_STAGEMAP']._serialized_start=1841
  _globals['_STAGEMAP']._serialized_end=1993
  _globals['_STAGEMAP_VALUESENTRY']._serialized_start=1916
  _globals['_STAGEMAP_VALUESENTRY']._serialized_end=1993
  _globals['_CHANGE']._serialized_start=1996
  _globals['_CHANGE']._serialized_end=2283
  _globals['_FLAG']._serialized_start=2286
  _globals['_FLAG']._serialized_end=2466
  _globals['_TIMESTAMPFLAG']._serialized_start=2469
  _globals['_TIMESTAMPFLAG']._serialized_end=2658
  _globals['_FILTER']._serialized_start=2660
  _globals['_FILTER']._serialized_end=2709
  _globals['_DEVICETOSTAGEMAP']._serialized_start=2712
  _globals['_DEVICETOSTAGEMAP']._serialized_end=2869
  _globals['_DEVICETOSTAGEMAP_VALUESENTRY']._serialized_start=2803
  _globals['_DEVICETOSTAGEMAP_VALUESENTRY']._serialized_end=2869
  _globals['_CHANGECONTROL']._serialized_start=2872
  _globals['_CHANGECONTROL']._serialized_end=3385
  _globals['_APPROVECONFIG']._serialized_start=3388
  _globals['_APPROVECONFIG']._serialized_end=3566
# @@protoc_insertion_point(module_scope)
