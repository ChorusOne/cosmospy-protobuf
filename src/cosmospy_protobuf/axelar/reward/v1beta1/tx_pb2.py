"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eaxelar/reward/v1beta1/tx.proto\x12\x15axelar.reward.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\x98\x01\n\x10RefundMsgRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12;\n\rinner_message\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x0e\xca\xb4-\nRefundable:\x04\x80\xb5\x18\x01".\n\x11RefundMsgResponse\x12\x0c\n\x04data\x18\x01 \x01(\x0c\x12\x0b\n\x03log\x18\x02 \x01(\tB9Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.reward.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00'
    _REFUNDMSGREQUEST.fields_by_name['sender']._options = None
    _REFUNDMSGREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REFUNDMSGREQUEST.fields_by_name['inner_message']._options = None
    _REFUNDMSGREQUEST.fields_by_name['inner_message']._serialized_options = b'\xca\xb4-\nRefundable'
    _REFUNDMSGREQUEST._options = None
    _REFUNDMSGREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _globals['_REFUNDMSGREQUEST']._serialized_start = 182
    _globals['_REFUNDMSGREQUEST']._serialized_end = 334
    _globals['_REFUNDMSGRESPONSE']._serialized_start = 336
    _globals['_REFUNDMSGRESPONSE']._serialized_end = 382