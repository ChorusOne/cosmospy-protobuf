"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/reward/v1beta1/types.proto\x12\x15axelar.reward.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xfc\x01\n\x04Pool\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x07rewards\x18\x02 \x03(\x0b2".axelar.reward.v1beta1.Pool.RewardB\x04\xc8\xde\x1f\x00\x1a\xaa\x01\n\x06Reward\x12D\n\tvalidator\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\xa5\x01\n\x06Refund\x12@\n\x05payer\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12Y\n\x04fees\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsB9Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.reward.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00'
    _POOL_REWARD.fields_by_name['validator']._options = None
    _POOL_REWARD.fields_by_name['validator']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _POOL_REWARD.fields_by_name['coins']._options = None
    _POOL_REWARD.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _POOL.fields_by_name['rewards']._options = None
    _POOL.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _REFUND.fields_by_name['payer']._options = None
    _REFUND.fields_by_name['payer']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REFUND.fields_by_name['fees']._options = None
    _REFUND.fields_by_name['fees']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_POOL']._serialized_start = 115
    _globals['_POOL']._serialized_end = 367
    _globals['_POOL_REWARD']._serialized_start = 197
    _globals['_POOL_REWARD']._serialized_end = 367
    _globals['_REFUND']._serialized_start = 370
    _globals['_REFUND']._serialized_end = 535