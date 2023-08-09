"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.snapshot.v1beta1 import tx_pb2 as axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2
from ....axelar.tss.v1beta1 import tx_pb2 as axelar_dot_tss_dot_v1beta1_dot_tx__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/tss/v1beta1/service.proto\x12\x12axelar.tss.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a axelar/snapshot/v1beta1/tx.proto\x1a\x1baxelar/tss/v1beta1/tx.proto2\x88\x01\n\nMsgService\x12z\n\tHeartBeat\x12$.axelar.tss.v1beta1.HeartBeatRequest\x1a%.axelar.tss.v1beta1.HeartBeatResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/axelar/tss/heartbeat:\x01*2\x0e\n\x0cQueryServiceB6Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['HeartBeat']._options = None
    _MSGSERVICE.methods_by_name['HeartBeat']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/axelar/tss/heartbeat:\x01*'
    _globals['_MSGSERVICE']._serialized_start = 172
    _globals['_MSGSERVICE']._serialized_end = 308
    _globals['_QUERYSERVICE']._serialized_start = 310
    _globals['_QUERYSERVICE']._serialized_end = 324