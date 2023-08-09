"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.nexus.exported.v1beta1 import types_pb2 as axelar_dot_nexus_dot_exported_dot_v1beta1_dot_types__pb2
from ....axelar.nexus.v1beta1 import types_pb2 as axelar_dot_nexus_dot_v1beta1_dot_types__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/nexus/v1beta1/query.proto\x12\x14axelar.nexus.v1beta1\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\x1a)axelar/nexus/exported/v1beta1/types.proto\x1a axelar/nexus/v1beta1/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"(\n\x17ChainMaintainersRequest\x12\r\n\x05chain\x18\x01 \x01(\t"b\n\x18ChainMaintainersResponse\x12F\n\x0bmaintainers\x18\x01 \x03(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress"e\n\x1bLatestDepositAddressRequest\x12\x16\n\x0erecipient_addr\x18\x01 \x01(\t\x12\x17\n\x0frecipient_chain\x18\x02 \x01(\t\x12\x15\n\rdeposit_chain\x18\x03 \x01(\t"4\n\x1cLatestDepositAddressResponse\x12\x14\n\x0cdeposit_addr\x18\x01 \x01(\t"\xa2\x01\n\x18TransfersForChainRequest\x12\r\n\x05chain\x18\x01 \x01(\t\x12;\n\x05state\x18\x02 \x01(\x0e2,.axelar.nexus.exported.v1beta1.TransferState\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xa4\x01\n\x19TransfersForChainResponse\x12J\n\ttransfers\x18\x01 \x03(\x0b21.axelar.nexus.exported.v1beta1.CrossChainTransferB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse".\n\x0eFeeInfoRequest\x12\r\n\x05chain\x18\x01 \x01(\t\x12\r\n\x05asset\x18\x02 \x01(\t"K\n\x0fFeeInfoResponse\x128\n\x08fee_info\x18\x01 \x01(\x0b2&.axelar.nexus.exported.v1beta1.FeeInfo"U\n\x12TransferFeeRequest\x12\x14\n\x0csource_chain\x18\x01 \x01(\t\x12\x19\n\x11destination_chain\x18\x02 \x01(\t\x12\x0e\n\x06amount\x18\x03 \x01(\t"C\n\x13TransferFeeResponse\x12,\n\x03fee\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"B\n\rChainsRequest\x121\n\x06status\x18\x01 \x01(\x0e2!.axelar.nexus.v1beta1.ChainStatus"e\n\x0eChainsResponse\x12S\n\x06chains\x18\x01 \x03(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName"\x1e\n\rAssetsRequest\x12\r\n\x05chain\x18\x01 \x01(\t" \n\x0eAssetsResponse\x12\x0e\n\x06assets\x18\x01 \x03(\t""\n\x11ChainStateRequest\x12\r\n\x05chain\x18\x01 \x01(\t"K\n\x12ChainStateResponse\x125\n\x05state\x18\x01 \x01(\x0b2 .axelar.nexus.v1beta1.ChainStateB\x04\xc8\xde\x1f\x00"%\n\x14ChainsByAssetRequest\x12\r\n\x05asset\x18\x01 \x01(\t"l\n\x15ChainsByAssetResponse\x12S\n\x06chains\x18\x01 \x03(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName"F\n\x17RecipientAddressRequest\x12\x14\n\x0cdeposit_addr\x18\x01 \x01(\t\x12\x15\n\rdeposit_chain\x18\x02 \x01(\t"K\n\x18RecipientAddressResponse\x12\x16\n\x0erecipient_addr\x18\x01 \x01(\t\x12\x17\n\x0frecipient_chain\x18\x02 \x01(\t"8\n\x18TransferRateLimitRequest\x12\r\n\x05chain\x18\x01 \x01(\t\x12\r\n\x05asset\x18\x02 \x01(\t"a\n\x19TransferRateLimitResponse\x12D\n\x13transfer_rate_limit\x18\x01 \x01(\x0b2\'.axelar.nexus.v1beta1.TransferRateLimit"\xc3\x02\n\x11TransferRateLimit\x12=\n\x05limit\x18\x01 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x123\n\x06window\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12@\n\x08incoming\x18\x03 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12@\n\x08outgoing\x18\x04 \x01(\x0cB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x126\n\ttime_left\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01"$\n\x0eMessageRequest\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID"W\n\x0fMessageResponse\x12D\n\x07message\x18\x01 \x01(\x0b2-.axelar.nexus.exported.v1beta1.GeneralMessageB\x04\xc8\xde\x1f\x00*\x9c\x01\n\x0bChainStatus\x12-\n\x18CHAIN_STATUS_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12)\n\x16CHAIN_STATUS_ACTIVATED\x10\x01\x1a\r\x8a\x9d \tActivated\x12-\n\x18CHAIN_STATUS_DEACTIVATED\x10\x02\x1a\x0f\x8a\x9d \x0bDeactivated\x1a\x04\x88\xa3\x1e\x00B8Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00'
    _CHAINSTATUS._options = None
    _CHAINSTATUS._serialized_options = b'\x88\xa3\x1e\x00'
    _CHAINSTATUS.values_by_name['CHAIN_STATUS_UNSPECIFIED']._options = None
    _CHAINSTATUS.values_by_name['CHAIN_STATUS_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bUnspecified'
    _CHAINSTATUS.values_by_name['CHAIN_STATUS_ACTIVATED']._options = None
    _CHAINSTATUS.values_by_name['CHAIN_STATUS_ACTIVATED']._serialized_options = b'\x8a\x9d \tActivated'
    _CHAINSTATUS.values_by_name['CHAIN_STATUS_DEACTIVATED']._options = None
    _CHAINSTATUS.values_by_name['CHAIN_STATUS_DEACTIVATED']._serialized_options = b'\x8a\x9d \x0bDeactivated'
    _CHAINMAINTAINERSRESPONSE.fields_by_name['maintainers']._options = None
    _CHAINMAINTAINERSRESPONSE.fields_by_name['maintainers']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _TRANSFERSFORCHAINRESPONSE.fields_by_name['transfers']._options = None
    _TRANSFERSFORCHAINRESPONSE.fields_by_name['transfers']._serialized_options = b'\xc8\xde\x1f\x00'
    _TRANSFERFEERESPONSE.fields_by_name['fee']._options = None
    _TRANSFERFEERESPONSE.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _CHAINSRESPONSE.fields_by_name['chains']._options = None
    _CHAINSRESPONSE.fields_by_name['chains']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CHAINSTATERESPONSE.fields_by_name['state']._options = None
    _CHAINSTATERESPONSE.fields_by_name['state']._serialized_options = b'\xc8\xde\x1f\x00'
    _CHAINSBYASSETRESPONSE.fields_by_name['chains']._options = None
    _CHAINSBYASSETRESPONSE.fields_by_name['chains']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _TRANSFERRATELIMIT.fields_by_name['limit']._options = None
    _TRANSFERRATELIMIT.fields_by_name['limit']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _TRANSFERRATELIMIT.fields_by_name['window']._options = None
    _TRANSFERRATELIMIT.fields_by_name['window']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _TRANSFERRATELIMIT.fields_by_name['incoming']._options = None
    _TRANSFERRATELIMIT.fields_by_name['incoming']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _TRANSFERRATELIMIT.fields_by_name['outgoing']._options = None
    _TRANSFERRATELIMIT.fields_by_name['outgoing']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _TRANSFERRATELIMIT.fields_by_name['time_left']._options = None
    _TRANSFERRATELIMIT.fields_by_name['time_left']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _MESSAGEREQUEST.fields_by_name['id']._options = None
    _MESSAGEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MESSAGERESPONSE.fields_by_name['message']._options = None
    _MESSAGERESPONSE.fields_by_name['message']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_CHAINSTATUS']._serialized_start = 2436
    _globals['_CHAINSTATUS']._serialized_end = 2592
    _globals['_CHAINMAINTAINERSREQUEST']._serialized_start = 265
    _globals['_CHAINMAINTAINERSREQUEST']._serialized_end = 305
    _globals['_CHAINMAINTAINERSRESPONSE']._serialized_start = 307
    _globals['_CHAINMAINTAINERSRESPONSE']._serialized_end = 405
    _globals['_LATESTDEPOSITADDRESSREQUEST']._serialized_start = 407
    _globals['_LATESTDEPOSITADDRESSREQUEST']._serialized_end = 508
    _globals['_LATESTDEPOSITADDRESSRESPONSE']._serialized_start = 510
    _globals['_LATESTDEPOSITADDRESSRESPONSE']._serialized_end = 562
    _globals['_TRANSFERSFORCHAINREQUEST']._serialized_start = 565
    _globals['_TRANSFERSFORCHAINREQUEST']._serialized_end = 727
    _globals['_TRANSFERSFORCHAINRESPONSE']._serialized_start = 730
    _globals['_TRANSFERSFORCHAINRESPONSE']._serialized_end = 894
    _globals['_FEEINFOREQUEST']._serialized_start = 896
    _globals['_FEEINFOREQUEST']._serialized_end = 942
    _globals['_FEEINFORESPONSE']._serialized_start = 944
    _globals['_FEEINFORESPONSE']._serialized_end = 1019
    _globals['_TRANSFERFEEREQUEST']._serialized_start = 1021
    _globals['_TRANSFERFEEREQUEST']._serialized_end = 1106
    _globals['_TRANSFERFEERESPONSE']._serialized_start = 1108
    _globals['_TRANSFERFEERESPONSE']._serialized_end = 1175
    _globals['_CHAINSREQUEST']._serialized_start = 1177
    _globals['_CHAINSREQUEST']._serialized_end = 1243
    _globals['_CHAINSRESPONSE']._serialized_start = 1245
    _globals['_CHAINSRESPONSE']._serialized_end = 1346
    _globals['_ASSETSREQUEST']._serialized_start = 1348
    _globals['_ASSETSREQUEST']._serialized_end = 1378
    _globals['_ASSETSRESPONSE']._serialized_start = 1380
    _globals['_ASSETSRESPONSE']._serialized_end = 1412
    _globals['_CHAINSTATEREQUEST']._serialized_start = 1414
    _globals['_CHAINSTATEREQUEST']._serialized_end = 1448
    _globals['_CHAINSTATERESPONSE']._serialized_start = 1450
    _globals['_CHAINSTATERESPONSE']._serialized_end = 1525
    _globals['_CHAINSBYASSETREQUEST']._serialized_start = 1527
    _globals['_CHAINSBYASSETREQUEST']._serialized_end = 1564
    _globals['_CHAINSBYASSETRESPONSE']._serialized_start = 1566
    _globals['_CHAINSBYASSETRESPONSE']._serialized_end = 1674
    _globals['_RECIPIENTADDRESSREQUEST']._serialized_start = 1676
    _globals['_RECIPIENTADDRESSREQUEST']._serialized_end = 1746
    _globals['_RECIPIENTADDRESSRESPONSE']._serialized_start = 1748
    _globals['_RECIPIENTADDRESSRESPONSE']._serialized_end = 1823
    _globals['_TRANSFERRATELIMITREQUEST']._serialized_start = 1825
    _globals['_TRANSFERRATELIMITREQUEST']._serialized_end = 1881
    _globals['_TRANSFERRATELIMITRESPONSE']._serialized_start = 1883
    _globals['_TRANSFERRATELIMITRESPONSE']._serialized_end = 1980
    _globals['_TRANSFERRATELIMIT']._serialized_start = 1983
    _globals['_TRANSFERRATELIMIT']._serialized_end = 2306
    _globals['_MESSAGEREQUEST']._serialized_start = 2308
    _globals['_MESSAGEREQUEST']._serialized_end = 2344
    _globals['_MESSAGERESPONSE']._serialized_start = 2346
    _globals['_MESSAGERESPONSE']._serialized_end = 2433