import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
from .... import axelar

class MsgServiceBase(abc.ABC):

    @abc.abstractmethod
    async def RegisterChainMaintainer(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.tx_pb2.RegisterChainMaintainerRequest, axelar.nexus.v1beta1.tx_pb2.RegisterChainMaintainerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeregisterChainMaintainer(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.tx_pb2.DeregisterChainMaintainerRequest, axelar.nexus.v1beta1.tx_pb2.DeregisterChainMaintainerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ActivateChain(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.tx_pb2.ActivateChainRequest, axelar.nexus.v1beta1.tx_pb2.ActivateChainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeactivateChain(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.tx_pb2.DeactivateChainRequest, axelar.nexus.v1beta1.tx_pb2.DeactivateChainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RegisterAssetFee(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.tx_pb2.RegisterAssetFeeRequest, axelar.nexus.v1beta1.tx_pb2.RegisterAssetFeeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetTransferRateLimit(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.tx_pb2.SetTransferRateLimitRequest, axelar.nexus.v1beta1.tx_pb2.SetTransferRateLimitResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.nexus.v1beta1.MsgService/RegisterChainMaintainer': grpclib.const.Handler(self.RegisterChainMaintainer, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.tx_pb2.RegisterChainMaintainerRequest, axelar.nexus.v1beta1.tx_pb2.RegisterChainMaintainerResponse), '/axelar.nexus.v1beta1.MsgService/DeregisterChainMaintainer': grpclib.const.Handler(self.DeregisterChainMaintainer, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.tx_pb2.DeregisterChainMaintainerRequest, axelar.nexus.v1beta1.tx_pb2.DeregisterChainMaintainerResponse), '/axelar.nexus.v1beta1.MsgService/ActivateChain': grpclib.const.Handler(self.ActivateChain, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.tx_pb2.ActivateChainRequest, axelar.nexus.v1beta1.tx_pb2.ActivateChainResponse), '/axelar.nexus.v1beta1.MsgService/DeactivateChain': grpclib.const.Handler(self.DeactivateChain, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.tx_pb2.DeactivateChainRequest, axelar.nexus.v1beta1.tx_pb2.DeactivateChainResponse), '/axelar.nexus.v1beta1.MsgService/RegisterAssetFee': grpclib.const.Handler(self.RegisterAssetFee, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.tx_pb2.RegisterAssetFeeRequest, axelar.nexus.v1beta1.tx_pb2.RegisterAssetFeeResponse), '/axelar.nexus.v1beta1.MsgService/SetTransferRateLimit': grpclib.const.Handler(self.SetTransferRateLimit, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.tx_pb2.SetTransferRateLimitRequest, axelar.nexus.v1beta1.tx_pb2.SetTransferRateLimitResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.RegisterChainMaintainer = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.MsgService/RegisterChainMaintainer', axelar.nexus.v1beta1.tx_pb2.RegisterChainMaintainerRequest, axelar.nexus.v1beta1.tx_pb2.RegisterChainMaintainerResponse)
        self.DeregisterChainMaintainer = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.MsgService/DeregisterChainMaintainer', axelar.nexus.v1beta1.tx_pb2.DeregisterChainMaintainerRequest, axelar.nexus.v1beta1.tx_pb2.DeregisterChainMaintainerResponse)
        self.ActivateChain = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.MsgService/ActivateChain', axelar.nexus.v1beta1.tx_pb2.ActivateChainRequest, axelar.nexus.v1beta1.tx_pb2.ActivateChainResponse)
        self.DeactivateChain = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.MsgService/DeactivateChain', axelar.nexus.v1beta1.tx_pb2.DeactivateChainRequest, axelar.nexus.v1beta1.tx_pb2.DeactivateChainResponse)
        self.RegisterAssetFee = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.MsgService/RegisterAssetFee', axelar.nexus.v1beta1.tx_pb2.RegisterAssetFeeRequest, axelar.nexus.v1beta1.tx_pb2.RegisterAssetFeeResponse)
        self.SetTransferRateLimit = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.MsgService/SetTransferRateLimit', axelar.nexus.v1beta1.tx_pb2.SetTransferRateLimitRequest, axelar.nexus.v1beta1.tx_pb2.SetTransferRateLimitResponse)

class QueryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def LatestDepositAddress(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.LatestDepositAddressRequest, axelar.nexus.v1beta1.query_pb2.LatestDepositAddressResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransfersForChain(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.TransfersForChainRequest, axelar.nexus.v1beta1.query_pb2.TransfersForChainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FeeInfo(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.FeeInfoRequest, axelar.nexus.v1beta1.query_pb2.FeeInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransferFee(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.TransferFeeRequest, axelar.nexus.v1beta1.query_pb2.TransferFeeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Chains(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.ChainsRequest, axelar.nexus.v1beta1.query_pb2.ChainsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Assets(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.AssetsRequest, axelar.nexus.v1beta1.query_pb2.AssetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChainState(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.ChainStateRequest, axelar.nexus.v1beta1.query_pb2.ChainStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChainsByAsset(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.ChainsByAssetRequest, axelar.nexus.v1beta1.query_pb2.ChainsByAssetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RecipientAddress(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.RecipientAddressRequest, axelar.nexus.v1beta1.query_pb2.RecipientAddressResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChainMaintainers(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.ChainMaintainersRequest, axelar.nexus.v1beta1.query_pb2.ChainMaintainersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransferRateLimit(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.TransferRateLimitRequest, axelar.nexus.v1beta1.query_pb2.TransferRateLimitResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Message(self, stream: 'grpclib.server.Stream[axelar.nexus.v1beta1.query_pb2.MessageRequest, axelar.nexus.v1beta1.query_pb2.MessageResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.nexus.v1beta1.QueryService/LatestDepositAddress': grpclib.const.Handler(self.LatestDepositAddress, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.LatestDepositAddressRequest, axelar.nexus.v1beta1.query_pb2.LatestDepositAddressResponse), '/axelar.nexus.v1beta1.QueryService/TransfersForChain': grpclib.const.Handler(self.TransfersForChain, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.TransfersForChainRequest, axelar.nexus.v1beta1.query_pb2.TransfersForChainResponse), '/axelar.nexus.v1beta1.QueryService/FeeInfo': grpclib.const.Handler(self.FeeInfo, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.FeeInfoRequest, axelar.nexus.v1beta1.query_pb2.FeeInfoResponse), '/axelar.nexus.v1beta1.QueryService/TransferFee': grpclib.const.Handler(self.TransferFee, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.TransferFeeRequest, axelar.nexus.v1beta1.query_pb2.TransferFeeResponse), '/axelar.nexus.v1beta1.QueryService/Chains': grpclib.const.Handler(self.Chains, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.ChainsRequest, axelar.nexus.v1beta1.query_pb2.ChainsResponse), '/axelar.nexus.v1beta1.QueryService/Assets': grpclib.const.Handler(self.Assets, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.AssetsRequest, axelar.nexus.v1beta1.query_pb2.AssetsResponse), '/axelar.nexus.v1beta1.QueryService/ChainState': grpclib.const.Handler(self.ChainState, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.ChainStateRequest, axelar.nexus.v1beta1.query_pb2.ChainStateResponse), '/axelar.nexus.v1beta1.QueryService/ChainsByAsset': grpclib.const.Handler(self.ChainsByAsset, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.ChainsByAssetRequest, axelar.nexus.v1beta1.query_pb2.ChainsByAssetResponse), '/axelar.nexus.v1beta1.QueryService/RecipientAddress': grpclib.const.Handler(self.RecipientAddress, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.RecipientAddressRequest, axelar.nexus.v1beta1.query_pb2.RecipientAddressResponse), '/axelar.nexus.v1beta1.QueryService/ChainMaintainers': grpclib.const.Handler(self.ChainMaintainers, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.ChainMaintainersRequest, axelar.nexus.v1beta1.query_pb2.ChainMaintainersResponse), '/axelar.nexus.v1beta1.QueryService/TransferRateLimit': grpclib.const.Handler(self.TransferRateLimit, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.TransferRateLimitRequest, axelar.nexus.v1beta1.query_pb2.TransferRateLimitResponse), '/axelar.nexus.v1beta1.QueryService/Message': grpclib.const.Handler(self.Message, grpclib.const.Cardinality.UNARY_UNARY, axelar.nexus.v1beta1.query_pb2.MessageRequest, axelar.nexus.v1beta1.query_pb2.MessageResponse)}

class QueryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.LatestDepositAddress = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/LatestDepositAddress', axelar.nexus.v1beta1.query_pb2.LatestDepositAddressRequest, axelar.nexus.v1beta1.query_pb2.LatestDepositAddressResponse)
        self.TransfersForChain = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/TransfersForChain', axelar.nexus.v1beta1.query_pb2.TransfersForChainRequest, axelar.nexus.v1beta1.query_pb2.TransfersForChainResponse)
        self.FeeInfo = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/FeeInfo', axelar.nexus.v1beta1.query_pb2.FeeInfoRequest, axelar.nexus.v1beta1.query_pb2.FeeInfoResponse)
        self.TransferFee = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/TransferFee', axelar.nexus.v1beta1.query_pb2.TransferFeeRequest, axelar.nexus.v1beta1.query_pb2.TransferFeeResponse)
        self.Chains = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/Chains', axelar.nexus.v1beta1.query_pb2.ChainsRequest, axelar.nexus.v1beta1.query_pb2.ChainsResponse)
        self.Assets = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/Assets', axelar.nexus.v1beta1.query_pb2.AssetsRequest, axelar.nexus.v1beta1.query_pb2.AssetsResponse)
        self.ChainState = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/ChainState', axelar.nexus.v1beta1.query_pb2.ChainStateRequest, axelar.nexus.v1beta1.query_pb2.ChainStateResponse)
        self.ChainsByAsset = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/ChainsByAsset', axelar.nexus.v1beta1.query_pb2.ChainsByAssetRequest, axelar.nexus.v1beta1.query_pb2.ChainsByAssetResponse)
        self.RecipientAddress = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/RecipientAddress', axelar.nexus.v1beta1.query_pb2.RecipientAddressRequest, axelar.nexus.v1beta1.query_pb2.RecipientAddressResponse)
        self.ChainMaintainers = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/ChainMaintainers', axelar.nexus.v1beta1.query_pb2.ChainMaintainersRequest, axelar.nexus.v1beta1.query_pb2.ChainMaintainersResponse)
        self.TransferRateLimit = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/TransferRateLimit', axelar.nexus.v1beta1.query_pb2.TransferRateLimitRequest, axelar.nexus.v1beta1.query_pb2.TransferRateLimitResponse)
        self.Message = grpclib.client.UnaryUnaryMethod(channel, '/axelar.nexus.v1beta1.QueryService/Message', axelar.nexus.v1beta1.query_pb2.MessageRequest, axelar.nexus.v1beta1.query_pb2.MessageResponse)