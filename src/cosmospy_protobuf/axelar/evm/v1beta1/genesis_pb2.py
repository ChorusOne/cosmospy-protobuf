"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....axelar.utils.v1beta1 import queuer_pb2 as axelar_dot_utils_dot_v1beta1_dot_queuer__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.evm.v1beta1 import params_pb2 as axelar_dot_evm_dot_v1beta1_dot_params__pb2
from ....axelar.evm.v1beta1 import types_pb2 as axelar_dot_evm_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/evm/v1beta1/genesis.proto\x12\x12axelar.evm.v1beta1\x1a!axelar/utils/v1beta1/queuer.proto\x1a\x14gogoproto/gogo.proto\x1a\x1faxelar/evm/v1beta1/params.proto\x1a\x1eaxelar/evm/v1beta1/types.proto"\xd4\x06\n\x0cGenesisState\x12<\n\x06chains\x18\x03 \x03(\x0b2&.axelar.evm.v1beta1.GenesisState.ChainB\x04\xc8\xde\x1f\x00\x1a\xff\x05\n\x05Chain\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.axelar.evm.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12:\n\x0cburner_infos\x18\x02 \x03(\x0b2\x1e.axelar.evm.v1beta1.BurnerInfoB\x04\xc8\xde\x1f\x00\x12=\n\rcommand_queue\x18\x03 \x01(\x0b2 .axelar.utils.v1beta1.QueueStateB\x04\xc8\xde\x1f\x00\x12B\n\x12confirmed_deposits\x18\x04 \x03(\x0b2 .axelar.evm.v1beta1.ERC20DepositB\x04\xc8\xde\x1f\x00\x12?\n\x0fburned_deposits\x18\x05 \x03(\x0b2 .axelar.evm.v1beta1.ERC20DepositB\x04\xc8\xde\x1f\x00\x12G\n\x0fcommand_batches\x18\x08 \x03(\x0b2(.axelar.evm.v1beta1.CommandBatchMetadataB\x04\xc8\xde\x1f\x00\x122\n\x07gateway\x18\t \x01(\x0b2\x1b.axelar.evm.v1beta1.GatewayB\x04\xc8\xde\x1f\x00\x12<\n\x06tokens\x18\n \x03(\x0b2&.axelar.evm.v1beta1.ERC20TokenMetadataB\x04\xc8\xde\x1f\x00\x12/\n\x06events\x18\x0b \x03(\x0b2\x19.axelar.evm.v1beta1.EventB\x04\xc8\xde\x1f\x00\x12E\n\x15confirmed_event_queue\x18\x0c \x01(\x0b2 .axelar.utils.v1beta1.QueueStateB\x04\xc8\xde\x1f\x00\x12I\n\x19legacy_confirmed_deposits\x18\r \x03(\x0b2 .axelar.evm.v1beta1.ERC20DepositB\x04\xc8\xde\x1f\x00\x12F\n\x16legacy_burned_deposits\x18\x0e \x03(\x0b2 .axelar.evm.v1beta1.ERC20DepositB\x04\xc8\xde\x1f\x00:\x04\x98\xa1\x1f\x01B6Z0github.com/axelarnetwork/axelar-core/x/evm/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.evm.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/evm/types\xc8\xe1\x1e\x00'
    _GENESISSTATE_CHAIN.fields_by_name['params']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['burner_infos']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['burner_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['command_queue']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['command_queue']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['confirmed_deposits']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['confirmed_deposits']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['burned_deposits']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['burned_deposits']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['command_batches']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['command_batches']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['gateway']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['gateway']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['tokens']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['tokens']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['events']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['events']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['confirmed_event_queue']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['confirmed_event_queue']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['legacy_confirmed_deposits']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['legacy_confirmed_deposits']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE_CHAIN.fields_by_name['legacy_burned_deposits']._options = None
    _GENESISSTATE_CHAIN.fields_by_name['legacy_burned_deposits']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['chains']._options = None
    _GENESISSTATE.fields_by_name['chains']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._options = None
    _GENESISSTATE._serialized_options = b'\x98\xa1\x1f\x01'
    _globals['_GENESISSTATE']._serialized_start = 179
    _globals['_GENESISSTATE']._serialized_end = 1031
    _globals['_GENESISSTATE_CHAIN']._serialized_start = 258
    _globals['_GENESISSTATE_CHAIN']._serialized_end = 1025