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
    async def Vote(self, stream: 'grpclib.server.Stream[axelar.vote.v1beta1.tx_pb2.VoteRequest, axelar.vote.v1beta1.tx_pb2.VoteResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.vote.v1beta1.MsgService/Vote': grpclib.const.Handler(self.Vote, grpclib.const.Cardinality.UNARY_UNARY, axelar.vote.v1beta1.tx_pb2.VoteRequest, axelar.vote.v1beta1.tx_pb2.VoteResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Vote = grpclib.client.UnaryUnaryMethod(channel, '/axelar.vote.v1beta1.MsgService/Vote', axelar.vote.v1beta1.tx_pb2.VoteRequest, axelar.vote.v1beta1.tx_pb2.VoteResponse)