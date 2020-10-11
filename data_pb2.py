# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndata.proto\x12\x04test\"+\n\x1bTestClientRecvStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientRecvStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2s\n\x0eTestClientRecv\x12\x61\n\x14TestClientRecvStream\x12!.test.TestClientRecvStreamRequest\x1a\".test.TestClientRecvStreamResponse\"\x00\x30\x01\x62\x06proto3'
)




_TESTCLIENTRECVSTREAMREQUEST = _descriptor.Descriptor(
  name='TestClientRecvStreamRequest',
  full_name='test.TestClientRecvStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestClientRecvStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=63,
)


_TESTCLIENTRECVSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestClientRecvStreamResponse',
  full_name='test.TestClientRecvStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestClientRecvStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=65,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['TestClientRecvStreamRequest'] = _TESTCLIENTRECVSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestClientRecvStreamResponse'] = _TESTCLIENTRECVSTREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestClientRecvStreamRequest = _reflection.GeneratedProtocolMessageType('TestClientRecvStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTRECVSTREAMREQUEST,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientRecvStreamRequest)
  })
_sym_db.RegisterMessage(TestClientRecvStreamRequest)

TestClientRecvStreamResponse = _reflection.GeneratedProtocolMessageType('TestClientRecvStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTRECVSTREAMRESPONSE,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientRecvStreamResponse)
  })
_sym_db.RegisterMessage(TestClientRecvStreamResponse)



_TESTCLIENTRECV = _descriptor.ServiceDescriptor(
  name='TestClientRecv',
  full_name='test.TestClientRecv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=113,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='TestClientRecvStream',
    full_name='test.TestClientRecv.TestClientRecvStream',
    index=0,
    containing_service=None,
    input_type=_TESTCLIENTRECVSTREAMREQUEST,
    output_type=_TESTCLIENTRECVSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTCLIENTRECV)

DESCRIPTOR.services_by_name['TestClientRecv'] = _TESTCLIENTRECV

# @@protoc_insertion_point(module_scope)
