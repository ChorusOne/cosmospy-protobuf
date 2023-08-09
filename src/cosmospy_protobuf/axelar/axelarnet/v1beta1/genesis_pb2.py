"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.axelarnet.v1beta1 import params_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_params__pb2
from ....axelar.axelarnet.v1beta1 import types_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_types__pb2
from ....axelar.utils.v1beta1 import queuer_pb2 as axelar_dot_utils_dot_v1beta1_dot_queuer__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&axelar/axelarnet/v1beta1/genesis.proto\x12\x18axelar.axelarnet.v1beta1\x1a\x14gogoproto/gogo.proto\x1a%axelar/axelarnet/v1beta1/params.proto\x1a$axelar/axelarnet/v1beta1/types.proto\x1a!axelar/utils/v1beta1/queuer.proto"\x94\x04\n\x0cGenesisState\x126\n\x06params\x18\x01 \x01(\x0b2 .axelar.axelarnet.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12L\n\x11collector_address\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12;\n\x06chains\x18\x03 \x03(\x0b2%.axelar.axelarnet.v1beta1.CosmosChainB\x04\xc8\xde\x1f\x00\x12>\n\x0etransfer_queue\x18\x05 \x01(\x0b2 .axelar.utils.v1beta1.QueueStateB\x04\xc8\xde\x1f\x00\x12R\n\ribc_transfers\x18\x07 \x03(\x0b2%.axelar.axelarnet.v1beta1.IBCTransferB\x14\xc8\xde\x1f\x00\xe2\xde\x1f\x0cIBCTransfers\x12f\n\x0eseq_id_mapping\x18\x08 \x03(\x0b28.axelar.axelarnet.v1beta1.GenesisState.SeqIdMappingEntryB\x14\xc8\xde\x1f\x00\xe2\xde\x1f\x0cSeqIDMapping\x1a3\n\x11SeqIdMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x028\x01:\x04\x98\xa1\x1f\x01J\x04\x08\x04\x10\x05J\x04\x08\x06\x10\x07B<Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.axelarnet.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00'
    _GENESISSTATE_SEQIDMAPPINGENTRY._options = None
    _GENESISSTATE_SEQIDMAPPINGENTRY._serialized_options = b'8\x01'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['collector_address']._options = None
    _GENESISSTATE.fields_by_name['collector_address']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _GENESISSTATE.fields_by_name['chains']._options = None
    _GENESISSTATE.fields_by_name['chains']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['transfer_queue']._options = None
    _GENESISSTATE.fields_by_name['transfer_queue']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['ibc_transfers']._options = None
    _GENESISSTATE.fields_by_name['ibc_transfers']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0cIBCTransfers'
    _GENESISSTATE.fields_by_name['seq_id_mapping']._options = None
    _GENESISSTATE.fields_by_name['seq_id_mapping']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0cSeqIDMapping'
    _GENESISSTATE._options = None
    _GENESISSTATE._serialized_options = b'\x98\xa1\x1f\x01'
    _globals['_GENESISSTATE']._serialized_start = 203
    _globals['_GENESISSTATE']._serialized_end = 735
    _globals['_GENESISSTATE_SEQIDMAPPINGENTRY']._serialized_start = 666
    _globals['_GENESISSTATE_SEQIDMAPPINGENTRY']._serialized_end = 717