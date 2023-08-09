"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.vote.v1beta1 import tx_pb2 as axelar_dot_vote_dot_v1beta1_dot_tx__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/vote/v1beta1/service.proto\x12\x13axelar.vote.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1caxelar/vote/v1beta1/tx.proto2w\n\nMsgService\x12i\n\x04Vote\x12 .axelar.vote.v1beta1.VoteRequest\x1a!.axelar.vote.v1beta1.VoteResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/axelar/vote/vote:\x01*B7Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.vote.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['Vote']._options = None
    _MSGSERVICE.methods_by_name['Vote']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/axelar/vote/vote:\x01*'
    _globals['_MSGSERVICE']._serialized_start = 140
    _globals['_MSGSERVICE']._serialized_end = 259