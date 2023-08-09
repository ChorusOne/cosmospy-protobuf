"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.evm.v1beta1 import query_pb2 as axelar_dot_evm_dot_v1beta1_dot_query__pb2
from ....axelar.evm.v1beta1 import tx_pb2 as axelar_dot_evm_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the evm Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetGateway = channel.unary_unary('/axelar.evm.v1beta1.MsgService/SetGateway', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SetGatewayRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SetGatewayResponse.FromString)
        self.ConfirmGatewayTx = channel.unary_unary('/axelar.evm.v1beta1.MsgService/ConfirmGatewayTx', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmGatewayTxRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmGatewayTxResponse.FromString)
        self.Link = channel.unary_unary('/axelar.evm.v1beta1.MsgService/Link', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.LinkRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.LinkResponse.FromString)
        self.ConfirmToken = channel.unary_unary('/axelar.evm.v1beta1.MsgService/ConfirmToken', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTokenRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTokenResponse.FromString)
        self.ConfirmDeposit = channel.unary_unary('/axelar.evm.v1beta1.MsgService/ConfirmDeposit', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmDepositRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmDepositResponse.FromString)
        self.ConfirmTransferKey = channel.unary_unary('/axelar.evm.v1beta1.MsgService/ConfirmTransferKey', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTransferKeyRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTransferKeyResponse.FromString)
        self.CreateDeployToken = channel.unary_unary('/axelar.evm.v1beta1.MsgService/CreateDeployToken', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateDeployTokenRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateDeployTokenResponse.FromString)
        self.CreateBurnTokens = channel.unary_unary('/axelar.evm.v1beta1.MsgService/CreateBurnTokens', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateBurnTokensRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateBurnTokensResponse.FromString)
        self.CreatePendingTransfers = channel.unary_unary('/axelar.evm.v1beta1.MsgService/CreatePendingTransfers', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreatePendingTransfersRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreatePendingTransfersResponse.FromString)
        self.CreateTransferOperatorship = channel.unary_unary('/axelar.evm.v1beta1.MsgService/CreateTransferOperatorship', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateTransferOperatorshipRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateTransferOperatorshipResponse.FromString)
        self.SignCommands = channel.unary_unary('/axelar.evm.v1beta1.MsgService/SignCommands', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SignCommandsRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SignCommandsResponse.FromString)
        self.AddChain = channel.unary_unary('/axelar.evm.v1beta1.MsgService/AddChain', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.AddChainRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.AddChainResponse.FromString)
        self.RetryFailedEvent = channel.unary_unary('/axelar.evm.v1beta1.MsgService/RetryFailedEvent', request_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.RetryFailedEventRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.RetryFailedEventResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the evm Msg service.
    """

    def SetGateway(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmGatewayTx(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Link(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmDeposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmTransferKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDeployToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBurnTokens(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePendingTransfers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTransferOperatorship(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignCommands(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetryFailedEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'SetGateway': grpc.unary_unary_rpc_method_handler(servicer.SetGateway, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SetGatewayRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SetGatewayResponse.SerializeToString), 'ConfirmGatewayTx': grpc.unary_unary_rpc_method_handler(servicer.ConfirmGatewayTx, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmGatewayTxRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmGatewayTxResponse.SerializeToString), 'Link': grpc.unary_unary_rpc_method_handler(servicer.Link, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.LinkRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.LinkResponse.SerializeToString), 'ConfirmToken': grpc.unary_unary_rpc_method_handler(servicer.ConfirmToken, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTokenRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTokenResponse.SerializeToString), 'ConfirmDeposit': grpc.unary_unary_rpc_method_handler(servicer.ConfirmDeposit, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmDepositRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmDepositResponse.SerializeToString), 'ConfirmTransferKey': grpc.unary_unary_rpc_method_handler(servicer.ConfirmTransferKey, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTransferKeyRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTransferKeyResponse.SerializeToString), 'CreateDeployToken': grpc.unary_unary_rpc_method_handler(servicer.CreateDeployToken, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateDeployTokenRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateDeployTokenResponse.SerializeToString), 'CreateBurnTokens': grpc.unary_unary_rpc_method_handler(servicer.CreateBurnTokens, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateBurnTokensRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateBurnTokensResponse.SerializeToString), 'CreatePendingTransfers': grpc.unary_unary_rpc_method_handler(servicer.CreatePendingTransfers, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreatePendingTransfersRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreatePendingTransfersResponse.SerializeToString), 'CreateTransferOperatorship': grpc.unary_unary_rpc_method_handler(servicer.CreateTransferOperatorship, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateTransferOperatorshipRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateTransferOperatorshipResponse.SerializeToString), 'SignCommands': grpc.unary_unary_rpc_method_handler(servicer.SignCommands, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SignCommandsRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SignCommandsResponse.SerializeToString), 'AddChain': grpc.unary_unary_rpc_method_handler(servicer.AddChain, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.AddChainRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.AddChainResponse.SerializeToString), 'RetryFailedEvent': grpc.unary_unary_rpc_method_handler(servicer.RetryFailedEvent, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.RetryFailedEventRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_tx__pb2.RetryFailedEventResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.evm.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the evm Msg service.
    """

    @staticmethod
    def SetGateway(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/SetGateway', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SetGatewayRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SetGatewayResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmGatewayTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/ConfirmGatewayTx', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmGatewayTxRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmGatewayTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Link(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/Link', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.LinkRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.LinkResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmToken(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/ConfirmToken', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTokenRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTokenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmDeposit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/ConfirmDeposit', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmDepositRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmDepositResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmTransferKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/ConfirmTransferKey', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTransferKeyRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.ConfirmTransferKeyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDeployToken(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/CreateDeployToken', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateDeployTokenRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateDeployTokenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBurnTokens(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/CreateBurnTokens', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateBurnTokensRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateBurnTokensResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePendingTransfers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/CreatePendingTransfers', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreatePendingTransfersRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreatePendingTransfersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTransferOperatorship(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/CreateTransferOperatorship', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateTransferOperatorshipRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.CreateTransferOperatorshipResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignCommands(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/SignCommands', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SignCommandsRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.SignCommandsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddChain(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/AddChain', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.AddChainRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.AddChainResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetryFailedEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.MsgService/RetryFailedEvent', axelar_dot_evm_dot_v1beta1_dot_tx__pb2.RetryFailedEventRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_tx__pb2.RetryFailedEventResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryServiceStub(object):
    """QueryService defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BatchedCommands = channel.unary_unary('/axelar.evm.v1beta1.QueryService/BatchedCommands', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BatchedCommandsRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BatchedCommandsResponse.FromString)
        self.BurnerInfo = channel.unary_unary('/axelar.evm.v1beta1.QueryService/BurnerInfo', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BurnerInfoRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BurnerInfoResponse.FromString)
        self.ConfirmationHeight = channel.unary_unary('/axelar.evm.v1beta1.QueryService/ConfirmationHeight', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ConfirmationHeightRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ConfirmationHeightResponse.FromString)
        self.DepositState = channel.unary_unary('/axelar.evm.v1beta1.QueryService/DepositState', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.DepositStateRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.DepositStateResponse.FromString)
        self.PendingCommands = channel.unary_unary('/axelar.evm.v1beta1.QueryService/PendingCommands', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.PendingCommandsRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.PendingCommandsResponse.FromString)
        self.Chains = channel.unary_unary('/axelar.evm.v1beta1.QueryService/Chains', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ChainsRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ChainsResponse.FromString)
        self.Command = channel.unary_unary('/axelar.evm.v1beta1.QueryService/Command', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.CommandRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.CommandResponse.FromString)
        self.KeyAddress = channel.unary_unary('/axelar.evm.v1beta1.QueryService/KeyAddress', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.KeyAddressRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.KeyAddressResponse.FromString)
        self.GatewayAddress = channel.unary_unary('/axelar.evm.v1beta1.QueryService/GatewayAddress', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.GatewayAddressRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.GatewayAddressResponse.FromString)
        self.Bytecode = channel.unary_unary('/axelar.evm.v1beta1.QueryService/Bytecode', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BytecodeRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BytecodeResponse.FromString)
        self.Event = channel.unary_unary('/axelar.evm.v1beta1.QueryService/Event', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.EventRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.EventResponse.FromString)
        self.ERC20Tokens = channel.unary_unary('/axelar.evm.v1beta1.QueryService/ERC20Tokens', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ERC20TokensRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ERC20TokensResponse.FromString)
        self.TokenInfo = channel.unary_unary('/axelar.evm.v1beta1.QueryService/TokenInfo', request_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.TokenInfoRequest.SerializeToString, response_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.TokenInfoResponse.FromString)

class QueryServiceServicer(object):
    """QueryService defines the gRPC querier service.
    """

    def BatchedCommands(self, request, context):
        """BatchedCommands queries the batched commands for a specified chain and
        BatchedCommandsID if no BatchedCommandsID is specified, then it returns the
        latest batched commands
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BurnerInfo(self, request, context):
        """BurnerInfo queries the burner info for the specified address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmationHeight(self, request, context):
        """ConfirmationHeight queries the confirmation height for the specified chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DepositState(self, request, context):
        """DepositState queries the state of the specified deposit
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PendingCommands(self, request, context):
        """PendingCommands queries the pending commands for the specified chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Chains(self, request, context):
        """Chains queries the available evm chains
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Command(self, request, context):
        """Command queries the command of a chain provided the command id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeyAddress(self, request, context):
        """KeyAddress queries the address of key of a chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GatewayAddress(self, request, context):
        """GatewayAddress queries the address of axelar gateway at the specified
        chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bytecode(self, request, context):
        """Bytecode queries the bytecode of a specified gateway at the specified
        chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Event(self, request, context):
        """Event queries an event at the specified chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ERC20Tokens(self, request, context):
        """ERC20Tokens queries the ERC20 tokens registered for a chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenInfo(self, request, context):
        """TokenInfo queries the token info for a registered ERC20 Token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'BatchedCommands': grpc.unary_unary_rpc_method_handler(servicer.BatchedCommands, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BatchedCommandsRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BatchedCommandsResponse.SerializeToString), 'BurnerInfo': grpc.unary_unary_rpc_method_handler(servicer.BurnerInfo, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BurnerInfoRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BurnerInfoResponse.SerializeToString), 'ConfirmationHeight': grpc.unary_unary_rpc_method_handler(servicer.ConfirmationHeight, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ConfirmationHeightRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ConfirmationHeightResponse.SerializeToString), 'DepositState': grpc.unary_unary_rpc_method_handler(servicer.DepositState, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.DepositStateRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.DepositStateResponse.SerializeToString), 'PendingCommands': grpc.unary_unary_rpc_method_handler(servicer.PendingCommands, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.PendingCommandsRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.PendingCommandsResponse.SerializeToString), 'Chains': grpc.unary_unary_rpc_method_handler(servicer.Chains, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ChainsRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ChainsResponse.SerializeToString), 'Command': grpc.unary_unary_rpc_method_handler(servicer.Command, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.CommandRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.CommandResponse.SerializeToString), 'KeyAddress': grpc.unary_unary_rpc_method_handler(servicer.KeyAddress, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.KeyAddressRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.KeyAddressResponse.SerializeToString), 'GatewayAddress': grpc.unary_unary_rpc_method_handler(servicer.GatewayAddress, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.GatewayAddressRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.GatewayAddressResponse.SerializeToString), 'Bytecode': grpc.unary_unary_rpc_method_handler(servicer.Bytecode, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BytecodeRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.BytecodeResponse.SerializeToString), 'Event': grpc.unary_unary_rpc_method_handler(servicer.Event, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.EventRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.EventResponse.SerializeToString), 'ERC20Tokens': grpc.unary_unary_rpc_method_handler(servicer.ERC20Tokens, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ERC20TokensRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.ERC20TokensResponse.SerializeToString), 'TokenInfo': grpc.unary_unary_rpc_method_handler(servicer.TokenInfo, request_deserializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.TokenInfoRequest.FromString, response_serializer=axelar_dot_evm_dot_v1beta1_dot_query__pb2.TokenInfoResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.evm.v1beta1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class QueryService(object):
    """QueryService defines the gRPC querier service.
    """

    @staticmethod
    def BatchedCommands(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/BatchedCommands', axelar_dot_evm_dot_v1beta1_dot_query__pb2.BatchedCommandsRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.BatchedCommandsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BurnerInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/BurnerInfo', axelar_dot_evm_dot_v1beta1_dot_query__pb2.BurnerInfoRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.BurnerInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmationHeight(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/ConfirmationHeight', axelar_dot_evm_dot_v1beta1_dot_query__pb2.ConfirmationHeightRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.ConfirmationHeightResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DepositState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/DepositState', axelar_dot_evm_dot_v1beta1_dot_query__pb2.DepositStateRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.DepositStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PendingCommands(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/PendingCommands', axelar_dot_evm_dot_v1beta1_dot_query__pb2.PendingCommandsRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.PendingCommandsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Chains(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/Chains', axelar_dot_evm_dot_v1beta1_dot_query__pb2.ChainsRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.ChainsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Command(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/Command', axelar_dot_evm_dot_v1beta1_dot_query__pb2.CommandRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.CommandResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeyAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/KeyAddress', axelar_dot_evm_dot_v1beta1_dot_query__pb2.KeyAddressRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.KeyAddressResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GatewayAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/GatewayAddress', axelar_dot_evm_dot_v1beta1_dot_query__pb2.GatewayAddressRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.GatewayAddressResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Bytecode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/Bytecode', axelar_dot_evm_dot_v1beta1_dot_query__pb2.BytecodeRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.BytecodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Event(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/Event', axelar_dot_evm_dot_v1beta1_dot_query__pb2.EventRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.EventResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ERC20Tokens(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/ERC20Tokens', axelar_dot_evm_dot_v1beta1_dot_query__pb2.ERC20TokensRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.ERC20TokensResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.evm.v1beta1.QueryService/TokenInfo', axelar_dot_evm_dot_v1beta1_dot_query__pb2.TokenInfoRequest.SerializeToString, axelar_dot_evm_dot_v1beta1_dot_query__pb2.TokenInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)