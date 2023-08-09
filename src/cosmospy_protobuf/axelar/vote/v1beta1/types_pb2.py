"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....axelar.vote.exported.v1beta1 import types_pb2 as axelar_dot_vote_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1faxelar/vote/v1beta1/types.proto\x12\x13axelar.vote.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a(axelar/vote/exported/v1beta1/types.proto"\x87\x03\n\x0bTalliedVote\x12>\n\x05tally\x18\x01 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12N\n\x04data\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB*\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler\x12^\n\x07poll_id\x18\x04 \x01(\x04BM\xc8\xde\x1f\x00\xda\xde\x1f;github.com/axelarnetwork/axelar-core/x/vote/exported.PollID\xe2\xde\x1f\x06PollID\x12H\n\ris_voter_late\x18\x05 \x03(\x0b21.axelar.vote.v1beta1.TalliedVote.IsVoterLateEntry\x1a2\n\x10IsVoterLateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x028\x01:\x04\x98\xa1\x1f\x01J\x04\x08\x02\x10\x03B7Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.vote.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc8\xe1\x1e\x00'
    _TALLIEDVOTE_ISVOTERLATEENTRY._options = None
    _TALLIEDVOTE_ISVOTERLATEENTRY._serialized_options = b'8\x01'
    _TALLIEDVOTE.fields_by_name['tally']._options = None
    _TALLIEDVOTE.fields_by_name['tally']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _TALLIEDVOTE.fields_by_name['data']._options = None
    _TALLIEDVOTE.fields_by_name['data']._serialized_options = b'\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler'
    _TALLIEDVOTE.fields_by_name['poll_id']._options = None
    _TALLIEDVOTE.fields_by_name['poll_id']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f;github.com/axelarnetwork/axelar-core/x/vote/exported.PollID\xe2\xde\x1f\x06PollID'
    _TALLIEDVOTE._options = None
    _TALLIEDVOTE._serialized_options = b'\x98\xa1\x1f\x01'
    _globals['_TALLIEDVOTE']._serialized_start = 175
    _globals['_TALLIEDVOTE']._serialized_end = 566
    _globals['_TALLIEDVOTE_ISVOTERLATEENTRY']._serialized_start = 504
    _globals['_TALLIEDVOTE_ISVOTERLATEENTRY']._serialized_end = 554