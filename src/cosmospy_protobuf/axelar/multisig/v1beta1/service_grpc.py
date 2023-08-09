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
    async def StartKeygen(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.tx_pb2.StartKeygenRequest, axelar.multisig.v1beta1.tx_pb2.StartKeygenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SubmitPubKey(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.tx_pb2.SubmitPubKeyRequest, axelar.multisig.v1beta1.tx_pb2.SubmitPubKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SubmitSignature(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.tx_pb2.SubmitSignatureRequest, axelar.multisig.v1beta1.tx_pb2.SubmitSignatureResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RotateKey(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.tx_pb2.RotateKeyRequest, axelar.multisig.v1beta1.tx_pb2.RotateKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def KeygenOptOut(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.tx_pb2.KeygenOptOutRequest, axelar.multisig.v1beta1.tx_pb2.KeygenOptOutResponse]') -> None:
        pass

    @abc.abstractmethod
    async def KeygenOptIn(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.tx_pb2.KeygenOptInRequest, axelar.multisig.v1beta1.tx_pb2.KeygenOptInResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.multisig.v1beta1.MsgService/StartKeygen': grpclib.const.Handler(self.StartKeygen, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.tx_pb2.StartKeygenRequest, axelar.multisig.v1beta1.tx_pb2.StartKeygenResponse), '/axelar.multisig.v1beta1.MsgService/SubmitPubKey': grpclib.const.Handler(self.SubmitPubKey, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.tx_pb2.SubmitPubKeyRequest, axelar.multisig.v1beta1.tx_pb2.SubmitPubKeyResponse), '/axelar.multisig.v1beta1.MsgService/SubmitSignature': grpclib.const.Handler(self.SubmitSignature, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.tx_pb2.SubmitSignatureRequest, axelar.multisig.v1beta1.tx_pb2.SubmitSignatureResponse), '/axelar.multisig.v1beta1.MsgService/RotateKey': grpclib.const.Handler(self.RotateKey, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.tx_pb2.RotateKeyRequest, axelar.multisig.v1beta1.tx_pb2.RotateKeyResponse), '/axelar.multisig.v1beta1.MsgService/KeygenOptOut': grpclib.const.Handler(self.KeygenOptOut, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.tx_pb2.KeygenOptOutRequest, axelar.multisig.v1beta1.tx_pb2.KeygenOptOutResponse), '/axelar.multisig.v1beta1.MsgService/KeygenOptIn': grpclib.const.Handler(self.KeygenOptIn, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.tx_pb2.KeygenOptInRequest, axelar.multisig.v1beta1.tx_pb2.KeygenOptInResponse)}

class MsgServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.StartKeygen = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.MsgService/StartKeygen', axelar.multisig.v1beta1.tx_pb2.StartKeygenRequest, axelar.multisig.v1beta1.tx_pb2.StartKeygenResponse)
        self.SubmitPubKey = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.MsgService/SubmitPubKey', axelar.multisig.v1beta1.tx_pb2.SubmitPubKeyRequest, axelar.multisig.v1beta1.tx_pb2.SubmitPubKeyResponse)
        self.SubmitSignature = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.MsgService/SubmitSignature', axelar.multisig.v1beta1.tx_pb2.SubmitSignatureRequest, axelar.multisig.v1beta1.tx_pb2.SubmitSignatureResponse)
        self.RotateKey = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.MsgService/RotateKey', axelar.multisig.v1beta1.tx_pb2.RotateKeyRequest, axelar.multisig.v1beta1.tx_pb2.RotateKeyResponse)
        self.KeygenOptOut = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.MsgService/KeygenOptOut', axelar.multisig.v1beta1.tx_pb2.KeygenOptOutRequest, axelar.multisig.v1beta1.tx_pb2.KeygenOptOutResponse)
        self.KeygenOptIn = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.MsgService/KeygenOptIn', axelar.multisig.v1beta1.tx_pb2.KeygenOptInRequest, axelar.multisig.v1beta1.tx_pb2.KeygenOptInResponse)

class QueryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def KeyID(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.query_pb2.KeyIDRequest, axelar.multisig.v1beta1.query_pb2.KeyIDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NextKeyID(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.query_pb2.NextKeyIDRequest, axelar.multisig.v1beta1.query_pb2.NextKeyIDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Key(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.query_pb2.KeyRequest, axelar.multisig.v1beta1.query_pb2.KeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def KeygenSession(self, stream: 'grpclib.server.Stream[axelar.multisig.v1beta1.query_pb2.KeygenSessionRequest, axelar.multisig.v1beta1.query_pb2.KeygenSessionResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/axelar.multisig.v1beta1.QueryService/KeyID': grpclib.const.Handler(self.KeyID, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.query_pb2.KeyIDRequest, axelar.multisig.v1beta1.query_pb2.KeyIDResponse), '/axelar.multisig.v1beta1.QueryService/NextKeyID': grpclib.const.Handler(self.NextKeyID, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.query_pb2.NextKeyIDRequest, axelar.multisig.v1beta1.query_pb2.NextKeyIDResponse), '/axelar.multisig.v1beta1.QueryService/Key': grpclib.const.Handler(self.Key, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.query_pb2.KeyRequest, axelar.multisig.v1beta1.query_pb2.KeyResponse), '/axelar.multisig.v1beta1.QueryService/KeygenSession': grpclib.const.Handler(self.KeygenSession, grpclib.const.Cardinality.UNARY_UNARY, axelar.multisig.v1beta1.query_pb2.KeygenSessionRequest, axelar.multisig.v1beta1.query_pb2.KeygenSessionResponse)}

class QueryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.KeyID = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.QueryService/KeyID', axelar.multisig.v1beta1.query_pb2.KeyIDRequest, axelar.multisig.v1beta1.query_pb2.KeyIDResponse)
        self.NextKeyID = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.QueryService/NextKeyID', axelar.multisig.v1beta1.query_pb2.NextKeyIDRequest, axelar.multisig.v1beta1.query_pb2.NextKeyIDResponse)
        self.Key = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.QueryService/Key', axelar.multisig.v1beta1.query_pb2.KeyRequest, axelar.multisig.v1beta1.query_pb2.KeyResponse)
        self.KeygenSession = grpclib.client.UnaryUnaryMethod(channel, '/axelar.multisig.v1beta1.QueryService/KeygenSession', axelar.multisig.v1beta1.query_pb2.KeygenSessionRequest, axelar.multisig.v1beta1.query_pb2.KeygenSessionResponse)