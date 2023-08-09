"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.axelarnet.v1beta1 import tx_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2
from ....axelar.axelarnet.v1beta1 import query_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&axelar/axelarnet/v1beta1/service.proto\x12\x18axelar.axelarnet.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a!axelar/axelarnet/v1beta1/tx.proto\x1a$axelar/axelarnet/v1beta1/query.proto2\xa0\r\n\nMsgService\x12x\n\x04Link\x12%.axelar.axelarnet.v1beta1.LinkRequest\x1a&.axelar.axelarnet.v1beta1.LinkResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/axelar/axelarnet/link:\x01*\x12\xa1\x01\n\x0eConfirmDeposit\x12/.axelar.axelarnet.v1beta1.ConfirmDepositRequest\x1a0.axelar.axelarnet.v1beta1.ConfirmDepositResponse",\x82\xd3\xe4\x93\x02&"!/axelar/axelarnet/confirm_deposit:\x01*\x12\xc6\x01\n\x17ExecutePendingTransfers\x128.axelar.axelarnet.v1beta1.ExecutePendingTransfersRequest\x1a9.axelar.axelarnet.v1beta1.ExecutePendingTransfersResponse"6\x82\xd3\xe4\x93\x020"+/axelar/axelarnet/execute_pending_transfers:\x01*\x12\xb7\x01\n\x13AddCosmosBasedChain\x124.axelar.axelarnet.v1beta1.AddCosmosBasedChainRequest\x1a5.axelar.axelarnet.v1beta1.AddCosmosBasedChainResponse"3\x82\xd3\xe4\x93\x02-"(/axelar/axelarnet/add_cosmos_based_chain:\x01*\x12\x9d\x01\n\rRegisterAsset\x12..axelar.axelarnet.v1beta1.RegisterAssetRequest\x1a/.axelar.axelarnet.v1beta1.RegisterAssetResponse"+\x82\xd3\xe4\x93\x02%" /axelar/axelarnet/register_asset:\x01*\x12\xae\x01\n\x11RouteIBCTransfers\x122.axelar.axelarnet.v1beta1.RouteIBCTransfersRequest\x1a3.axelar.axelarnet.v1beta1.RouteIBCTransfersResponse"0\x82\xd3\xe4\x93\x02*"%/axelar/axelarnet/route_ibc_transfers:\x01*\x12\xba\x01\n\x14RegisterFeeCollector\x125.axelar.axelarnet.v1beta1.RegisterFeeCollectorRequest\x1a6.axelar.axelarnet.v1beta1.RegisterFeeCollectorResponse"3\x82\xd3\xe4\x93\x02-"(/axelar/axelarnet/register_fee_collector:\x01*\x12\xaa\x01\n\x10RetryIBCTransfer\x121.axelar.axelarnet.v1beta1.RetryIBCTransferRequest\x1a2.axelar.axelarnet.v1beta1.RetryIBCTransferResponse"/\x82\xd3\xe4\x93\x02)"$/axelar/axelarnet/retry_ibc_transfer:\x01*\x12\x99\x01\n\x0cRouteMessage\x12-.axelar.axelarnet.v1beta1.RouteMessageRequest\x1a..axelar.axelarnet.v1beta1.RouteMessageResponse"*\x82\xd3\xe4\x93\x02$"\x1f/axelar/axelarnet/route_message:\x01*\x12\x99\x01\n\x0cCallContract\x12-.axelar.axelarnet.v1beta1.CallContractRequest\x1a..axelar.axelarnet.v1beta1.CallContractResponse"*\x82\xd3\xe4\x93\x02$"\x1f/axelar/axelarnet/call_contract:\x01*2\xd5\x01\n\x0cQueryService\x12\xc4\x01\n\x17PendingIBCTransferCount\x128.axelar.axelarnet.v1beta1.PendingIBCTransferCountRequest\x1a9.axelar.axelarnet.v1beta1.PendingIBCTransferCountResponse"4\x82\xd3\xe4\x93\x02.\x12,/axelar/axelarnet/v1beta1/ibc_transfer_countB<Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.axelarnet.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['Link']._options = None
    _MSGSERVICE.methods_by_name['Link']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/axelar/axelarnet/link:\x01*'
    _MSGSERVICE.methods_by_name['ConfirmDeposit']._options = None
    _MSGSERVICE.methods_by_name['ConfirmDeposit']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/axelar/axelarnet/confirm_deposit:\x01*'
    _MSGSERVICE.methods_by_name['ExecutePendingTransfers']._options = None
    _MSGSERVICE.methods_by_name['ExecutePendingTransfers']._serialized_options = b'\x82\xd3\xe4\x93\x020"+/axelar/axelarnet/execute_pending_transfers:\x01*'
    _MSGSERVICE.methods_by_name['AddCosmosBasedChain']._options = None
    _MSGSERVICE.methods_by_name['AddCosmosBasedChain']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/axelar/axelarnet/add_cosmos_based_chain:\x01*'
    _MSGSERVICE.methods_by_name['RegisterAsset']._options = None
    _MSGSERVICE.methods_by_name['RegisterAsset']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /axelar/axelarnet/register_asset:\x01*'
    _MSGSERVICE.methods_by_name['RouteIBCTransfers']._options = None
    _MSGSERVICE.methods_by_name['RouteIBCTransfers']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/axelar/axelarnet/route_ibc_transfers:\x01*'
    _MSGSERVICE.methods_by_name['RegisterFeeCollector']._options = None
    _MSGSERVICE.methods_by_name['RegisterFeeCollector']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/axelar/axelarnet/register_fee_collector:\x01*'
    _MSGSERVICE.methods_by_name['RetryIBCTransfer']._options = None
    _MSGSERVICE.methods_by_name['RetryIBCTransfer']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/axelar/axelarnet/retry_ibc_transfer:\x01*'
    _MSGSERVICE.methods_by_name['RouteMessage']._options = None
    _MSGSERVICE.methods_by_name['RouteMessage']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/axelar/axelarnet/route_message:\x01*'
    _MSGSERVICE.methods_by_name['CallContract']._options = None
    _MSGSERVICE.methods_by_name['CallContract']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/axelar/axelarnet/call_contract:\x01*'
    _QUERYSERVICE.methods_by_name['PendingIBCTransferCount']._options = None
    _QUERYSERVICE.methods_by_name['PendingIBCTransferCount']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/axelar/axelarnet/v1beta1/ibc_transfer_count'
    _globals['_MSGSERVICE']._serialized_start = 194
    _globals['_MSGSERVICE']._serialized_end = 1890
    _globals['_QUERYSERVICE']._serialized_start = 1893
    _globals['_QUERYSERVICE']._serialized_end = 2106