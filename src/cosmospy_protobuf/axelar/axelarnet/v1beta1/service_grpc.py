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
    async def Link(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.LinkRequest, axelar.axelarnet.v1beta1.tx_pb2.LinkResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfirmDeposit(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.ConfirmDepositRequest, axelar.axelarnet.v1beta1.tx_pb2.ConfirmDepositResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExecutePendingTransfers(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.ExecutePendingTransfersRequest, axelar.axelarnet.v1beta1.tx_pb2.ExecutePendingTransfersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddCosmosBasedChain(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.AddCosmosBasedChainRequest, axelar.axelarnet.v1beta1.tx_pb2.AddCosmosBasedChainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RegisterAsset(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.RegisterAssetRequest, axelar.axelarnet.v1beta1.tx_pb2.RegisterAssetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RouteIBCTransfers(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.RouteIBCTransfersRequest, axelar.axelarnet.v1beta1.tx_pb2.RouteIBCTransfersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RegisterFeeCollector(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.RegisterFeeCollectorRequest, axelar.axelarnet.v1beta1.tx_pb2.RegisterFeeCollectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RetryIBCTransfer(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.RetryIBCTransferRequest, axelar.axelarnet.v1beta1.tx_pb2.RetryIBCTransferResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RouteMessage(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.RouteMessageRequest, axelar.axelarnet.v1beta1.tx_pb2.RouteMessageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CallContract(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.tx_pb2.CallContractRequest, axelar.axelarnet.v1beta1.tx_pb2.CallContractResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.axelarnet.v1beta1.MsgService/Link': grpclib.const.Handler(self.Link, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.LinkRequest, axelar.axelarnet.v1beta1.tx_pb2.LinkResponse), '/axelar.axelarnet.v1beta1.MsgService/ConfirmDeposit': grpclib.const.Handler(self.ConfirmDeposit, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.ConfirmDepositRequest, axelar.axelarnet.v1beta1.tx_pb2.ConfirmDepositResponse), '/axelar.axelarnet.v1beta1.MsgService/ExecutePendingTransfers': grpclib.const.Handler(self.ExecutePendingTransfers, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.ExecutePendingTransfersRequest, axelar.axelarnet.v1beta1.tx_pb2.ExecutePendingTransfersResponse), '/axelar.axelarnet.v1beta1.MsgService/AddCosmosBasedChain': grpclib.const.Handler(self.AddCosmosBasedChain, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.AddCosmosBasedChainRequest, axelar.axelarnet.v1beta1.tx_pb2.AddCosmosBasedChainResponse), '/axelar.axelarnet.v1beta1.MsgService/RegisterAsset': grpclib.const.Handler(self.RegisterAsset, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.RegisterAssetRequest, axelar.axelarnet.v1beta1.tx_pb2.RegisterAssetResponse), '/axelar.axelarnet.v1beta1.MsgService/RouteIBCTransfers': grpclib.const.Handler(self.RouteIBCTransfers, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.RouteIBCTransfersRequest, axelar.axelarnet.v1beta1.tx_pb2.RouteIBCTransfersResponse), '/axelar.axelarnet.v1beta1.MsgService/RegisterFeeCollector': grpclib.const.Handler(self.RegisterFeeCollector, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.RegisterFeeCollectorRequest, axelar.axelarnet.v1beta1.tx_pb2.RegisterFeeCollectorResponse), '/axelar.axelarnet.v1beta1.MsgService/RetryIBCTransfer': grpclib.const.Handler(self.RetryIBCTransfer, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.RetryIBCTransferRequest, axelar.axelarnet.v1beta1.tx_pb2.RetryIBCTransferResponse), '/axelar.axelarnet.v1beta1.MsgService/RouteMessage': grpclib.const.Handler(self.RouteMessage, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.RouteMessageRequest, axelar.axelarnet.v1beta1.tx_pb2.RouteMessageResponse), '/axelar.axelarnet.v1beta1.MsgService/CallContract': grpclib.const.Handler(self.CallContract, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.tx_pb2.CallContractRequest, axelar.axelarnet.v1beta1.tx_pb2.CallContractResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Link = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/Link', axelar.axelarnet.v1beta1.tx_pb2.LinkRequest, axelar.axelarnet.v1beta1.tx_pb2.LinkResponse)
        self.ConfirmDeposit = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/ConfirmDeposit', axelar.axelarnet.v1beta1.tx_pb2.ConfirmDepositRequest, axelar.axelarnet.v1beta1.tx_pb2.ConfirmDepositResponse)
        self.ExecutePendingTransfers = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/ExecutePendingTransfers', axelar.axelarnet.v1beta1.tx_pb2.ExecutePendingTransfersRequest, axelar.axelarnet.v1beta1.tx_pb2.ExecutePendingTransfersResponse)
        self.AddCosmosBasedChain = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/AddCosmosBasedChain', axelar.axelarnet.v1beta1.tx_pb2.AddCosmosBasedChainRequest, axelar.axelarnet.v1beta1.tx_pb2.AddCosmosBasedChainResponse)
        self.RegisterAsset = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/RegisterAsset', axelar.axelarnet.v1beta1.tx_pb2.RegisterAssetRequest, axelar.axelarnet.v1beta1.tx_pb2.RegisterAssetResponse)
        self.RouteIBCTransfers = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/RouteIBCTransfers', axelar.axelarnet.v1beta1.tx_pb2.RouteIBCTransfersRequest, axelar.axelarnet.v1beta1.tx_pb2.RouteIBCTransfersResponse)
        self.RegisterFeeCollector = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/RegisterFeeCollector', axelar.axelarnet.v1beta1.tx_pb2.RegisterFeeCollectorRequest, axelar.axelarnet.v1beta1.tx_pb2.RegisterFeeCollectorResponse)
        self.RetryIBCTransfer = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/RetryIBCTransfer', axelar.axelarnet.v1beta1.tx_pb2.RetryIBCTransferRequest, axelar.axelarnet.v1beta1.tx_pb2.RetryIBCTransferResponse)
        self.RouteMessage = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/RouteMessage', axelar.axelarnet.v1beta1.tx_pb2.RouteMessageRequest, axelar.axelarnet.v1beta1.tx_pb2.RouteMessageResponse)
        self.CallContract = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.MsgService/CallContract', axelar.axelarnet.v1beta1.tx_pb2.CallContractRequest, axelar.axelarnet.v1beta1.tx_pb2.CallContractResponse)

class QueryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def PendingIBCTransferCount(self, stream: 'grpclib.server.Stream[axelar.axelarnet.v1beta1.query_pb2.PendingIBCTransferCountRequest, axelar.axelarnet.v1beta1.query_pb2.PendingIBCTransferCountResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.axelarnet.v1beta1.QueryService/PendingIBCTransferCount': grpclib.const.Handler(self.PendingIBCTransferCount, grpclib.const.Cardinality.UNARY_UNARY, axelar.axelarnet.v1beta1.query_pb2.PendingIBCTransferCountRequest, axelar.axelarnet.v1beta1.query_pb2.PendingIBCTransferCountResponse)}

class QueryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.PendingIBCTransferCount = grpclib.client.UnaryUnaryMethod(channel, '/axelar.axelarnet.v1beta1.QueryService/PendingIBCTransferCount', axelar.axelarnet.v1beta1.query_pb2.PendingIBCTransferCountRequest, axelar.axelarnet.v1beta1.query_pb2.PendingIBCTransferCountResponse)