"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"axelar/reward/v1beta1/params.proto\x12\x15axelar.reward.v1beta1\x1a\x14gogoproto/gogo.proto"\xc0\x01\n\x06Params\x12\\\n$external_chain_voting_inflation_rate\x18\x01 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12X\n key_mgmt_relative_inflation_rate\x18\x02 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecB9Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.reward.v1beta1.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/axelarnetwork/axelar-core/x/reward/types\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['external_chain_voting_inflation_rate']._options = None
    _PARAMS.fields_by_name['external_chain_voting_inflation_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _PARAMS.fields_by_name['key_mgmt_relative_inflation_rate']._options = None
    _PARAMS.fields_by_name['key_mgmt_relative_inflation_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _globals['_PARAMS']._serialized_start = 84
    _globals['_PARAMS']._serialized_end = 276