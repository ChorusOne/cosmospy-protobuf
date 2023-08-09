"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.axelarnet.v1beta1 import query_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2
from ....axelar.axelarnet.v1beta1 import tx_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the axelarnet Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Link = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/Link', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.LinkRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.LinkResponse.FromString)
        self.ConfirmDeposit = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/ConfirmDeposit', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ConfirmDepositRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ConfirmDepositResponse.FromString)
        self.ExecutePendingTransfers = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/ExecutePendingTransfers', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ExecutePendingTransfersRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ExecutePendingTransfersResponse.FromString)
        self.AddCosmosBasedChain = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/AddCosmosBasedChain', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.AddCosmosBasedChainRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.AddCosmosBasedChainResponse.FromString)
        self.RegisterAsset = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/RegisterAsset', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterAssetRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterAssetResponse.FromString)
        self.RouteIBCTransfers = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/RouteIBCTransfers', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteIBCTransfersRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteIBCTransfersResponse.FromString)
        self.RegisterFeeCollector = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/RegisterFeeCollector', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterFeeCollectorRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterFeeCollectorResponse.FromString)
        self.RetryIBCTransfer = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/RetryIBCTransfer', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RetryIBCTransferRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RetryIBCTransferResponse.FromString)
        self.RouteMessage = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/RouteMessage', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteMessageRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteMessageResponse.FromString)
        self.CallContract = channel.unary_unary('/axelar.axelarnet.v1beta1.MsgService/CallContract', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.CallContractRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.CallContractResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the axelarnet Msg service.
    """

    def Link(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmDeposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecutePendingTransfers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCosmosBasedChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterAsset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteIBCTransfers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterFeeCollector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetryIBCTransfer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallContract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Link': grpc.unary_unary_rpc_method_handler(servicer.Link, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.LinkRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.LinkResponse.SerializeToString), 'ConfirmDeposit': grpc.unary_unary_rpc_method_handler(servicer.ConfirmDeposit, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ConfirmDepositRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ConfirmDepositResponse.SerializeToString), 'ExecutePendingTransfers': grpc.unary_unary_rpc_method_handler(servicer.ExecutePendingTransfers, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ExecutePendingTransfersRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ExecutePendingTransfersResponse.SerializeToString), 'AddCosmosBasedChain': grpc.unary_unary_rpc_method_handler(servicer.AddCosmosBasedChain, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.AddCosmosBasedChainRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.AddCosmosBasedChainResponse.SerializeToString), 'RegisterAsset': grpc.unary_unary_rpc_method_handler(servicer.RegisterAsset, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterAssetRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterAssetResponse.SerializeToString), 'RouteIBCTransfers': grpc.unary_unary_rpc_method_handler(servicer.RouteIBCTransfers, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteIBCTransfersRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteIBCTransfersResponse.SerializeToString), 'RegisterFeeCollector': grpc.unary_unary_rpc_method_handler(servicer.RegisterFeeCollector, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterFeeCollectorRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterFeeCollectorResponse.SerializeToString), 'RetryIBCTransfer': grpc.unary_unary_rpc_method_handler(servicer.RetryIBCTransfer, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RetryIBCTransferRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RetryIBCTransferResponse.SerializeToString), 'RouteMessage': grpc.unary_unary_rpc_method_handler(servicer.RouteMessage, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteMessageRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteMessageResponse.SerializeToString), 'CallContract': grpc.unary_unary_rpc_method_handler(servicer.CallContract, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.CallContractRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.CallContractResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.axelarnet.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the axelarnet Msg service.
    """

    @staticmethod
    def Link(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/Link', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.LinkRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.LinkResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmDeposit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/ConfirmDeposit', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ConfirmDepositRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ConfirmDepositResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecutePendingTransfers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/ExecutePendingTransfers', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ExecutePendingTransfersRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.ExecutePendingTransfersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCosmosBasedChain(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/AddCosmosBasedChain', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.AddCosmosBasedChainRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.AddCosmosBasedChainResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/RegisterAsset', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterAssetRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterAssetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteIBCTransfers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/RouteIBCTransfers', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteIBCTransfersRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteIBCTransfersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterFeeCollector(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/RegisterFeeCollector', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterFeeCollectorRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RegisterFeeCollectorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetryIBCTransfer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/RetryIBCTransfer', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RetryIBCTransferRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RetryIBCTransferResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/RouteMessage', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteMessageRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.RouteMessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallContract(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.MsgService/CallContract', axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.CallContractRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_tx__pb2.CallContractResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryServiceStub(object):
    """QueryService defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PendingIBCTransferCount = channel.unary_unary('/axelar.axelarnet.v1beta1.QueryService/PendingIBCTransferCount', request_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2.PendingIBCTransferCountRequest.SerializeToString, response_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2.PendingIBCTransferCountResponse.FromString)

class QueryServiceServicer(object):
    """QueryService defines the gRPC querier service.
    """

    def PendingIBCTransferCount(self, request, context):
        """PendingIBCTransferCount queries the pending ibc transfers for all chains
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'PendingIBCTransferCount': grpc.unary_unary_rpc_method_handler(servicer.PendingIBCTransferCount, request_deserializer=axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2.PendingIBCTransferCountRequest.FromString, response_serializer=axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2.PendingIBCTransferCountResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.axelarnet.v1beta1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class QueryService(object):
    """QueryService defines the gRPC querier service.
    """

    @staticmethod
    def PendingIBCTransferCount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.axelarnet.v1beta1.QueryService/PendingIBCTransferCount', axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2.PendingIBCTransferCountRequest.SerializeToString, axelar_dot_axelarnet_dot_v1beta1_dot_query__pb2.PendingIBCTransferCountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)