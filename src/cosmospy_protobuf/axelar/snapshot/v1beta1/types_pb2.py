"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#axelar/snapshot/v1beta1/types.proto\x12\x17axelar.snapshot.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto"\xaa\x01\n\x10ProxiedValidator\x12D\n\tvalidator\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12@\n\x05proxy\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0e\n\x06active\x18\x03 \x01(\x08B;Z5github.com/axelarnetwork/axelar-core/x/snapshot/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.snapshot.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/snapshot/types\xc8\xe1\x1e\x00'
    _PROXIEDVALIDATOR.fields_by_name['validator']._options = None
    _PROXIEDVALIDATOR.fields_by_name['validator']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _PROXIEDVALIDATOR.fields_by_name['proxy']._options = None
    _PROXIEDVALIDATOR.fields_by_name['proxy']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _globals['_PROXIEDVALIDATOR']._serialized_start = 117
    _globals['_PROXIEDVALIDATOR']._serialized_end = 287