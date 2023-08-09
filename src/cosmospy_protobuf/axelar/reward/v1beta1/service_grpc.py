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
    async def RefundMsg(self, stream: 'grpclib.server.Stream[axelar.reward.v1beta1.tx_pb2.RefundMsgRequest, axelar.reward.v1beta1.tx_pb2.RefundMsgResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.reward.v1beta1.MsgService/RefundMsg': grpclib.const.Handler(self.RefundMsg, grpclib.const.Cardinality.UNARY_UNARY, axelar.reward.v1beta1.tx_pb2.RefundMsgRequest, axelar.reward.v1beta1.tx_pb2.RefundMsgResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.RefundMsg = grpclib.client.UnaryUnaryMethod(channel, '/axelar.reward.v1beta1.MsgService/RefundMsg', axelar.reward.v1beta1.tx_pb2.RefundMsgRequest, axelar.reward.v1beta1.tx_pb2.RefundMsgResponse)

class QueryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def InflationRate(self, stream: 'grpclib.server.Stream[axelar.reward.v1beta1.query_pb2.InflationRateRequest, axelar.reward.v1beta1.query_pb2.InflationRateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[axelar.reward.v1beta1.query_pb2.ParamsRequest, axelar.reward.v1beta1.query_pb2.ParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.reward.v1beta1.QueryService/InflationRate': grpclib.const.Handler(self.InflationRate, grpclib.const.Cardinality.UNARY_UNARY, axelar.reward.v1beta1.query_pb2.InflationRateRequest, axelar.reward.v1beta1.query_pb2.InflationRateResponse), '/axelar.reward.v1beta1.QueryService/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, axelar.reward.v1beta1.query_pb2.ParamsRequest, axelar.reward.v1beta1.query_pb2.ParamsResponse)}

class QueryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.InflationRate = grpclib.client.UnaryUnaryMethod(channel, '/axelar.reward.v1beta1.QueryService/InflationRate', axelar.reward.v1beta1.query_pb2.InflationRateRequest, axelar.reward.v1beta1.query_pb2.InflationRateResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/axelar.reward.v1beta1.QueryService/Params', axelar.reward.v1beta1.query_pb2.ParamsRequest, axelar.reward.v1beta1.query_pb2.ParamsResponse)