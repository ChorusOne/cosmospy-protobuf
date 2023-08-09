"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.nexus.v1beta1 import query_pb2 as axelar_dot_nexus_dot_v1beta1_dot_query__pb2
from ....axelar.nexus.v1beta1 import tx_pb2 as axelar_dot_nexus_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the nexus Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterChainMaintainer = channel.unary_unary('/axelar.nexus.v1beta1.MsgService/RegisterChainMaintainer', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterChainMaintainerRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterChainMaintainerResponse.FromString)
        self.DeregisterChainMaintainer = channel.unary_unary('/axelar.nexus.v1beta1.MsgService/DeregisterChainMaintainer', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeregisterChainMaintainerRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeregisterChainMaintainerResponse.FromString)
        self.ActivateChain = channel.unary_unary('/axelar.nexus.v1beta1.MsgService/ActivateChain', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.ActivateChainRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.ActivateChainResponse.FromString)
        self.DeactivateChain = channel.unary_unary('/axelar.nexus.v1beta1.MsgService/DeactivateChain', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeactivateChainRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeactivateChainResponse.FromString)
        self.RegisterAssetFee = channel.unary_unary('/axelar.nexus.v1beta1.MsgService/RegisterAssetFee', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterAssetFeeRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterAssetFeeResponse.FromString)
        self.SetTransferRateLimit = channel.unary_unary('/axelar.nexus.v1beta1.MsgService/SetTransferRateLimit', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.SetTransferRateLimitRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.SetTransferRateLimitResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the nexus Msg service.
    """

    def RegisterChainMaintainer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeregisterChainMaintainer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterAssetFee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTransferRateLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RegisterChainMaintainer': grpc.unary_unary_rpc_method_handler(servicer.RegisterChainMaintainer, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterChainMaintainerRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterChainMaintainerResponse.SerializeToString), 'DeregisterChainMaintainer': grpc.unary_unary_rpc_method_handler(servicer.DeregisterChainMaintainer, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeregisterChainMaintainerRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeregisterChainMaintainerResponse.SerializeToString), 'ActivateChain': grpc.unary_unary_rpc_method_handler(servicer.ActivateChain, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.ActivateChainRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.ActivateChainResponse.SerializeToString), 'DeactivateChain': grpc.unary_unary_rpc_method_handler(servicer.DeactivateChain, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeactivateChainRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeactivateChainResponse.SerializeToString), 'RegisterAssetFee': grpc.unary_unary_rpc_method_handler(servicer.RegisterAssetFee, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterAssetFeeRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterAssetFeeResponse.SerializeToString), 'SetTransferRateLimit': grpc.unary_unary_rpc_method_handler(servicer.SetTransferRateLimit, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.SetTransferRateLimitRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.SetTransferRateLimitResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.nexus.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the nexus Msg service.
    """

    @staticmethod
    def RegisterChainMaintainer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.MsgService/RegisterChainMaintainer', axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterChainMaintainerRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterChainMaintainerResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeregisterChainMaintainer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.MsgService/DeregisterChainMaintainer', axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeregisterChainMaintainerRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeregisterChainMaintainerResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActivateChain(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.MsgService/ActivateChain', axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.ActivateChainRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.ActivateChainResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeactivateChain(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.MsgService/DeactivateChain', axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeactivateChainRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.DeactivateChainResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterAssetFee(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.MsgService/RegisterAssetFee', axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterAssetFeeRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.RegisterAssetFeeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTransferRateLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.MsgService/SetTransferRateLimit', axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.SetTransferRateLimitRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_tx__pb2.SetTransferRateLimitResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryServiceStub(object):
    """QueryService defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LatestDepositAddress = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/LatestDepositAddress', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.LatestDepositAddressRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.LatestDepositAddressResponse.FromString)
        self.TransfersForChain = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/TransfersForChain', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransfersForChainRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransfersForChainResponse.FromString)
        self.FeeInfo = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/FeeInfo', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.FeeInfoRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.FeeInfoResponse.FromString)
        self.TransferFee = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/TransferFee', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferFeeRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferFeeResponse.FromString)
        self.Chains = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/Chains', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsResponse.FromString)
        self.Assets = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/Assets', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.AssetsRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.AssetsResponse.FromString)
        self.ChainState = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/ChainState', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainStateRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainStateResponse.FromString)
        self.ChainsByAsset = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/ChainsByAsset', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsByAssetRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsByAssetResponse.FromString)
        self.RecipientAddress = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/RecipientAddress', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.RecipientAddressRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.RecipientAddressResponse.FromString)
        self.ChainMaintainers = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/ChainMaintainers', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainMaintainersRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainMaintainersResponse.FromString)
        self.TransferRateLimit = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/TransferRateLimit', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferRateLimitRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferRateLimitResponse.FromString)
        self.Message = channel.unary_unary('/axelar.nexus.v1beta1.QueryService/Message', request_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.MessageRequest.SerializeToString, response_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.MessageResponse.FromString)

class QueryServiceServicer(object):
    """QueryService defines the gRPC querier service.
    """

    def LatestDepositAddress(self, request, context):
        """LatestDepositAddress queries the a deposit address by recipient
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransfersForChain(self, request, context):
        """TransfersForChain queries transfers by chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FeeInfo(self, request, context):
        """FeeInfo queries the fee info by chain and asset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferFee(self, request, context):
        """TransferFee queries the transfer fee by the source, destination chain,
        and amount. If amount is 0, the min fee is returned
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Chains(self, request, context):
        """Chains queries the chains registered on the network
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Assets(self, request, context):
        """Assets queries the assets registered for a chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChainState(self, request, context):
        """ChainState queries the state of a registered chain on the network
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChainsByAsset(self, request, context):
        """ChainsByAsset queries the chains that support an asset on the network
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecipientAddress(self, request, context):
        """RecipientAddress queries the recipient address for a given deposit address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChainMaintainers(self, request, context):
        """ChainMaintainers queries the chain maintainers for a given chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferRateLimit(self, request, context):
        """TransferRateLimit queries the transfer rate limit for a given chain and
        asset. If a rate limit is not set, nil is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'LatestDepositAddress': grpc.unary_unary_rpc_method_handler(servicer.LatestDepositAddress, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.LatestDepositAddressRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.LatestDepositAddressResponse.SerializeToString), 'TransfersForChain': grpc.unary_unary_rpc_method_handler(servicer.TransfersForChain, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransfersForChainRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransfersForChainResponse.SerializeToString), 'FeeInfo': grpc.unary_unary_rpc_method_handler(servicer.FeeInfo, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.FeeInfoRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.FeeInfoResponse.SerializeToString), 'TransferFee': grpc.unary_unary_rpc_method_handler(servicer.TransferFee, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferFeeRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferFeeResponse.SerializeToString), 'Chains': grpc.unary_unary_rpc_method_handler(servicer.Chains, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsResponse.SerializeToString), 'Assets': grpc.unary_unary_rpc_method_handler(servicer.Assets, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.AssetsRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.AssetsResponse.SerializeToString), 'ChainState': grpc.unary_unary_rpc_method_handler(servicer.ChainState, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainStateRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainStateResponse.SerializeToString), 'ChainsByAsset': grpc.unary_unary_rpc_method_handler(servicer.ChainsByAsset, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsByAssetRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsByAssetResponse.SerializeToString), 'RecipientAddress': grpc.unary_unary_rpc_method_handler(servicer.RecipientAddress, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.RecipientAddressRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.RecipientAddressResponse.SerializeToString), 'ChainMaintainers': grpc.unary_unary_rpc_method_handler(servicer.ChainMaintainers, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainMaintainersRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainMaintainersResponse.SerializeToString), 'TransferRateLimit': grpc.unary_unary_rpc_method_handler(servicer.TransferRateLimit, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferRateLimitRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferRateLimitResponse.SerializeToString), 'Message': grpc.unary_unary_rpc_method_handler(servicer.Message, request_deserializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.MessageRequest.FromString, response_serializer=axelar_dot_nexus_dot_v1beta1_dot_query__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.nexus.v1beta1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class QueryService(object):
    """QueryService defines the gRPC querier service.
    """

    @staticmethod
    def LatestDepositAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/LatestDepositAddress', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.LatestDepositAddressRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.LatestDepositAddressResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransfersForChain(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/TransfersForChain', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransfersForChainRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransfersForChainResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FeeInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/FeeInfo', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.FeeInfoRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.FeeInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferFee(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/TransferFee', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferFeeRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferFeeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Chains(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/Chains', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Assets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/Assets', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.AssetsRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.AssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChainState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/ChainState', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainStateRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChainsByAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/ChainsByAsset', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsByAssetRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainsByAssetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecipientAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/RecipientAddress', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.RecipientAddressRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.RecipientAddressResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChainMaintainers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/ChainMaintainers', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainMaintainersRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.ChainMaintainersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferRateLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/TransferRateLimit', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferRateLimitRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.TransferRateLimitResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Message(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.nexus.v1beta1.QueryService/Message', axelar_dot_nexus_dot_v1beta1_dot_query__pb2.MessageRequest.SerializeToString, axelar_dot_nexus_dot_v1beta1_dot_query__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)