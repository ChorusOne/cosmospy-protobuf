"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.reward.v1beta1 import params_pb2 as axelar_dot_reward_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/reward/v1beta1/query.proto\x12\x15axelar.reward.v1beta1\x1a\x14gogoproto/gogo.proto\x1a"axelar/reward/v1beta1/params.proto"\x16\n\x14InflationRateRequest"_\n\x15InflationRateResponse\x12F\n\x0einflation_rate\x18\x01 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"\x0f\n\rParamsRequest"E\n\x0eParamsResponse\x123\n\x06params\x18\x01 \x01(\x0b2\x1d.axelar.reward.v1beta1.ParamsB\x04\xc8\xde\x1f\x00B9Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.reward.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00'
    _INFLATIONRATERESPONSE.fields_by_name['inflation_rate']._options = None
    _INFLATIONRATERESPONSE.fields_by_name['inflation_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _PARAMSRESPONSE.fields_by_name['params']._options = None
    _PARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_INFLATIONRATEREQUEST']._serialized_start = 118
    _globals['_INFLATIONRATEREQUEST']._serialized_end = 140
    _globals['_INFLATIONRATERESPONSE']._serialized_start = 142
    _globals['_INFLATIONRATERESPONSE']._serialized_end = 237
    _globals['_PARAMSREQUEST']._serialized_start = 239
    _globals['_PARAMSREQUEST']._serialized_end = 254
    _globals['_PARAMSRESPONSE']._serialized_start = 256
    _globals['_PARAMSRESPONSE']._serialized_end = 325