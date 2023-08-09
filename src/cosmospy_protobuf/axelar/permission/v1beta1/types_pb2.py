"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%axelar/permission/v1beta1/types.proto\x12\x19axelar.permission.v1beta1\x1a\x14gogoproto/gogo.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\x88\x01\n\nGovAccount\x12B\n\x07address\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x126\n\x04role\x18\x02 \x01(\x0e2(.axelar.permission.exported.v1beta1.RoleB=Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.permission.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00'
    _GOVACCOUNT.fields_by_name['address']._options = None
    _GOVACCOUNT.fields_by_name['address']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _globals['_GOVACCOUNT']._serialized_start = 139
    _globals['_GOVACCOUNT']._serialized_end = 275