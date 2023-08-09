"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.reward.v1beta1 import tx_pb2 as axelar_dot_reward_dot_v1beta1_dot_tx__pb2
from ....axelar.reward.v1beta1 import query_pb2 as axelar_dot_reward_dot_v1beta1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#axelar/reward/v1beta1/service.proto\x12\x15axelar.reward.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1eaxelar/reward/v1beta1/tx.proto\x1a!axelar/reward/v1beta1/query.proto2\x97\x01\n\nMsgService\x12\x88\x01\n\tRefundMsg\x12\'.axelar.reward.v1beta1.RefundMsgRequest\x1a(.axelar.reward.v1beta1.RefundMsgResponse"(\x82\xd3\xe4\x93\x02""\x1d/axelar/reward/refund_message:\x01*2\xa8\x02\n\x0cQueryService\x12\x99\x01\n\rInflationRate\x12+.axelar.reward.v1beta1.InflationRateRequest\x1a,.axelar.reward.v1beta1.InflationRateResponse"-\x82\xd3\xe4\x93\x02\'\x12%/axelar/reward/v1beta1/inflation_rate\x12|\n\x06Params\x12$.axelar.reward.v1beta1.ParamsRequest\x1a%.axelar.reward.v1beta1.ParamsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/axelar/reward/v1beta1/paramsB9Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.reward.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['RefundMsg']._options = None
    _MSGSERVICE.methods_by_name['RefundMsg']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/axelar/reward/refund_message:\x01*'
    _QUERYSERVICE.methods_by_name['InflationRate']._options = None
    _QUERYSERVICE.methods_by_name['InflationRate']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/axelar/reward/v1beta1/inflation_rate"
    _QUERYSERVICE.methods_by_name['Params']._options = None
    _QUERYSERVICE.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/axelar/reward/v1beta1/params'
    _globals['_MSGSERVICE']._serialized_start = 182
    _globals['_MSGSERVICE']._serialized_end = 333
    _globals['_QUERYSERVICE']._serialized_start = 336
    _globals['_QUERYSERVICE']._serialized_end = 632