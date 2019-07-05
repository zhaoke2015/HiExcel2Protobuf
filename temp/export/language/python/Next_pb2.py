# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Next.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Next.proto',
  package='HiProtobuf',
  syntax='proto3',
  serialized_options=_b('\n\031com.HiProtobuf.HiProtobufB\016Next_classname\252\002\nHiProtobuf'),
  serialized_pb=_b('\n\nNext.proto\x12\nHiProtobuf\"K\n\x04Next\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02hp\x18\x03 \x01(\x05\x12\x0e\n\x06\x61ttack\x18\x04 \x01(\x05\x12\r\n\x05infos\x18\x05 \x03(\t\"{\n\nExcel_Next\x12.\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32 .HiProtobuf.Excel_Next.DataEntry\x1a=\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.HiProtobuf.Next:\x02\x38\x01\x42\x38\n\x19\x63om.HiProtobuf.HiProtobufB\x0eNext_classname\xaa\x02\nHiProtobufb\x06proto3')
)




_NEXT = _descriptor.Descriptor(
  name='Next',
  full_name='HiProtobuf.Next',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='HiProtobuf.Next.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='HiProtobuf.Next.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hp', full_name='HiProtobuf.Next.hp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack', full_name='HiProtobuf.Next.attack', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infos', full_name='HiProtobuf.Next.infos', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=26,
  serialized_end=101,
)


_EXCEL_NEXT_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='HiProtobuf.Excel_Next.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='HiProtobuf.Excel_Next.DataEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='HiProtobuf.Excel_Next.DataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=226,
)

_EXCEL_NEXT = _descriptor.Descriptor(
  name='Excel_Next',
  full_name='HiProtobuf.Excel_Next',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='HiProtobuf.Excel_Next.Data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXCEL_NEXT_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=226,
)

_EXCEL_NEXT_DATAENTRY.fields_by_name['value'].message_type = _NEXT
_EXCEL_NEXT_DATAENTRY.containing_type = _EXCEL_NEXT
_EXCEL_NEXT.fields_by_name['Data'].message_type = _EXCEL_NEXT_DATAENTRY
DESCRIPTOR.message_types_by_name['Next'] = _NEXT
DESCRIPTOR.message_types_by_name['Excel_Next'] = _EXCEL_NEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Next = _reflection.GeneratedProtocolMessageType('Next', (_message.Message,), {
  'DESCRIPTOR' : _NEXT,
  '__module__' : 'Next_pb2'
  # @@protoc_insertion_point(class_scope:HiProtobuf.Next)
  })
_sym_db.RegisterMessage(Next)

Excel_Next = _reflection.GeneratedProtocolMessageType('Excel_Next', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXCEL_NEXT_DATAENTRY,
    '__module__' : 'Next_pb2'
    # @@protoc_insertion_point(class_scope:HiProtobuf.Excel_Next.DataEntry)
    })
  ,
  'DESCRIPTOR' : _EXCEL_NEXT,
  '__module__' : 'Next_pb2'
  # @@protoc_insertion_point(class_scope:HiProtobuf.Excel_Next)
  })
_sym_db.RegisterMessage(Excel_Next)
_sym_db.RegisterMessage(Excel_Next.DataEntry)


DESCRIPTOR._options = None
_EXCEL_NEXT_DATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
