# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: electricity_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='electricity_data.proto',
  package='gRPC_microservice',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x65lectricity_data.proto\x12\x11gRPC_microservice\"\r\n\x0bRequestInfo\"V\n\x04\x44\x61ta\x12\x0e\n\x06\x61_name\x18\x01 \x01(\t\x12\x0e\n\x06\x62_name\x18\x02 \x01(\t\x12.\n\tdata_list\x18\x03 \x03(\x0b\x32\x1b.gRPC_microservice.DataPair\" \n\x08\x44\x61taPair\x12\t\n\x01\x61\x18\x01 \x01(\t\x12\t\n\x01\x62\x18\x02 \x01(\t2V\n\x0e\x45lectrictyData\x12\x44\n\x07GetData\x12\x1e.gRPC_microservice.RequestInfo\x1a\x17.gRPC_microservice.Data\"\x00\x62\x06proto3')
)




_REQUESTINFO = _descriptor.Descriptor(
  name='RequestInfo',
  full_name='gRPC_microservice.RequestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=58,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='gRPC_microservice.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a_name', full_name='gRPC_microservice.Data.a_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b_name', full_name='gRPC_microservice.Data.b_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_list', full_name='gRPC_microservice.Data.data_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=146,
)


_DATAPAIR = _descriptor.Descriptor(
  name='DataPair',
  full_name='gRPC_microservice.DataPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='gRPC_microservice.DataPair.a', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='gRPC_microservice.DataPair.b', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=180,
)

_DATA.fields_by_name['data_list'].message_type = _DATAPAIR
DESCRIPTOR.message_types_by_name['RequestInfo'] = _REQUESTINFO
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['DataPair'] = _DATAPAIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestInfo = _reflection.GeneratedProtocolMessageType('RequestInfo', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTINFO,
  __module__ = 'electricity_data_pb2'
  # @@protoc_insertion_point(class_scope:gRPC_microservice.RequestInfo)
  ))
_sym_db.RegisterMessage(RequestInfo)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'electricity_data_pb2'
  # @@protoc_insertion_point(class_scope:gRPC_microservice.Data)
  ))
_sym_db.RegisterMessage(Data)

DataPair = _reflection.GeneratedProtocolMessageType('DataPair', (_message.Message,), dict(
  DESCRIPTOR = _DATAPAIR,
  __module__ = 'electricity_data_pb2'
  # @@protoc_insertion_point(class_scope:gRPC_microservice.DataPair)
  ))
_sym_db.RegisterMessage(DataPair)



_ELECTRICTYDATA = _descriptor.ServiceDescriptor(
  name='ElectrictyData',
  full_name='gRPC_microservice.ElectrictyData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=182,
  serialized_end=268,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='gRPC_microservice.ElectrictyData.GetData',
    index=0,
    containing_service=None,
    input_type=_REQUESTINFO,
    output_type=_DATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ELECTRICTYDATA)

DESCRIPTOR.services_by_name['ElectrictyData'] = _ELECTRICTYDATA

# @@protoc_insertion_point(module_scope)
