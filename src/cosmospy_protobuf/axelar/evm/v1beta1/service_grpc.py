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
    async def SetGateway(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.SetGatewayRequest, axelar.evm.v1beta1.tx_pb2.SetGatewayResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfirmGatewayTx(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.ConfirmGatewayTxRequest, axelar.evm.v1beta1.tx_pb2.ConfirmGatewayTxResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Link(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.LinkRequest, axelar.evm.v1beta1.tx_pb2.LinkResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfirmToken(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.ConfirmTokenRequest, axelar.evm.v1beta1.tx_pb2.ConfirmTokenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfirmDeposit(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.ConfirmDepositRequest, axelar.evm.v1beta1.tx_pb2.ConfirmDepositResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfirmTransferKey(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.ConfirmTransferKeyRequest, axelar.evm.v1beta1.tx_pb2.ConfirmTransferKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateDeployToken(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.CreateDeployTokenRequest, axelar.evm.v1beta1.tx_pb2.CreateDeployTokenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateBurnTokens(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.CreateBurnTokensRequest, axelar.evm.v1beta1.tx_pb2.CreateBurnTokensResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreatePendingTransfers(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.CreatePendingTransfersRequest, axelar.evm.v1beta1.tx_pb2.CreatePendingTransfersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTransferOperatorship(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.CreateTransferOperatorshipRequest, axelar.evm.v1beta1.tx_pb2.CreateTransferOperatorshipResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SignCommands(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.SignCommandsRequest, axelar.evm.v1beta1.tx_pb2.SignCommandsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddChain(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.AddChainRequest, axelar.evm.v1beta1.tx_pb2.AddChainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RetryFailedEvent(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.tx_pb2.RetryFailedEventRequest, axelar.evm.v1beta1.tx_pb2.RetryFailedEventResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.evm.v1beta1.MsgService/SetGateway': grpclib.const.Handler(self.SetGateway, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.SetGatewayRequest, axelar.evm.v1beta1.tx_pb2.SetGatewayResponse), '/axelar.evm.v1beta1.MsgService/ConfirmGatewayTx': grpclib.const.Handler(self.ConfirmGatewayTx, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.ConfirmGatewayTxRequest, axelar.evm.v1beta1.tx_pb2.ConfirmGatewayTxResponse), '/axelar.evm.v1beta1.MsgService/Link': grpclib.const.Handler(self.Link, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.LinkRequest, axelar.evm.v1beta1.tx_pb2.LinkResponse), '/axelar.evm.v1beta1.MsgService/ConfirmToken': grpclib.const.Handler(self.ConfirmToken, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.ConfirmTokenRequest, axelar.evm.v1beta1.tx_pb2.ConfirmTokenResponse), '/axelar.evm.v1beta1.MsgService/ConfirmDeposit': grpclib.const.Handler(self.ConfirmDeposit, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.ConfirmDepositRequest, axelar.evm.v1beta1.tx_pb2.ConfirmDepositResponse), '/axelar.evm.v1beta1.MsgService/ConfirmTransferKey': grpclib.const.Handler(self.ConfirmTransferKey, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.ConfirmTransferKeyRequest, axelar.evm.v1beta1.tx_pb2.ConfirmTransferKeyResponse), '/axelar.evm.v1beta1.MsgService/CreateDeployToken': grpclib.const.Handler(self.CreateDeployToken, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.CreateDeployTokenRequest, axelar.evm.v1beta1.tx_pb2.CreateDeployTokenResponse), '/axelar.evm.v1beta1.MsgService/CreateBurnTokens': grpclib.const.Handler(self.CreateBurnTokens, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.CreateBurnTokensRequest, axelar.evm.v1beta1.tx_pb2.CreateBurnTokensResponse), '/axelar.evm.v1beta1.MsgService/CreatePendingTransfers': grpclib.const.Handler(self.CreatePendingTransfers, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.CreatePendingTransfersRequest, axelar.evm.v1beta1.tx_pb2.CreatePendingTransfersResponse), '/axelar.evm.v1beta1.MsgService/CreateTransferOperatorship': grpclib.const.Handler(self.CreateTransferOperatorship, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.CreateTransferOperatorshipRequest, axelar.evm.v1beta1.tx_pb2.CreateTransferOperatorshipResponse), '/axelar.evm.v1beta1.MsgService/SignCommands': grpclib.const.Handler(self.SignCommands, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.SignCommandsRequest, axelar.evm.v1beta1.tx_pb2.SignCommandsResponse), '/axelar.evm.v1beta1.MsgService/AddChain': grpclib.const.Handler(self.AddChain, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.AddChainRequest, axelar.evm.v1beta1.tx_pb2.AddChainResponse), '/axelar.evm.v1beta1.MsgService/RetryFailedEvent': grpclib.const.Handler(self.RetryFailedEvent, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.tx_pb2.RetryFailedEventRequest, axelar.evm.v1beta1.tx_pb2.RetryFailedEventResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetGateway = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/SetGateway', axelar.evm.v1beta1.tx_pb2.SetGatewayRequest, axelar.evm.v1beta1.tx_pb2.SetGatewayResponse)
        self.ConfirmGatewayTx = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/ConfirmGatewayTx', axelar.evm.v1beta1.tx_pb2.ConfirmGatewayTxRequest, axelar.evm.v1beta1.tx_pb2.ConfirmGatewayTxResponse)
        self.Link = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/Link', axelar.evm.v1beta1.tx_pb2.LinkRequest, axelar.evm.v1beta1.tx_pb2.LinkResponse)
        self.ConfirmToken = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/ConfirmToken', axelar.evm.v1beta1.tx_pb2.ConfirmTokenRequest, axelar.evm.v1beta1.tx_pb2.ConfirmTokenResponse)
        self.ConfirmDeposit = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/ConfirmDeposit', axelar.evm.v1beta1.tx_pb2.ConfirmDepositRequest, axelar.evm.v1beta1.tx_pb2.ConfirmDepositResponse)
        self.ConfirmTransferKey = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/ConfirmTransferKey', axelar.evm.v1beta1.tx_pb2.ConfirmTransferKeyRequest, axelar.evm.v1beta1.tx_pb2.ConfirmTransferKeyResponse)
        self.CreateDeployToken = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/CreateDeployToken', axelar.evm.v1beta1.tx_pb2.CreateDeployTokenRequest, axelar.evm.v1beta1.tx_pb2.CreateDeployTokenResponse)
        self.CreateBurnTokens = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/CreateBurnTokens', axelar.evm.v1beta1.tx_pb2.CreateBurnTokensRequest, axelar.evm.v1beta1.tx_pb2.CreateBurnTokensResponse)
        self.CreatePendingTransfers = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/CreatePendingTransfers', axelar.evm.v1beta1.tx_pb2.CreatePendingTransfersRequest, axelar.evm.v1beta1.tx_pb2.CreatePendingTransfersResponse)
        self.CreateTransferOperatorship = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/CreateTransferOperatorship', axelar.evm.v1beta1.tx_pb2.CreateTransferOperatorshipRequest, axelar.evm.v1beta1.tx_pb2.CreateTransferOperatorshipResponse)
        self.SignCommands = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/SignCommands', axelar.evm.v1beta1.tx_pb2.SignCommandsRequest, axelar.evm.v1beta1.tx_pb2.SignCommandsResponse)
        self.AddChain = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/AddChain', axelar.evm.v1beta1.tx_pb2.AddChainRequest, axelar.evm.v1beta1.tx_pb2.AddChainResponse)
        self.RetryFailedEvent = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.MsgService/RetryFailedEvent', axelar.evm.v1beta1.tx_pb2.RetryFailedEventRequest, axelar.evm.v1beta1.tx_pb2.RetryFailedEventResponse)

class QueryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def BatchedCommands(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.BatchedCommandsRequest, axelar.evm.v1beta1.query_pb2.BatchedCommandsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BurnerInfo(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.BurnerInfoRequest, axelar.evm.v1beta1.query_pb2.BurnerInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfirmationHeight(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.ConfirmationHeightRequest, axelar.evm.v1beta1.query_pb2.ConfirmationHeightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DepositState(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.DepositStateRequest, axelar.evm.v1beta1.query_pb2.DepositStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PendingCommands(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.PendingCommandsRequest, axelar.evm.v1beta1.query_pb2.PendingCommandsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Chains(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.ChainsRequest, axelar.evm.v1beta1.query_pb2.ChainsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Command(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.CommandRequest, axelar.evm.v1beta1.query_pb2.CommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def KeyAddress(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.KeyAddressRequest, axelar.evm.v1beta1.query_pb2.KeyAddressResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GatewayAddress(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.GatewayAddressRequest, axelar.evm.v1beta1.query_pb2.GatewayAddressResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Bytecode(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.BytecodeRequest, axelar.evm.v1beta1.query_pb2.BytecodeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Event(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.EventRequest, axelar.evm.v1beta1.query_pb2.EventResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ERC20Tokens(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.ERC20TokensRequest, axelar.evm.v1beta1.query_pb2.ERC20TokensResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TokenInfo(self, stream: 'grpclib.server.Stream[axelar.evm.v1beta1.query_pb2.TokenInfoRequest, axelar.evm.v1beta1.query_pb2.TokenInfoResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.evm.v1beta1.QueryService/BatchedCommands': grpclib.const.Handler(self.BatchedCommands, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.BatchedCommandsRequest, axelar.evm.v1beta1.query_pb2.BatchedCommandsResponse), '/axelar.evm.v1beta1.QueryService/BurnerInfo': grpclib.const.Handler(self.BurnerInfo, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.BurnerInfoRequest, axelar.evm.v1beta1.query_pb2.BurnerInfoResponse), '/axelar.evm.v1beta1.QueryService/ConfirmationHeight': grpclib.const.Handler(self.ConfirmationHeight, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.ConfirmationHeightRequest, axelar.evm.v1beta1.query_pb2.ConfirmationHeightResponse), '/axelar.evm.v1beta1.QueryService/DepositState': grpclib.const.Handler(self.DepositState, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.DepositStateRequest, axelar.evm.v1beta1.query_pb2.DepositStateResponse), '/axelar.evm.v1beta1.QueryService/PendingCommands': grpclib.const.Handler(self.PendingCommands, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.PendingCommandsRequest, axelar.evm.v1beta1.query_pb2.PendingCommandsResponse), '/axelar.evm.v1beta1.QueryService/Chains': grpclib.const.Handler(self.Chains, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.ChainsRequest, axelar.evm.v1beta1.query_pb2.ChainsResponse), '/axelar.evm.v1beta1.QueryService/Command': grpclib.const.Handler(self.Command, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.CommandRequest, axelar.evm.v1beta1.query_pb2.CommandResponse), '/axelar.evm.v1beta1.QueryService/KeyAddress': grpclib.const.Handler(self.KeyAddress, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.KeyAddressRequest, axelar.evm.v1beta1.query_pb2.KeyAddressResponse), '/axelar.evm.v1beta1.QueryService/GatewayAddress': grpclib.const.Handler(self.GatewayAddress, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.GatewayAddressRequest, axelar.evm.v1beta1.query_pb2.GatewayAddressResponse), '/axelar.evm.v1beta1.QueryService/Bytecode': grpclib.const.Handler(self.Bytecode, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.BytecodeRequest, axelar.evm.v1beta1.query_pb2.BytecodeResponse), '/axelar.evm.v1beta1.QueryService/Event': grpclib.const.Handler(self.Event, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.EventRequest, axelar.evm.v1beta1.query_pb2.EventResponse), '/axelar.evm.v1beta1.QueryService/ERC20Tokens': grpclib.const.Handler(self.ERC20Tokens, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.ERC20TokensRequest, axelar.evm.v1beta1.query_pb2.ERC20TokensResponse), '/axelar.evm.v1beta1.QueryService/TokenInfo': grpclib.const.Handler(self.TokenInfo, grpclib.const.Cardinality.UNARY_UNARY, axelar.evm.v1beta1.query_pb2.TokenInfoRequest, axelar.evm.v1beta1.query_pb2.TokenInfoResponse)}

class QueryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.BatchedCommands = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/BatchedCommands', axelar.evm.v1beta1.query_pb2.BatchedCommandsRequest, axelar.evm.v1beta1.query_pb2.BatchedCommandsResponse)
        self.BurnerInfo = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/BurnerInfo', axelar.evm.v1beta1.query_pb2.BurnerInfoRequest, axelar.evm.v1beta1.query_pb2.BurnerInfoResponse)
        self.ConfirmationHeight = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/ConfirmationHeight', axelar.evm.v1beta1.query_pb2.ConfirmationHeightRequest, axelar.evm.v1beta1.query_pb2.ConfirmationHeightResponse)
        self.DepositState = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/DepositState', axelar.evm.v1beta1.query_pb2.DepositStateRequest, axelar.evm.v1beta1.query_pb2.DepositStateResponse)
        self.PendingCommands = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/PendingCommands', axelar.evm.v1beta1.query_pb2.PendingCommandsRequest, axelar.evm.v1beta1.query_pb2.PendingCommandsResponse)
        self.Chains = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/Chains', axelar.evm.v1beta1.query_pb2.ChainsRequest, axelar.evm.v1beta1.query_pb2.ChainsResponse)
        self.Command = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/Command', axelar.evm.v1beta1.query_pb2.CommandRequest, axelar.evm.v1beta1.query_pb2.CommandResponse)
        self.KeyAddress = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/KeyAddress', axelar.evm.v1beta1.query_pb2.KeyAddressRequest, axelar.evm.v1beta1.query_pb2.KeyAddressResponse)
        self.GatewayAddress = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/GatewayAddress', axelar.evm.v1beta1.query_pb2.GatewayAddressRequest, axelar.evm.v1beta1.query_pb2.GatewayAddressResponse)
        self.Bytecode = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/Bytecode', axelar.evm.v1beta1.query_pb2.BytecodeRequest, axelar.evm.v1beta1.query_pb2.BytecodeResponse)
        self.Event = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/Event', axelar.evm.v1beta1.query_pb2.EventRequest, axelar.evm.v1beta1.query_pb2.EventResponse)
        self.ERC20Tokens = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/ERC20Tokens', axelar.evm.v1beta1.query_pb2.ERC20TokensRequest, axelar.evm.v1beta1.query_pb2.ERC20TokensResponse)
        self.TokenInfo = grpclib.client.UnaryUnaryMethod(channel, '/axelar.evm.v1beta1.QueryService/TokenInfo', axelar.evm.v1beta1.query_pb2.TokenInfoRequest, axelar.evm.v1beta1.query_pb2.TokenInfoResponse)