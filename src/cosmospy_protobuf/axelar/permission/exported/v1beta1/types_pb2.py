"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.axelar/permission/exported/v1beta1/types.proto\x12"axelar.permission.exported.v1beta1\x1a\x14gogoproto/gogo.proto\x1a google/protobuf/descriptor.proto*q\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x15\n\x11ROLE_UNRESTRICTED\x10\x01\x12\x19\n\x15ROLE_CHAIN_MANAGEMENT\x10\x02\x12\x17\n\x13ROLE_ACCESS_CONTROL\x10\x03\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01:d\n\x0fpermission_role\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x0e2(.axelar.permission.exported.v1beta1.RoleB@Z:github.com/axelarnetwork/axelar-core/x/permission/exported\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.permission.exported.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(permission_role)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z:github.com/axelarnetwork/axelar-core/x/permission/exported\xc8\xe1\x1e\x00'
    _ROLE._options = None
    _ROLE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _globals['_ROLE']._serialized_start = 142
    _globals['_ROLE']._serialized_end = 255