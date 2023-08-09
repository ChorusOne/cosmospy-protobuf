"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.nexus.v1beta1 import tx_pb2 as axelar_dot_nexus_dot_v1beta1_dot_tx__pb2
from ....axelar.nexus.v1beta1 import query_pb2 as axelar_dot_nexus_dot_v1beta1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"axelar/nexus/v1beta1/service.proto\x12\x14axelar.nexus.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1daxelar/nexus/v1beta1/tx.proto\x1a axelar/nexus/v1beta1/query.proto2\x91\x08\n\nMsgService\x12\xba\x01\n\x17RegisterChainMaintainer\x124.axelar.nexus.v1beta1.RegisterChainMaintainerRequest\x1a5.axelar.nexus.v1beta1.RegisterChainMaintainerResponse"2\x82\xd3\xe4\x93\x02,"\'/axelar/nexus/register_chain_maintainer:\x01*\x12\xc2\x01\n\x19DeregisterChainMaintainer\x126.axelar.nexus.v1beta1.DeregisterChainMaintainerRequest\x1a7.axelar.nexus.v1beta1.DeregisterChainMaintainerResponse"4\x82\xd3\xe4\x93\x02.")/axelar/nexus/deregister_chain_maintainer:\x01*\x12\x91\x01\n\rActivateChain\x12*.axelar.nexus.v1beta1.ActivateChainRequest\x1a+.axelar.nexus.v1beta1.ActivateChainResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/axelar/nexus/activate_chain:\x01*\x12\x99\x01\n\x0fDeactivateChain\x12,.axelar.nexus.v1beta1.DeactivateChainRequest\x1a-.axelar.nexus.v1beta1.DeactivateChainResponse")\x82\xd3\xe4\x93\x02#"\x1e/axelar/nexus/deactivate_chain:\x01*\x12\x9e\x01\n\x10RegisterAssetFee\x12-.axelar.nexus.v1beta1.RegisterAssetFeeRequest\x1a..axelar.nexus.v1beta1.RegisterAssetFeeResponse"+\x82\xd3\xe4\x93\x02%" /axelar/nexus/register_asset_fee:\x01*\x12\xaf\x01\n\x14SetTransferRateLimit\x121.axelar.nexus.v1beta1.SetTransferRateLimitRequest\x1a2.axelar.nexus.v1beta1.SetTransferRateLimitResponse"0\x82\xd3\xe4\x93\x02*"%/axelar/nexus/set_transfer_rate_limit:\x01*2\xa2\x10\n\x0cQueryService\x12\xe6\x01\n\x14LatestDepositAddress\x121.axelar.nexus.v1beta1.LatestDepositAddressRequest\x1a2.axelar.nexus.v1beta1.LatestDepositAddressResponse"g\x82\xd3\xe4\x93\x02a\x12_/axelar/nexus/v1beta1/latest_deposit_address/{recipient_addr}/{recipient_chain}/{deposit_chain}\x12\xb7\x01\n\x11TransfersForChain\x12..axelar.nexus.v1beta1.TransfersForChainRequest\x1a/.axelar.nexus.v1beta1.TransfersForChainResponse"A\x82\xd3\xe4\x93\x02;\x129/axelar/nexus/v1beta1/transfers_for_chain/{chain}/{state}\x12\xab\x01\n\x07FeeInfo\x12$.axelar.nexus.v1beta1.FeeInfoRequest\x1a%.axelar.nexus.v1beta1.FeeInfoResponse"S\x82\xd3\xe4\x93\x02M\x12./axelar/nexus/v1beta1/fee_info/{chain}/{asset}Z\x1b\x12\x19/axelar/nexus/v1beta1/fee\x12\xe0\x01\n\x0bTransferFee\x12(.axelar.nexus.v1beta1.TransferFeeRequest\x1a).axelar.nexus.v1beta1.TransferFeeResponse"|\x82\xd3\xe4\x93\x02v\x12N/axelar/nexus/v1beta1/transfer_fee/{source_chain}/{destination_chain}/{amount}Z$\x12"/axelar/nexus/v1beta1/transfer_fee\x12y\n\x06Chains\x12#.axelar.nexus.v1beta1.ChainsRequest\x1a$.axelar.nexus.v1beta1.ChainsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/axelar/nexus/v1beta1/chains\x12\x81\x01\n\x06Assets\x12#.axelar.nexus.v1beta1.AssetsRequest\x1a$.axelar.nexus.v1beta1.AssetsResponse",\x82\xd3\xe4\x93\x02&\x12$/axelar/nexus/v1beta1/assets/{chain}\x12\x92\x01\n\nChainState\x12\'.axelar.nexus.v1beta1.ChainStateRequest\x1a(.axelar.nexus.v1beta1.ChainStateResponse"1\x82\xd3\xe4\x93\x02+\x12)/axelar/nexus/v1beta1/chain_state/{chain}\x12\x9f\x01\n\rChainsByAsset\x12*.axelar.nexus.v1beta1.ChainsByAssetRequest\x1a+.axelar.nexus.v1beta1.ChainsByAssetResponse"5\x82\xd3\xe4\x93\x02/\x12-/axelar/nexus/v1beta1/chains_by_asset/{asset}\x12\xc1\x01\n\x10RecipientAddress\x12-.axelar.nexus.v1beta1.RecipientAddressRequest\x1a..axelar.nexus.v1beta1.RecipientAddressResponse"N\x82\xd3\xe4\x93\x02H\x12F/axelar/nexus/v1beta1/recipient_address/{deposit_chain}/{deposit_addr}\x12\xaa\x01\n\x10ChainMaintainers\x12-.axelar.nexus.v1beta1.ChainMaintainersRequest\x1a..axelar.nexus.v1beta1.ChainMaintainersResponse"7\x82\xd3\xe4\x93\x021\x12//axelar/nexus/v1beta1/chain_maintainers/{chain}\x12\xb7\x01\n\x11TransferRateLimit\x12..axelar.nexus.v1beta1.TransferRateLimitRequest\x1a/.axelar.nexus.v1beta1.TransferRateLimitResponse"A\x82\xd3\xe4\x93\x02;\x129/axelar/nexus/v1beta1/transfer_rate_limit/{chain}/{asset}\x12}\n\x07Message\x12$.axelar.nexus.v1beta1.MessageRequest\x1a%.axelar.nexus.v1beta1.MessageResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/axelar/nexus/v1beta1/messageB8Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['RegisterChainMaintainer']._options = None
    _MSGSERVICE.methods_by_name['RegisterChainMaintainer']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/axelar/nexus/register_chain_maintainer:\x01*'
    _MSGSERVICE.methods_by_name['DeregisterChainMaintainer']._options = None
    _MSGSERVICE.methods_by_name['DeregisterChainMaintainer']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/axelar/nexus/deregister_chain_maintainer:\x01*'
    _MSGSERVICE.methods_by_name['ActivateChain']._options = None
    _MSGSERVICE.methods_by_name['ActivateChain']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/axelar/nexus/activate_chain:\x01*'
    _MSGSERVICE.methods_by_name['DeactivateChain']._options = None
    _MSGSERVICE.methods_by_name['DeactivateChain']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/axelar/nexus/deactivate_chain:\x01*'
    _MSGSERVICE.methods_by_name['RegisterAssetFee']._options = None
    _MSGSERVICE.methods_by_name['RegisterAssetFee']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /axelar/nexus/register_asset_fee:\x01*'
    _MSGSERVICE.methods_by_name['SetTransferRateLimit']._options = None
    _MSGSERVICE.methods_by_name['SetTransferRateLimit']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/axelar/nexus/set_transfer_rate_limit:\x01*'
    _QUERYSERVICE.methods_by_name['LatestDepositAddress']._options = None
    _QUERYSERVICE.methods_by_name['LatestDepositAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02a\x12_/axelar/nexus/v1beta1/latest_deposit_address/{recipient_addr}/{recipient_chain}/{deposit_chain}'
    _QUERYSERVICE.methods_by_name['TransfersForChain']._options = None
    _QUERYSERVICE.methods_by_name['TransfersForChain']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/axelar/nexus/v1beta1/transfers_for_chain/{chain}/{state}'
    _QUERYSERVICE.methods_by_name['FeeInfo']._options = None
    _QUERYSERVICE.methods_by_name['FeeInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02M\x12./axelar/nexus/v1beta1/fee_info/{chain}/{asset}Z\x1b\x12\x19/axelar/nexus/v1beta1/fee'
    _QUERYSERVICE.methods_by_name['TransferFee']._options = None
    _QUERYSERVICE.methods_by_name['TransferFee']._serialized_options = b'\x82\xd3\xe4\x93\x02v\x12N/axelar/nexus/v1beta1/transfer_fee/{source_chain}/{destination_chain}/{amount}Z$\x12"/axelar/nexus/v1beta1/transfer_fee'
    _QUERYSERVICE.methods_by_name['Chains']._options = None
    _QUERYSERVICE.methods_by_name['Chains']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/axelar/nexus/v1beta1/chains'
    _QUERYSERVICE.methods_by_name['Assets']._options = None
    _QUERYSERVICE.methods_by_name['Assets']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/axelar/nexus/v1beta1/assets/{chain}'
    _QUERYSERVICE.methods_by_name['ChainState']._options = None
    _QUERYSERVICE.methods_by_name['ChainState']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/axelar/nexus/v1beta1/chain_state/{chain}'
    _QUERYSERVICE.methods_by_name['ChainsByAsset']._options = None
    _QUERYSERVICE.methods_by_name['ChainsByAsset']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/axelar/nexus/v1beta1/chains_by_asset/{asset}'
    _QUERYSERVICE.methods_by_name['RecipientAddress']._options = None
    _QUERYSERVICE.methods_by_name['RecipientAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/axelar/nexus/v1beta1/recipient_address/{deposit_chain}/{deposit_addr}'
    _QUERYSERVICE.methods_by_name['ChainMaintainers']._options = None
    _QUERYSERVICE.methods_by_name['ChainMaintainers']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//axelar/nexus/v1beta1/chain_maintainers/{chain}'
    _QUERYSERVICE.methods_by_name['TransferRateLimit']._options = None
    _QUERYSERVICE.methods_by_name['TransferRateLimit']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/axelar/nexus/v1beta1/transfer_rate_limit/{chain}/{asset}'
    _QUERYSERVICE.methods_by_name['Message']._options = None
    _QUERYSERVICE.methods_by_name['Message']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/axelar/nexus/v1beta1/message'
    _globals['_MSGSERVICE']._serialized_start = 178
    _globals['_MSGSERVICE']._serialized_end = 1219
    _globals['_QUERYSERVICE']._serialized_start = 1222
    _globals['_QUERYSERVICE']._serialized_end = 3304