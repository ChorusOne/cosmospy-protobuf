import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
from .... import axelar

class MsgBase(abc.ABC):

    @abc.abstractmethod
    async def RegisterController(self, stream: 'grpclib.server.Stream[axelar.permission.v1beta1.tx_pb2.RegisterControllerRequest, axelar.permission.v1beta1.tx_pb2.RegisterControllerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeregisterController(self, stream: 'grpclib.server.Stream[axelar.permission.v1beta1.tx_pb2.DeregisterControllerRequest, axelar.permission.v1beta1.tx_pb2.DeregisterControllerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateGovernanceKey(self, stream: 'grpclib.server.Stream[axelar.permission.v1beta1.tx_pb2.UpdateGovernanceKeyRequest, axelar.permission.v1beta1.tx_pb2.UpdateGovernanceKeyResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.permission.v1beta1.Msg/RegisterController': grpclib.const.Handler(self.RegisterController, grpclib.const.Cardinality.UNARY_UNARY, axelar.permission.v1beta1.tx_pb2.RegisterControllerRequest, axelar.permission.v1beta1.tx_pb2.RegisterControllerResponse), '/axelar.permission.v1beta1.Msg/DeregisterController': grpclib.const.Handler(self.DeregisterController, grpclib.const.Cardinality.UNARY_UNARY, axelar.permission.v1beta1.tx_pb2.DeregisterControllerRequest, axelar.permission.v1beta1.tx_pb2.DeregisterControllerResponse), '/axelar.permission.v1beta1.Msg/UpdateGovernanceKey': grpclib.const.Handler(self.UpdateGovernanceKey, grpclib.const.Cardinality.UNARY_UNARY, axelar.permission.v1beta1.tx_pb2.UpdateGovernanceKeyRequest, axelar.permission.v1beta1.tx_pb2.UpdateGovernanceKeyResponse)}

class MsgStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.RegisterController = grpclib.client.UnaryUnaryMethod(channel, '/axelar.permission.v1beta1.Msg/RegisterController', axelar.permission.v1beta1.tx_pb2.RegisterControllerRequest, axelar.permission.v1beta1.tx_pb2.RegisterControllerResponse)
        self.DeregisterController = grpclib.client.UnaryUnaryMethod(channel, '/axelar.permission.v1beta1.Msg/DeregisterController', axelar.permission.v1beta1.tx_pb2.DeregisterControllerRequest, axelar.permission.v1beta1.tx_pb2.DeregisterControllerResponse)
        self.UpdateGovernanceKey = grpclib.client.UnaryUnaryMethod(channel, '/axelar.permission.v1beta1.Msg/UpdateGovernanceKey', axelar.permission.v1beta1.tx_pb2.UpdateGovernanceKeyRequest, axelar.permission.v1beta1.tx_pb2.UpdateGovernanceKeyResponse)

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def GovernanceKey(self, stream: 'grpclib.server.Stream[axelar.permission.v1beta1.query_pb2.QueryGovernanceKeyRequest, axelar.permission.v1beta1.query_pb2.QueryGovernanceKeyResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.permission.v1beta1.Query/GovernanceKey': grpclib.const.Handler(self.GovernanceKey, grpclib.const.Cardinality.UNARY_UNARY, axelar.permission.v1beta1.query_pb2.QueryGovernanceKeyRequest, axelar.permission.v1beta1.query_pb2.QueryGovernanceKeyResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GovernanceKey = grpclib.client.UnaryUnaryMethod(channel, '/axelar.permission.v1beta1.Query/GovernanceKey', axelar.permission.v1beta1.query_pb2.QueryGovernanceKeyRequest, axelar.permission.v1beta1.query_pb2.QueryGovernanceKeyResponse)