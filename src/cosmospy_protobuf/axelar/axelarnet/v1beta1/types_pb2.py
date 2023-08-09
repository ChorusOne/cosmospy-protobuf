"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$axelar/axelarnet/v1beta1/types.proto\x12\x18axelar.axelarnet.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xc1\x04\n\x0bIBCTransfer\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12.\n\x05token\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x1b\n\x07port_id\x18\x04 \x01(\tB\n\xe2\xde\x1f\x06PortID\x12!\n\nchannel_id\x18\x05 \x01(\tB\r\xe2\xde\x1f\tChannelID\x12\x14\n\x08sequence\x18\x06 \x01(\x04B\x02\x18\x01\x12V\n\x02id\x18\x07 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12<\n\x06status\x18\x08 \x01(\x0e2,.axelar.axelarnet.v1beta1.IBCTransfer.Status"\xc0\x01\n\x06Status\x12/\n\x12STATUS_UNSPECIFIED\x10\x00\x1a\x17\x8a\x9d \x13TransferNonExistent\x12\'\n\x0eSTATUS_PENDING\x10\x01\x1a\x13\x8a\x9d \x0fTransferPending\x12+\n\x10STATUS_COMPLETED\x10\x02\x1a\x15\x8a\x9d \x11TransferCompleted\x12%\n\rSTATUS_FAILED\x10\x03\x1a\x12\x8a\x9d \x0eTransferFailed\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01"\xcd\x01\n\x0bCosmosChain\x12Q\n\x04name\x18\x01 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x1d\n\x08ibc_path\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07IBCPath\x127\n\x06assets\x18\x03 \x03(\x0b2\x1f.axelar.axelarnet.v1beta1.AssetB\x06\x18\x01\xc8\xde\x1f\x00\x12\x13\n\x0baddr_prefix\x18\x04 \x01(\t"^\n\x05Asset\x12\r\n\x05denom\x18\x01 \x01(\t\x12B\n\nmin_amount\x18\x02 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int:\x02\x18\x01"|\n\x03Fee\x12/\n\x06amount\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12D\n\trecipient\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB<Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.axelarnet.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00'
    _IBCTRANSFER_STATUS._options = None
    _IBCTRANSFER_STATUS._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _IBCTRANSFER_STATUS.values_by_name['STATUS_UNSPECIFIED']._options = None
    _IBCTRANSFER_STATUS.values_by_name['STATUS_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x13TransferNonExistent'
    _IBCTRANSFER_STATUS.values_by_name['STATUS_PENDING']._options = None
    _IBCTRANSFER_STATUS.values_by_name['STATUS_PENDING']._serialized_options = b'\x8a\x9d \x0fTransferPending'
    _IBCTRANSFER_STATUS.values_by_name['STATUS_COMPLETED']._options = None
    _IBCTRANSFER_STATUS.values_by_name['STATUS_COMPLETED']._serialized_options = b'\x8a\x9d \x11TransferCompleted'
    _IBCTRANSFER_STATUS.values_by_name['STATUS_FAILED']._options = None
    _IBCTRANSFER_STATUS.values_by_name['STATUS_FAILED']._serialized_options = b'\x8a\x9d \x0eTransferFailed'
    _IBCTRANSFER.fields_by_name['sender']._options = None
    _IBCTRANSFER.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _IBCTRANSFER.fields_by_name['token']._options = None
    _IBCTRANSFER.fields_by_name['token']._serialized_options = b'\xc8\xde\x1f\x00'
    _IBCTRANSFER.fields_by_name['port_id']._options = None
    _IBCTRANSFER.fields_by_name['port_id']._serialized_options = b'\xe2\xde\x1f\x06PortID'
    _IBCTRANSFER.fields_by_name['channel_id']._options = None
    _IBCTRANSFER.fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _IBCTRANSFER.fields_by_name['sequence']._options = None
    _IBCTRANSFER.fields_by_name['sequence']._serialized_options = b'\x18\x01'
    _IBCTRANSFER.fields_by_name['id']._options = None
    _IBCTRANSFER.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _COSMOSCHAIN.fields_by_name['name']._options = None
    _COSMOSCHAIN.fields_by_name['name']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _COSMOSCHAIN.fields_by_name['ibc_path']._options = None
    _COSMOSCHAIN.fields_by_name['ibc_path']._serialized_options = b'\xe2\xde\x1f\x07IBCPath'
    _COSMOSCHAIN.fields_by_name['assets']._options = None
    _COSMOSCHAIN.fields_by_name['assets']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00'
    _ASSET.fields_by_name['min_amount']._options = None
    _ASSET.fields_by_name['min_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _ASSET._options = None
    _ASSET._serialized_options = b'\x18\x01'
    _FEE.fields_by_name['amount']._options = None
    _FEE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _FEE.fields_by_name['recipient']._options = None
    _FEE.fields_by_name['recipient']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _globals['_IBCTRANSFER']._serialized_start = 121
    _globals['_IBCTRANSFER']._serialized_end = 698
    _globals['_IBCTRANSFER_STATUS']._serialized_start = 506
    _globals['_IBCTRANSFER_STATUS']._serialized_end = 698
    _globals['_COSMOSCHAIN']._serialized_start = 701
    _globals['_COSMOSCHAIN']._serialized_end = 906
    _globals['_ASSET']._serialized_start = 908
    _globals['_ASSET']._serialized_end = 1002
    _globals['_FEE']._serialized_start = 1004
    _globals['_FEE']._serialized_end = 1128