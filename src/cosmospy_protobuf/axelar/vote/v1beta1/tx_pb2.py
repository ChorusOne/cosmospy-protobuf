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
from ....axelar.vote.v1beta1 import types_pb2 as axelar_dot_vote_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1caxelar/vote/v1beta1/tx.proto\x12\x13axelar.vote.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a.axelar/permission/exported/v1beta1/types.proto\x1a\x1faxelar/vote/v1beta1/types.proto"\x92\x02\n\x0bVoteRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12^\n\x07poll_id\x18\x04 \x01(\x04BM\xc8\xde\x1f\x00\xda\xde\x1f;github.com/axelarnetwork/axelar-core/x/vote/exported.PollID\xe2\xde\x1f\x06PollID\x12N\n\x04vote\x18\x05 \x01(\x0b2\x14.google.protobuf.AnyB*\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler:\x04\x80\xb5\x18\x01J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04"\x1b\n\x0cVoteResponse\x12\x0b\n\x03log\x18\x01 \x01(\tB7Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.vote.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc8\xe1\x1e\x00'
    _VOTEREQUEST.fields_by_name['sender']._options = None
    _VOTEREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _VOTEREQUEST.fields_by_name['poll_id']._options = None
    _VOTEREQUEST.fields_by_name['poll_id']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f;github.com/axelarnetwork/axelar-core/x/vote/exported.PollID\xe2\xde\x1f\x06PollID'
    _VOTEREQUEST.fields_by_name['vote']._options = None
    _VOTEREQUEST.fields_by_name['vote']._serialized_options = b'\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler'
    _VOTEREQUEST._options = None
    _VOTEREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _globals['_VOTEREQUEST']._serialized_start = 211
    _globals['_VOTEREQUEST']._serialized_end = 485
    _globals['_VOTERESPONSE']._serialized_start = 487
    _globals['_VOTERESPONSE']._serialized_end = 514