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
    async def RegisterProxy(self, stream: 'grpclib.server.Stream[axelar.snapshot.v1beta1.tx_pb2.RegisterProxyRequest, axelar.snapshot.v1beta1.tx_pb2.RegisterProxyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeactivateProxy(self, stream: 'grpclib.server.Stream[axelar.snapshot.v1beta1.tx_pb2.DeactivateProxyRequest, axelar.snapshot.v1beta1.tx_pb2.DeactivateProxyResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.snapshot.v1beta1.MsgService/RegisterProxy': grpclib.const.Handler(self.RegisterProxy, grpclib.const.Cardinality.UNARY_UNARY, axelar.snapshot.v1beta1.tx_pb2.RegisterProxyRequest, axelar.snapshot.v1beta1.tx_pb2.RegisterProxyResponse), '/axelar.snapshot.v1beta1.MsgService/DeactivateProxy': grpclib.const.Handler(self.DeactivateProxy, grpclib.const.Cardinality.UNARY_UNARY, axelar.snapshot.v1beta1.tx_pb2.DeactivateProxyRequest, axelar.snapshot.v1beta1.tx_pb2.DeactivateProxyResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.RegisterProxy = grpclib.client.UnaryUnaryMethod(channel, '/axelar.snapshot.v1beta1.MsgService/RegisterProxy', axelar.snapshot.v1beta1.tx_pb2.RegisterProxyRequest, axelar.snapshot.v1beta1.tx_pb2.RegisterProxyResponse)
        self.DeactivateProxy = grpclib.client.UnaryUnaryMethod(channel, '/axelar.snapshot.v1beta1.MsgService/DeactivateProxy', axelar.snapshot.v1beta1.tx_pb2.DeactivateProxyRequest, axelar.snapshot.v1beta1.tx_pb2.DeactivateProxyResponse)