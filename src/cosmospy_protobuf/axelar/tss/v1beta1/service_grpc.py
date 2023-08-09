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
    async def HeartBeat(self, stream: 'grpclib.server.Stream[axelar.tss.v1beta1.tx_pb2.HeartBeatRequest, axelar.tss.v1beta1.tx_pb2.HeartBeatResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.tss.v1beta1.MsgService/HeartBeat': grpclib.const.Handler(self.HeartBeat, grpclib.const.Cardinality.UNARY_UNARY, axelar.tss.v1beta1.tx_pb2.HeartBeatRequest, axelar.tss.v1beta1.tx_pb2.HeartBeatResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.HeartBeat = grpclib.client.UnaryUnaryMethod(channel, '/axelar.tss.v1beta1.MsgService/HeartBeat', axelar.tss.v1beta1.tx_pb2.HeartBeatRequest, axelar.tss.v1beta1.tx_pb2.HeartBeatResponse)

class QueryServiceBase(abc.ABC):

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {}

class QueryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        pass