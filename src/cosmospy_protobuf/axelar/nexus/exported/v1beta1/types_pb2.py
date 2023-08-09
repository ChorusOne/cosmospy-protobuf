"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....axelar.tss.exported.v1beta1 import types_pb2 as axelar_dot_tss_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)axelar/nexus/exported/v1beta1/types.proto\x12\x1daxelar.nexus.exported.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\'axelar/tss/exported/v1beta1/types.proto"\x93\x01\n\x05Chain\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xfa\xde\x1f\tChainName\x12\x1f\n\x17supports_foreign_assets\x18\x03 \x01(\x08\x126\n\x08key_type\x18\x04 \x01(\x0e2$.axelar.tss.exported.v1beta1.KeyType\x12\x0e\n\x06module\x18\x05 \x01(\tJ\x04\x08\x02\x10\x03"_\n\x11CrossChainAddress\x129\n\x05chain\x18\x01 \x01(\x0b2$.axelar.nexus.exported.v1beta1.ChainB\x04\xc8\xde\x1f\x00\x12\x0f\n\x07address\x18\x02 \x01(\t"\xee\x01\n\x12CrossChainTransfer\x12I\n\trecipient\x18\x01 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00\x12.\n\x05asset\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12 \n\x02id\x18\x03 \x01(\x04B\x14\xe2\xde\x1f\x02ID\xfa\xde\x1f\nTransferID\x12;\n\x05state\x18\x04 \x01(\x0e2,.axelar.nexus.exported.v1beta1.TransferState"i\n\x0bTransferFee\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\xfa\x01\n\x07FeeInfo\x12\x1c\n\x05chain\x18\x01 \x01(\tB\r\xfa\xde\x1f\tChainName\x12\r\n\x05asset\x18\x02 \x01(\t\x12@\n\x08fee_rate\x18\x03 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12?\n\x07min_fee\x18\x04 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12?\n\x07max_fee\x18\x05 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int"5\n\x05Asset\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x17\n\x0fis_native_asset\x18\x03 \x01(\x08J\x04\x08\x02\x10\x03"\xc6\x04\n\x0eGeneralMessage\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID\x12F\n\x06sender\x18\x02 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00\x12I\n\trecipient\x18\x03 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cpayload_hash\x18\x04 \x01(\x0c\x12D\n\x06status\x18\x05 \x01(\x0e24.axelar.nexus.exported.v1beta1.GeneralMessage.Status\x12(\n\x05asset\x18\x06 \x01(\x0b2\x19.cosmos.base.v1beta1.Coin\x12$\n\x0csource_tx_id\x18\x07 \x01(\x0cB\x0e\xe2\xde\x1f\nSourceTxID\x12\x17\n\x0fsource_tx_index\x18\x08 \x01(\x04"\xc7\x01\n\x06Status\x12\'\n\x12STATUS_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bNonExistent\x12!\n\x0fSTATUS_APPROVED\x10\x01\x1a\x0c\x8a\x9d \x08Approved\x12%\n\x11STATUS_PROCESSING\x10\x02\x1a\x0e\x8a\x9d \nProcessing\x12!\n\x0fSTATUS_EXECUTED\x10\x03\x1a\x0c\x8a\x9d \x08Executed\x12\x1d\n\rSTATUS_FAILED\x10\x04\x1a\n\x8a\x9d \x06Failed\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01*\xcd\x01\n\rTransferState\x12\x1e\n\x1aTRANSFER_STATE_UNSPECIFIED\x10\x00\x12\'\n\x16TRANSFER_STATE_PENDING\x10\x01\x1a\x0b\x8a\x9d \x07Pending\x12)\n\x17TRANSFER_STATE_ARCHIVED\x10\x02\x1a\x0c\x8a\x9d \x08Archived\x12>\n"TRANSFER_STATE_INSUFFICIENT_AMOUNT\x10\x03\x1a\x16\x8a\x9d \x12InsufficientAmount\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01*\xac\x01\n\x11TransferDirection\x123\n\x1eTRANSFER_DIRECTION_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12-\n\x1bTRANSFER_DIRECTION_INCOMING\x10\x01\x1a\x0c\x8a\x9d \x08Incoming\x12-\n\x1bTRANSFER_DIRECTION_OUTGOING\x10\x02\x1a\x0c\x8a\x9d \x08Outgoing\x1a\x04\x88\xa3\x1e\x00B;Z5github.com/axelarnetwork/axelar-core/x/nexus/exported\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.exported.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/nexus/exported\xc8\xe1\x1e\x00'
    _TRANSFERSTATE._options = None
    _TRANSFERSTATE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _TRANSFERSTATE.values_by_name['TRANSFER_STATE_PENDING']._options = None
    _TRANSFERSTATE.values_by_name['TRANSFER_STATE_PENDING']._serialized_options = b'\x8a\x9d \x07Pending'
    _TRANSFERSTATE.values_by_name['TRANSFER_STATE_ARCHIVED']._options = None
    _TRANSFERSTATE.values_by_name['TRANSFER_STATE_ARCHIVED']._serialized_options = b'\x8a\x9d \x08Archived'
    _TRANSFERSTATE.values_by_name['TRANSFER_STATE_INSUFFICIENT_AMOUNT']._options = None
    _TRANSFERSTATE.values_by_name['TRANSFER_STATE_INSUFFICIENT_AMOUNT']._serialized_options = b'\x8a\x9d \x12InsufficientAmount'
    _TRANSFERDIRECTION._options = None
    _TRANSFERDIRECTION._serialized_options = b'\x88\xa3\x1e\x00'
    _TRANSFERDIRECTION.values_by_name['TRANSFER_DIRECTION_UNSPECIFIED']._options = None
    _TRANSFERDIRECTION.values_by_name['TRANSFER_DIRECTION_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bUnspecified'
    _TRANSFERDIRECTION.values_by_name['TRANSFER_DIRECTION_INCOMING']._options = None
    _TRANSFERDIRECTION.values_by_name['TRANSFER_DIRECTION_INCOMING']._serialized_options = b'\x8a\x9d \x08Incoming'
    _TRANSFERDIRECTION.values_by_name['TRANSFER_DIRECTION_OUTGOING']._options = None
    _TRANSFERDIRECTION.values_by_name['TRANSFER_DIRECTION_OUTGOING']._serialized_options = b'\x8a\x9d \x08Outgoing'
    _CHAIN.fields_by_name['name']._options = None
    _CHAIN.fields_by_name['name']._serialized_options = b'\xfa\xde\x1f\tChainName'
    _CROSSCHAINADDRESS.fields_by_name['chain']._options = None
    _CROSSCHAINADDRESS.fields_by_name['chain']._serialized_options = b'\xc8\xde\x1f\x00'
    _CROSSCHAINTRANSFER.fields_by_name['recipient']._options = None
    _CROSSCHAINTRANSFER.fields_by_name['recipient']._serialized_options = b'\xc8\xde\x1f\x00'
    _CROSSCHAINTRANSFER.fields_by_name['asset']._options = None
    _CROSSCHAINTRANSFER.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _CROSSCHAINTRANSFER.fields_by_name['id']._options = None
    _CROSSCHAINTRANSFER.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f\nTransferID'
    _TRANSFERFEE.fields_by_name['coins']._options = None
    _TRANSFERFEE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _FEEINFO.fields_by_name['chain']._options = None
    _FEEINFO.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f\tChainName'
    _FEEINFO.fields_by_name['fee_rate']._options = None
    _FEEINFO.fields_by_name['fee_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _FEEINFO.fields_by_name['min_fee']._options = None
    _FEEINFO.fields_by_name['min_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _FEEINFO.fields_by_name['max_fee']._options = None
    _FEEINFO.fields_by_name['max_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _GENERALMESSAGE_STATUS._options = None
    _GENERALMESSAGE_STATUS._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_UNSPECIFIED']._options = None
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bNonExistent'
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_APPROVED']._options = None
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_APPROVED']._serialized_options = b'\x8a\x9d \x08Approved'
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_PROCESSING']._options = None
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_PROCESSING']._serialized_options = b'\x8a\x9d \nProcessing'
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_EXECUTED']._options = None
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_EXECUTED']._serialized_options = b'\x8a\x9d \x08Executed'
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_FAILED']._options = None
    _GENERALMESSAGE_STATUS.values_by_name['STATUS_FAILED']._serialized_options = b'\x8a\x9d \x06Failed'
    _GENERALMESSAGE.fields_by_name['id']._options = None
    _GENERALMESSAGE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _GENERALMESSAGE.fields_by_name['sender']._options = None
    _GENERALMESSAGE.fields_by_name['sender']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENERALMESSAGE.fields_by_name['recipient']._options = None
    _GENERALMESSAGE.fields_by_name['recipient']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENERALMESSAGE.fields_by_name['source_tx_id']._options = None
    _GENERALMESSAGE.fields_by_name['source_tx_id']._serialized_options = b'\xe2\xde\x1f\nSourceTxID'
    _globals['_TRANSFERSTATE']._serialized_start = 1660
    _globals['_TRANSFERSTATE']._serialized_end = 1865
    _globals['_TRANSFERDIRECTION']._serialized_start = 1868
    _globals['_TRANSFERDIRECTION']._serialized_end = 2040
    _globals['_CHAIN']._serialized_start = 172
    _globals['_CHAIN']._serialized_end = 319
    _globals['_CROSSCHAINADDRESS']._serialized_start = 321
    _globals['_CROSSCHAINADDRESS']._serialized_end = 416
    _globals['_CROSSCHAINTRANSFER']._serialized_start = 419
    _globals['_CROSSCHAINTRANSFER']._serialized_end = 657
    _globals['_TRANSFERFEE']._serialized_start = 659
    _globals['_TRANSFERFEE']._serialized_end = 764
    _globals['_FEEINFO']._serialized_start = 767
    _globals['_FEEINFO']._serialized_end = 1017
    _globals['_ASSET']._serialized_start = 1019
    _globals['_ASSET']._serialized_end = 1072
    _globals['_GENERALMESSAGE']._serialized_start = 1075
    _globals['_GENERALMESSAGE']._serialized_end = 1657
    _globals['_GENERALMESSAGE_STATUS']._serialized_start = 1458
    _globals['_GENERALMESSAGE_STATUS']._serialized_end = 1657