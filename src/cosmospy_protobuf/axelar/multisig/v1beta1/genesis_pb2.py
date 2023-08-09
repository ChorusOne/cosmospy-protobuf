"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.multisig.v1beta1 import params_pb2 as axelar_dot_multisig_dot_v1beta1_dot_params__pb2
from ....axelar.multisig.v1beta1 import types_pb2 as axelar_dot_multisig_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%axelar/multisig/v1beta1/genesis.proto\x12\x17axelar.multisig.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$axelar/multisig/v1beta1/params.proto\x1a#axelar/multisig/v1beta1/types.proto"\xc4\x02\n\x0cGenesisState\x125\n\x06params\x18\x01 \x01(\x0b2\x1f.axelar.multisig.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12E\n\x0fkeygen_sessions\x18\x02 \x03(\x0b2&.axelar.multisig.v1beta1.KeygenSessionB\x04\xc8\xde\x1f\x00\x12G\n\x10signing_sessions\x18\x03 \x03(\x0b2\'.axelar.multisig.v1beta1.SigningSessionB\x04\xc8\xde\x1f\x00\x120\n\x04keys\x18\x04 \x03(\x0b2\x1c.axelar.multisig.v1beta1.KeyB\x04\xc8\xde\x1f\x00\x12;\n\nkey_epochs\x18\x05 \x03(\x0b2!.axelar.multisig.v1beta1.KeyEpochB\x04\xc8\xde\x1f\x00B;Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['keygen_sessions']._options = None
    _GENESISSTATE.fields_by_name['keygen_sessions']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['signing_sessions']._options = None
    _GENESISSTATE.fields_by_name['signing_sessions']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['keys']._options = None
    _GENESISSTATE.fields_by_name['keys']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['key_epochs']._options = None
    _GENESISSTATE.fields_by_name['key_epochs']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 164
    _globals['_GENESISSTATE']._serialized_end = 488