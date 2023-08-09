"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.crypto.multisig import keys_pb2 as cosmos_dot_crypto_dot_multisig_dot_keys__pb2
from ....axelar.permission.v1beta1 import types_pb2 as axelar_dot_permission_dot_v1beta1_dot_types__pb2
from ....axelar.permission.v1beta1 import params_pb2 as axelar_dot_permission_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'axelar/permission/v1beta1/genesis.proto\x12\x19axelar.permission.v1beta1\x1a\x14gogoproto/gogo.proto\x1a!cosmos/crypto/multisig/keys.proto\x1a%axelar/permission/v1beta1/types.proto\x1a&axelar/permission/v1beta1/params.proto"\xcd\x01\n\x0cGenesisState\x127\n\x06params\x18\x01 \x01(\x0b2!.axelar.permission.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12A\n\x0egovernance_key\x18\x02 \x01(\x0b2).cosmos.crypto.multisig.LegacyAminoPubKey\x12A\n\x0cgov_accounts\x18\x03 \x03(\x0b2%.axelar.permission.v1beta1.GovAccountB\x04\xc8\xde\x1f\x00B=Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.permission.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['gov_accounts']._options = None
    _GENESISSTATE.fields_by_name['gov_accounts']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 207
    _globals['_GENESISSTATE']._serialized_end = 412