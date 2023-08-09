"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .....axelar.snapshot.exported.v1beta1 import types_pb2 as axelar_dot_snapshot_dot_exported_dot_v1beta1_dot_types__pb2
from .....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(axelar/vote/exported/v1beta1/types.proto\x12\x1caxelar.vote.exported.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a,axelar/snapshot/exported/v1beta1/types.proto\x1a$axelar/utils/v1beta1/threshold.proto"\xb5\x04\n\x0cPollMetadata\x12\x12\n\nexpires_at\x18\x03 \x01(\x03\x12P\n\x06result\x18\x04 \x01(\x0b2\x14.google.protobuf.AnyB*\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler\x12?\n\x10voting_threshold\x18\x05 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x126\n\x05state\x18\x06 \x01(\x0e2\'.axelar.vote.exported.v1beta1.PollState\x12\x17\n\x0fmin_voter_count\x18\x07 \x01(\x03\x12\x18\n\x10reward_pool_name\x18\n \x01(\t\x12\x14\n\x0cgrace_period\x18\x0b \x01(\x03\x12\x14\n\x0ccompleted_at\x18\x0c \x01(\x03\x12 \n\x02id\x18\r \x01(\x04B\x14\xc8\xde\x1f\x00\xda\xde\x1f\x06PollID\xe2\xde\x1f\x02ID\x12B\n\x08snapshot\x18\x0f \x01(\x0b2*.axelar.snapshot.exported.v1beta1.SnapshotB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06module\x18\x10 \x01(\t\x12Y\n\x0fmodule_metadata\x18\x11 \x01(\x0b2\x14.google.protobuf.AnyB*\xca\xb4-&github.com/cosmos/codec/ProtoMarshalerJ\x04\x08\x01\x10\x02J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\x0e\x10\x0f"5\n\x07PollKey\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\tB\x06\xe2\xde\x1f\x02ID:\x06\x18\x01\x98\xa0\x1f\x00"\x86\x01\n\x10PollParticipants\x12)\n\x07poll_id\x18\x01 \x01(\x04B\x18\xc8\xde\x1f\x00\xda\xde\x1f\x06PollID\xe2\xde\x1f\x06PollID\x12G\n\x0cparticipants\x18\x02 \x03(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress*\xb3\x01\n\tPollState\x12+\n\x16POLL_STATE_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bNonExistent\x12#\n\x12POLL_STATE_PENDING\x10\x01\x1a\x0b\x8a\x9d \x07Pending\x12\'\n\x14POLL_STATE_COMPLETED\x10\x02\x1a\r\x8a\x9d \tCompleted\x12!\n\x11POLL_STATE_FAILED\x10\x03\x1a\n\x8a\x9d \x06Failed\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01B:Z4github.com/axelarnetwork/axelar-core/x/vote/exported\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.vote.exported.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/axelarnetwork/axelar-core/x/vote/exported\xc8\xe1\x1e\x00'
    _POLLSTATE._options = None
    _POLLSTATE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _POLLSTATE.values_by_name['POLL_STATE_UNSPECIFIED']._options = None
    _POLLSTATE.values_by_name['POLL_STATE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bNonExistent'
    _POLLSTATE.values_by_name['POLL_STATE_PENDING']._options = None
    _POLLSTATE.values_by_name['POLL_STATE_PENDING']._serialized_options = b'\x8a\x9d \x07Pending'
    _POLLSTATE.values_by_name['POLL_STATE_COMPLETED']._options = None
    _POLLSTATE.values_by_name['POLL_STATE_COMPLETED']._serialized_options = b'\x8a\x9d \tCompleted'
    _POLLSTATE.values_by_name['POLL_STATE_FAILED']._options = None
    _POLLSTATE.values_by_name['POLL_STATE_FAILED']._serialized_options = b'\x8a\x9d \x06Failed'
    _POLLMETADATA.fields_by_name['result']._options = None
    _POLLMETADATA.fields_by_name['result']._serialized_options = b'\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler'
    _POLLMETADATA.fields_by_name['voting_threshold']._options = None
    _POLLMETADATA.fields_by_name['voting_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _POLLMETADATA.fields_by_name['id']._options = None
    _POLLMETADATA.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x06PollID\xe2\xde\x1f\x02ID'
    _POLLMETADATA.fields_by_name['snapshot']._options = None
    _POLLMETADATA.fields_by_name['snapshot']._serialized_options = b'\xc8\xde\x1f\x00'
    _POLLMETADATA.fields_by_name['module_metadata']._options = None
    _POLLMETADATA.fields_by_name['module_metadata']._serialized_options = b'\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler'
    _POLLKEY.fields_by_name['id']._options = None
    _POLLKEY.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _POLLKEY._options = None
    _POLLKEY._serialized_options = b'\x18\x01\x98\xa0\x1f\x00'
    _POLLPARTICIPANTS.fields_by_name['poll_id']._options = None
    _POLLPARTICIPANTS.fields_by_name['poll_id']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x06PollID\xe2\xde\x1f\x06PollID'
    _POLLPARTICIPANTS.fields_by_name['participants']._options = None
    _POLLPARTICIPANTS.fields_by_name['participants']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _globals['_POLLSTATE']._serialized_start = 995
    _globals['_POLLSTATE']._serialized_end = 1174
    _globals['_POLLMETADATA']._serialized_start = 235
    _globals['_POLLMETADATA']._serialized_end = 800
    _globals['_POLLKEY']._serialized_start = 802
    _globals['_POLLKEY']._serialized_end = 855
    _globals['_POLLPARTICIPANTS']._serialized_start = 858
    _globals['_POLLPARTICIPANTS']._serialized_end = 992