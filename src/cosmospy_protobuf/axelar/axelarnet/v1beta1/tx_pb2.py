"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....axelar.nexus.exported.v1beta1 import types_pb2 as axelar_dot_nexus_dot_exported_dot_v1beta1_dot_types__pb2
from ....axelar.axelarnet.v1beta1 import types_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_types__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/axelarnet/v1beta1/tx.proto\x12\x18axelar.axelarnet.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto\x1a)axelar/nexus/exported/v1beta1/types.proto\x1a$axelar/axelarnet/v1beta1/types.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\xdb\x01\n\x0bLinkRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x16\n\x0erecipient_addr\x18\x02 \x01(\t\x12\\\n\x0frecipient_chain\x18\x03 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\r\n\x05asset\x18\x04 \x01(\t:\x04\x80\xb5\x18\x01"$\n\x0cLinkResponse\x12\x14\n\x0cdeposit_addr\x18\x01 \x01(\t"\xc7\x01\n\x15ConfirmDepositRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12J\n\x0fdeposit_address\x18\x04 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\r\n\x05denom\x18\x05 \x01(\t:\x04\x80\xb5\x18\x01J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04"\x18\n\x16ConfirmDepositResponse"i\n\x1eExecutePendingTransfersRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x01"!\n\x1fExecutePendingTransfersResponse"\xc5\x01\n\x16RegisterIBCPathRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x0c\n\x04path\x18\x03 \x01(\t:\x06\x18\x01\x80\xb5\x18\x02"\x19\n\x17RegisterIBCPathResponse"\xfc\x02\n\x1aAddCosmosBasedChainRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12;\n\x05chain\x18\x02 \x01(\x0b2$.axelar.nexus.exported.v1beta1.ChainB\x06\x18\x01\xc8\xde\x1f\x00\x12\x13\n\x0baddr_prefix\x18\x03 \x01(\t\x12C\n\rnative_assets\x18\x05 \x03(\x0b2$.axelar.nexus.exported.v1beta1.AssetB\x06\x18\x01\xc8\xde\x1f\x00\x12Y\n\x0ccosmos_chain\x18\x06 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x1d\n\x08ibc_path\x18\x07 \x01(\tB\x0b\xe2\xde\x1f\x07IBCPath:\x04\x80\xb5\x18\x03J\x04\x08\x04\x10\x05"\x1d\n\x1bAddCosmosBasedChainResponse"\xe3\x02\n\x14RegisterAssetRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x129\n\x05asset\x18\x03 \x01(\x0b2$.axelar.nexus.exported.v1beta1.AssetB\x04\xc8\xde\x1f\x00\x12>\n\x05limit\x18\x04 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x123\n\x06window\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01:\x04\x80\xb5\x18\x02"\x17\n\x15RegisterAssetResponse"c\n\x18RouteIBCTransfersRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x01"\x1b\n\x19RouteIBCTransfersResponse"\xb0\x01\n\x1bRegisterFeeCollectorRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12H\n\rfee_collector\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x03"\x1e\n\x1cRegisterFeeCollectorResponse"\x8e\x02\n\x17RetryIBCTransferRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12V\n\x02id\x18\x03 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID:\x04\x80\xb5\x18\x01"\x1a\n\x18RetryIBCTransferResponse"\x83\x01\n\x13RouteMessageRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x12\n\x02id\x18\x02 \x01(\tB\x06\xe2\xde\x1f\x02ID\x12\x0f\n\x07payload\x18\x03 \x01(\x0c:\x04\x80\xb5\x18\x01"\x16\n\x14RouteMessageResponse"\x89\x02\n\x13CallContractRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x18\n\x10contract_address\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12*\n\x03fee\x18\x05 \x01(\x0b2\x1d.axelar.axelarnet.v1beta1.Fee:\x04\x80\xb5\x18\x01"\x16\n\x14CallContractResponseB<Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.axelarnet.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00'
    _LINKREQUEST.fields_by_name['sender']._options = None
    _LINKREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _LINKREQUEST.fields_by_name['recipient_chain']._options = None
    _LINKREQUEST.fields_by_name['recipient_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _LINKREQUEST._options = None
    _LINKREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _CONFIRMDEPOSITREQUEST.fields_by_name['sender']._options = None
    _CONFIRMDEPOSITREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _CONFIRMDEPOSITREQUEST.fields_by_name['deposit_address']._options = None
    _CONFIRMDEPOSITREQUEST.fields_by_name['deposit_address']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _CONFIRMDEPOSITREQUEST._options = None
    _CONFIRMDEPOSITREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _EXECUTEPENDINGTRANSFERSREQUEST.fields_by_name['sender']._options = None
    _EXECUTEPENDINGTRANSFERSREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _EXECUTEPENDINGTRANSFERSREQUEST._options = None
    _EXECUTEPENDINGTRANSFERSREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _REGISTERIBCPATHREQUEST.fields_by_name['sender']._options = None
    _REGISTERIBCPATHREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERIBCPATHREQUEST.fields_by_name['chain']._options = None
    _REGISTERIBCPATHREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _REGISTERIBCPATHREQUEST._options = None
    _REGISTERIBCPATHREQUEST._serialized_options = b'\x18\x01\x80\xb5\x18\x02'
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['sender']._options = None
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['chain']._options = None
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['chain']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00'
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['native_assets']._options = None
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['native_assets']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00'
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['cosmos_chain']._options = None
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['cosmos_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['ibc_path']._options = None
    _ADDCOSMOSBASEDCHAINREQUEST.fields_by_name['ibc_path']._serialized_options = b'\xe2\xde\x1f\x07IBCPath'
    _ADDCOSMOSBASEDCHAINREQUEST._options = None
    _ADDCOSMOSBASEDCHAINREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _REGISTERASSETREQUEST.fields_by_name['sender']._options = None
    _REGISTERASSETREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERASSETREQUEST.fields_by_name['chain']._options = None
    _REGISTERASSETREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _REGISTERASSETREQUEST.fields_by_name['asset']._options = None
    _REGISTERASSETREQUEST.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _REGISTERASSETREQUEST.fields_by_name['limit']._options = None
    _REGISTERASSETREQUEST.fields_by_name['limit']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _REGISTERASSETREQUEST.fields_by_name['window']._options = None
    _REGISTERASSETREQUEST.fields_by_name['window']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _REGISTERASSETREQUEST._options = None
    _REGISTERASSETREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _ROUTEIBCTRANSFERSREQUEST.fields_by_name['sender']._options = None
    _ROUTEIBCTRANSFERSREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _ROUTEIBCTRANSFERSREQUEST._options = None
    _ROUTEIBCTRANSFERSREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _REGISTERFEECOLLECTORREQUEST.fields_by_name['sender']._options = None
    _REGISTERFEECOLLECTORREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERFEECOLLECTORREQUEST.fields_by_name['fee_collector']._options = None
    _REGISTERFEECOLLECTORREQUEST.fields_by_name['fee_collector']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERFEECOLLECTORREQUEST._options = None
    _REGISTERFEECOLLECTORREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _RETRYIBCTRANSFERREQUEST.fields_by_name['sender']._options = None
    _RETRYIBCTRANSFERREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _RETRYIBCTRANSFERREQUEST.fields_by_name['chain']._options = None
    _RETRYIBCTRANSFERREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _RETRYIBCTRANSFERREQUEST.fields_by_name['id']._options = None
    _RETRYIBCTRANSFERREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _RETRYIBCTRANSFERREQUEST._options = None
    _RETRYIBCTRANSFERREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _ROUTEMESSAGEREQUEST.fields_by_name['sender']._options = None
    _ROUTEMESSAGEREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _ROUTEMESSAGEREQUEST.fields_by_name['id']._options = None
    _ROUTEMESSAGEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _ROUTEMESSAGEREQUEST._options = None
    _ROUTEMESSAGEREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _CALLCONTRACTREQUEST.fields_by_name['sender']._options = None
    _CALLCONTRACTREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _CALLCONTRACTREQUEST.fields_by_name['chain']._options = None
    _CALLCONTRACTREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CALLCONTRACTREQUEST._options = None
    _CALLCONTRACTREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _globals['_LINKREQUEST']._serialized_start = 333
    _globals['_LINKREQUEST']._serialized_end = 552
    _globals['_LINKRESPONSE']._serialized_start = 554
    _globals['_LINKRESPONSE']._serialized_end = 590
    _globals['_CONFIRMDEPOSITREQUEST']._serialized_start = 593
    _globals['_CONFIRMDEPOSITREQUEST']._serialized_end = 792
    _globals['_CONFIRMDEPOSITRESPONSE']._serialized_start = 794
    _globals['_CONFIRMDEPOSITRESPONSE']._serialized_end = 818
    _globals['_EXECUTEPENDINGTRANSFERSREQUEST']._serialized_start = 820
    _globals['_EXECUTEPENDINGTRANSFERSREQUEST']._serialized_end = 925
    _globals['_EXECUTEPENDINGTRANSFERSRESPONSE']._serialized_start = 927
    _globals['_EXECUTEPENDINGTRANSFERSRESPONSE']._serialized_end = 960
    _globals['_REGISTERIBCPATHREQUEST']._serialized_start = 963
    _globals['_REGISTERIBCPATHREQUEST']._serialized_end = 1160
    _globals['_REGISTERIBCPATHRESPONSE']._serialized_start = 1162
    _globals['_REGISTERIBCPATHRESPONSE']._serialized_end = 1187
    _globals['_ADDCOSMOSBASEDCHAINREQUEST']._serialized_start = 1190
    _globals['_ADDCOSMOSBASEDCHAINREQUEST']._serialized_end = 1570
    _globals['_ADDCOSMOSBASEDCHAINRESPONSE']._serialized_start = 1572
    _globals['_ADDCOSMOSBASEDCHAINRESPONSE']._serialized_end = 1601
    _globals['_REGISTERASSETREQUEST']._serialized_start = 1604
    _globals['_REGISTERASSETREQUEST']._serialized_end = 1959
    _globals['_REGISTERASSETRESPONSE']._serialized_start = 1961
    _globals['_REGISTERASSETRESPONSE']._serialized_end = 1984
    _globals['_ROUTEIBCTRANSFERSREQUEST']._serialized_start = 1986
    _globals['_ROUTEIBCTRANSFERSREQUEST']._serialized_end = 2085
    _globals['_ROUTEIBCTRANSFERSRESPONSE']._serialized_start = 2087
    _globals['_ROUTEIBCTRANSFERSRESPONSE']._serialized_end = 2114
    _globals['_REGISTERFEECOLLECTORREQUEST']._serialized_start = 2117
    _globals['_REGISTERFEECOLLECTORREQUEST']._serialized_end = 2293
    _globals['_REGISTERFEECOLLECTORRESPONSE']._serialized_start = 2295
    _globals['_REGISTERFEECOLLECTORRESPONSE']._serialized_end = 2325
    _globals['_RETRYIBCTRANSFERREQUEST']._serialized_start = 2328
    _globals['_RETRYIBCTRANSFERREQUEST']._serialized_end = 2598
    _globals['_RETRYIBCTRANSFERRESPONSE']._serialized_start = 2600
    _globals['_RETRYIBCTRANSFERRESPONSE']._serialized_end = 2626
    _globals['_ROUTEMESSAGEREQUEST']._serialized_start = 2629
    _globals['_ROUTEMESSAGEREQUEST']._serialized_end = 2760
    _globals['_ROUTEMESSAGERESPONSE']._serialized_start = 2762
    _globals['_ROUTEMESSAGERESPONSE']._serialized_end = 2784
    _globals['_CALLCONTRACTREQUEST']._serialized_start = 2787
    _globals['_CALLCONTRACTREQUEST']._serialized_end = 3052
    _globals['_CALLCONTRACTRESPONSE']._serialized_start = 3054
    _globals['_CALLCONTRACTRESPONSE']._serialized_end = 3076