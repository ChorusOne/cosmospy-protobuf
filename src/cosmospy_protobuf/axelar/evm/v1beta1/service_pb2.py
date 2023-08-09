"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.evm.v1beta1 import tx_pb2 as axelar_dot_evm_dot_v1beta1_dot_tx__pb2
from ....axelar.evm.v1beta1 import query_pb2 as axelar_dot_evm_dot_v1beta1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/evm/v1beta1/service.proto\x12\x12axelar.evm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1baxelar/evm/v1beta1/tx.proto\x1a\x1eaxelar/evm/v1beta1/query.proto2\x9d\x0f\n\nMsgService\x12\x7f\n\nSetGateway\x12%.axelar.evm.v1beta1.SetGatewayRequest\x1a&.axelar.evm.v1beta1.SetGatewayResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/axelar/evm/set_gateway:\x01*\x12\x98\x01\n\x10ConfirmGatewayTx\x12+.axelar.evm.v1beta1.ConfirmGatewayTxRequest\x1a,.axelar.evm.v1beta1.ConfirmGatewayTxResponse")\x82\xd3\xe4\x93\x02#"\x1e/axelar/evm/confirm_gateway_tx:\x01*\x12f\n\x04Link\x12\x1f.axelar.evm.v1beta1.LinkRequest\x1a .axelar.evm.v1beta1.LinkResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/axelar/evm/link:\x01*\x12\x87\x01\n\x0cConfirmToken\x12\'.axelar.evm.v1beta1.ConfirmTokenRequest\x1a(.axelar.evm.v1beta1.ConfirmTokenResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/axelar/evm/confirm_token:\x01*\x12\x8f\x01\n\x0eConfirmDeposit\x12).axelar.evm.v1beta1.ConfirmDepositRequest\x1a*.axelar.evm.v1beta1.ConfirmDepositResponse"&\x82\xd3\xe4\x93\x02 "\x1b/axelar/evm/confirm_deposit:\x01*\x12\xa0\x01\n\x12ConfirmTransferKey\x12-.axelar.evm.v1beta1.ConfirmTransferKeyRequest\x1a..axelar.evm.v1beta1.ConfirmTransferKeyResponse"+\x82\xd3\xe4\x93\x02%" /axelar/evm/confirm_transfer_key:\x01*\x12\x9c\x01\n\x11CreateDeployToken\x12,.axelar.evm.v1beta1.CreateDeployTokenRequest\x1a-.axelar.evm.v1beta1.CreateDeployTokenResponse"*\x82\xd3\xe4\x93\x02$"\x1f/axelar/evm/create_deploy_token:\x01*\x12\x98\x01\n\x10CreateBurnTokens\x12+.axelar.evm.v1beta1.CreateBurnTokensRequest\x1a,.axelar.evm.v1beta1.CreateBurnTokensResponse")\x82\xd3\xe4\x93\x02#"\x1e/axelar/evm/create_burn_tokens:\x01*\x12\xb0\x01\n\x16CreatePendingTransfers\x121.axelar.evm.v1beta1.CreatePendingTransfersRequest\x1a2.axelar.evm.v1beta1.CreatePendingTransfersResponse"/\x82\xd3\xe4\x93\x02)"$/axelar/evm/create_pending_transfers:\x01*\x12\xc0\x01\n\x1aCreateTransferOperatorship\x125.axelar.evm.v1beta1.CreateTransferOperatorshipRequest\x1a6.axelar.evm.v1beta1.CreateTransferOperatorshipResponse"3\x82\xd3\xe4\x93\x02-"(/axelar/evm/create_transfer_operatorship:\x01*\x12\x87\x01\n\x0cSignCommands\x12\'.axelar.evm.v1beta1.SignCommandsRequest\x1a(.axelar.evm.v1beta1.SignCommandsResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/axelar/evm/sign_commands:\x01*\x12w\n\x08AddChain\x12#.axelar.evm.v1beta1.AddChainRequest\x1a$.axelar.evm.v1beta1.AddChainResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/axelar/evm/add_chain:\x01*\x12\x98\x01\n\x10RetryFailedEvent\x12+.axelar.evm.v1beta1.RetryFailedEventRequest\x1a,.axelar.evm.v1beta1.RetryFailedEventResponse")\x82\xd3\xe4\x93\x02#"\x1e/axelar/evm/retry-failed-event:\x01*2\xf9\x0e\n\x0cQueryService\x12\xa5\x01\n\x0fBatchedCommands\x12*.axelar.evm.v1beta1.BatchedCommandsRequest\x1a+.axelar.evm.v1beta1.BatchedCommandsResponse"9\x82\xd3\xe4\x93\x023\x121/axelar/evm/v1beta1/batched_commands/{chain}/{id}\x12\x84\x01\n\nBurnerInfo\x12%.axelar.evm.v1beta1.BurnerInfoRequest\x1a&.axelar.evm.v1beta1.BurnerInfoResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/axelar/evm/v1beta1/burner_info\x12\xac\x01\n\x12ConfirmationHeight\x12-.axelar.evm.v1beta1.ConfirmationHeightRequest\x1a..axelar.evm.v1beta1.ConfirmationHeightResponse"7\x82\xd3\xe4\x93\x021\x12//axelar/evm/v1beta1/confirmation_height/{chain}\x12\x8f\x01\n\x0cDepositState\x12\'.axelar.evm.v1beta1.DepositStateRequest\x1a(.axelar.evm.v1beta1.DepositStateResponse",\x88\x02\x01\x82\xd3\xe4\x93\x02#\x12!/axelar/evm/v1beta1/deposit_state\x12\xa0\x01\n\x0fPendingCommands\x12*.axelar.evm.v1beta1.PendingCommandsRequest\x1a+.axelar.evm.v1beta1.PendingCommandsResponse"4\x82\xd3\xe4\x93\x02.\x12,/axelar/evm/v1beta1/pending_commands/{chain}\x12s\n\x06Chains\x12!.axelar.evm.v1beta1.ChainsRequest\x1a".axelar.evm.v1beta1.ChainsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/axelar/evm/v1beta1/chains\x12\x7f\n\x07Command\x12".axelar.evm.v1beta1.CommandRequest\x1a#.axelar.evm.v1beta1.CommandResponse"+\x82\xd3\xe4\x93\x02%\x12#/axelar/evm/v1beta1/command_request\x12\x8c\x01\n\nKeyAddress\x12%.axelar.evm.v1beta1.KeyAddressRequest\x1a&.axelar.evm.v1beta1.KeyAddressResponse"/\x82\xd3\xe4\x93\x02)\x12\'/axelar/evm/v1beta1/key_address/{chain}\x12\x9c\x01\n\x0eGatewayAddress\x12).axelar.evm.v1beta1.GatewayAddressRequest\x1a*.axelar.evm.v1beta1.GatewayAddressResponse"3\x82\xd3\xe4\x93\x02-\x12+/axelar/evm/v1beta1/gateway_address/{chain}\x12\x8e\x01\n\x08Bytecode\x12#.axelar.evm.v1beta1.BytecodeRequest\x1a$.axelar.evm.v1beta1.BytecodeResponse"7\x82\xd3\xe4\x93\x021\x12//axelar/evm/v1beta1/bytecode/{chain}/{contract}\x12\x82\x01\n\x05Event\x12 .axelar.evm.v1beta1.EventRequest\x1a!.axelar.evm.v1beta1.EventResponse"4\x82\xd3\xe4\x93\x02.\x12,/axelar/evm/v1beta1/event/{chain}/{event_id}\x12\x90\x01\n\x0bERC20Tokens\x12&.axelar.evm.v1beta1.ERC20TokensRequest\x1a\'.axelar.evm.v1beta1.ERC20TokensResponse"0\x82\xd3\xe4\x93\x02*\x12(/axelar/evm/v1beta1/erc20_tokens/{chain}\x12\x88\x01\n\tTokenInfo\x12$.axelar.evm.v1beta1.TokenInfoRequest\x1a%.axelar.evm.v1beta1.TokenInfoResponse".\x82\xd3\xe4\x93\x02(\x12&/axelar/evm/v1beta1/token_info/{chain}B6Z0github.com/axelarnetwork/axelar-core/x/evm/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.evm.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/evm/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['SetGateway']._options = None
    _MSGSERVICE.methods_by_name['SetGateway']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/axelar/evm/set_gateway:\x01*'
    _MSGSERVICE.methods_by_name['ConfirmGatewayTx']._options = None
    _MSGSERVICE.methods_by_name['ConfirmGatewayTx']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/axelar/evm/confirm_gateway_tx:\x01*'
    _MSGSERVICE.methods_by_name['Link']._options = None
    _MSGSERVICE.methods_by_name['Link']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/axelar/evm/link:\x01*'
    _MSGSERVICE.methods_by_name['ConfirmToken']._options = None
    _MSGSERVICE.methods_by_name['ConfirmToken']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/axelar/evm/confirm_token:\x01*'
    _MSGSERVICE.methods_by_name['ConfirmDeposit']._options = None
    _MSGSERVICE.methods_by_name['ConfirmDeposit']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/axelar/evm/confirm_deposit:\x01*'
    _MSGSERVICE.methods_by_name['ConfirmTransferKey']._options = None
    _MSGSERVICE.methods_by_name['ConfirmTransferKey']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /axelar/evm/confirm_transfer_key:\x01*'
    _MSGSERVICE.methods_by_name['CreateDeployToken']._options = None
    _MSGSERVICE.methods_by_name['CreateDeployToken']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/axelar/evm/create_deploy_token:\x01*'
    _MSGSERVICE.methods_by_name['CreateBurnTokens']._options = None
    _MSGSERVICE.methods_by_name['CreateBurnTokens']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/axelar/evm/create_burn_tokens:\x01*'
    _MSGSERVICE.methods_by_name['CreatePendingTransfers']._options = None
    _MSGSERVICE.methods_by_name['CreatePendingTransfers']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/axelar/evm/create_pending_transfers:\x01*'
    _MSGSERVICE.methods_by_name['CreateTransferOperatorship']._options = None
    _MSGSERVICE.methods_by_name['CreateTransferOperatorship']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/axelar/evm/create_transfer_operatorship:\x01*'
    _MSGSERVICE.methods_by_name['SignCommands']._options = None
    _MSGSERVICE.methods_by_name['SignCommands']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/axelar/evm/sign_commands:\x01*'
    _MSGSERVICE.methods_by_name['AddChain']._options = None
    _MSGSERVICE.methods_by_name['AddChain']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/axelar/evm/add_chain:\x01*'
    _MSGSERVICE.methods_by_name['RetryFailedEvent']._options = None
    _MSGSERVICE.methods_by_name['RetryFailedEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/axelar/evm/retry-failed-event:\x01*'
    _QUERYSERVICE.methods_by_name['BatchedCommands']._options = None
    _QUERYSERVICE.methods_by_name['BatchedCommands']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/axelar/evm/v1beta1/batched_commands/{chain}/{id}'
    _QUERYSERVICE.methods_by_name['BurnerInfo']._options = None
    _QUERYSERVICE.methods_by_name['BurnerInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/axelar/evm/v1beta1/burner_info'
    _QUERYSERVICE.methods_by_name['ConfirmationHeight']._options = None
    _QUERYSERVICE.methods_by_name['ConfirmationHeight']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//axelar/evm/v1beta1/confirmation_height/{chain}'
    _QUERYSERVICE.methods_by_name['DepositState']._options = None
    _QUERYSERVICE.methods_by_name['DepositState']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02#\x12!/axelar/evm/v1beta1/deposit_state'
    _QUERYSERVICE.methods_by_name['PendingCommands']._options = None
    _QUERYSERVICE.methods_by_name['PendingCommands']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/axelar/evm/v1beta1/pending_commands/{chain}'
    _QUERYSERVICE.methods_by_name['Chains']._options = None
    _QUERYSERVICE.methods_by_name['Chains']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/axelar/evm/v1beta1/chains'
    _QUERYSERVICE.methods_by_name['Command']._options = None
    _QUERYSERVICE.methods_by_name['Command']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/axelar/evm/v1beta1/command_request'
    _QUERYSERVICE.methods_by_name['KeyAddress']._options = None
    _QUERYSERVICE.methods_by_name['KeyAddress']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/axelar/evm/v1beta1/key_address/{chain}"
    _QUERYSERVICE.methods_by_name['GatewayAddress']._options = None
    _QUERYSERVICE.methods_by_name['GatewayAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/axelar/evm/v1beta1/gateway_address/{chain}'
    _QUERYSERVICE.methods_by_name['Bytecode']._options = None
    _QUERYSERVICE.methods_by_name['Bytecode']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//axelar/evm/v1beta1/bytecode/{chain}/{contract}'
    _QUERYSERVICE.methods_by_name['Event']._options = None
    _QUERYSERVICE.methods_by_name['Event']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/axelar/evm/v1beta1/event/{chain}/{event_id}'
    _QUERYSERVICE.methods_by_name['ERC20Tokens']._options = None
    _QUERYSERVICE.methods_by_name['ERC20Tokens']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/axelar/evm/v1beta1/erc20_tokens/{chain}'
    _QUERYSERVICE.methods_by_name['TokenInfo']._options = None
    _QUERYSERVICE.methods_by_name['TokenInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/axelar/evm/v1beta1/token_info/{chain}'
    _globals['_MSGSERVICE']._serialized_start = 170
    _globals['_MSGSERVICE']._serialized_end = 2119
    _globals['_QUERYSERVICE']._serialized_start = 2122
    _globals['_QUERYSERVICE']._serialized_end = 4035