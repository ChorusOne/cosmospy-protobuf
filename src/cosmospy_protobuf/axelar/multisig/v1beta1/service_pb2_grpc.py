"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.multisig.v1beta1 import query_pb2 as axelar_dot_multisig_dot_v1beta1_dot_query__pb2
from ....axelar.multisig.v1beta1 import tx_pb2 as axelar_dot_multisig_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the multisig Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartKeygen = channel.unary_unary('/axelar.multisig.v1beta1.MsgService/StartKeygen', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.StartKeygenRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.StartKeygenResponse.FromString)
        self.SubmitPubKey = channel.unary_unary('/axelar.multisig.v1beta1.MsgService/SubmitPubKey', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitPubKeyRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitPubKeyResponse.FromString)
        self.SubmitSignature = channel.unary_unary('/axelar.multisig.v1beta1.MsgService/SubmitSignature', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitSignatureRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitSignatureResponse.FromString)
        self.RotateKey = channel.unary_unary('/axelar.multisig.v1beta1.MsgService/RotateKey', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.RotateKeyRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.RotateKeyResponse.FromString)
        self.KeygenOptOut = channel.unary_unary('/axelar.multisig.v1beta1.MsgService/KeygenOptOut', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptOutRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptOutResponse.FromString)
        self.KeygenOptIn = channel.unary_unary('/axelar.multisig.v1beta1.MsgService/KeygenOptIn', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptInRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptInResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the multisig Msg service.
    """

    def StartKeygen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitPubKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitSignature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RotateKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeygenOptOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeygenOptIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'StartKeygen': grpc.unary_unary_rpc_method_handler(servicer.StartKeygen, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.StartKeygenRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.StartKeygenResponse.SerializeToString), 'SubmitPubKey': grpc.unary_unary_rpc_method_handler(servicer.SubmitPubKey, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitPubKeyRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitPubKeyResponse.SerializeToString), 'SubmitSignature': grpc.unary_unary_rpc_method_handler(servicer.SubmitSignature, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitSignatureRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitSignatureResponse.SerializeToString), 'RotateKey': grpc.unary_unary_rpc_method_handler(servicer.RotateKey, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.RotateKeyRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.RotateKeyResponse.SerializeToString), 'KeygenOptOut': grpc.unary_unary_rpc_method_handler(servicer.KeygenOptOut, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptOutRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptOutResponse.SerializeToString), 'KeygenOptIn': grpc.unary_unary_rpc_method_handler(servicer.KeygenOptIn, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptInRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptInResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.multisig.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the multisig Msg service.
    """

    @staticmethod
    def StartKeygen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.MsgService/StartKeygen', axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.StartKeygenRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.StartKeygenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitPubKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.MsgService/SubmitPubKey', axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitPubKeyRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitPubKeyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitSignature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.MsgService/SubmitSignature', axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitSignatureRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.SubmitSignatureResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RotateKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.MsgService/RotateKey', axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.RotateKeyRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.RotateKeyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeygenOptOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.MsgService/KeygenOptOut', axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptOutRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptOutResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeygenOptIn(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.MsgService/KeygenOptIn', axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptInRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_tx__pb2.KeygenOptInResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryServiceStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.KeyID = channel.unary_unary('/axelar.multisig.v1beta1.QueryService/KeyID', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyIDRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyIDResponse.FromString)
        self.NextKeyID = channel.unary_unary('/axelar.multisig.v1beta1.QueryService/NextKeyID', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.NextKeyIDRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.NextKeyIDResponse.FromString)
        self.Key = channel.unary_unary('/axelar.multisig.v1beta1.QueryService/Key', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyResponse.FromString)
        self.KeygenSession = channel.unary_unary('/axelar.multisig.v1beta1.QueryService/KeygenSession', request_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeygenSessionRequest.SerializeToString, response_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeygenSessionResponse.FromString)

class QueryServiceServicer(object):
    """Query defines the gRPC querier service.
    """

    def KeyID(self, request, context):
        """KeyID returns the key ID of a key assigned to a given chain.
        If no key is assigned, it returns the grpc NOT_FOUND error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NextKeyID(self, request, context):
        """NextKeyID returns the key ID assigned for the next rotation on a given
        chain. If no key rotation is in progress, it returns the grpc NOT_FOUND
        error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Key(self, request, context):
        """Key returns the key corresponding to a given key ID.
        If no key is found, it returns the grpc NOT_FOUND error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeygenSession(self, request, context):
        """KeygenSession returns the keygen session info for a given key ID.
        If no key is found, it returns the grpc NOT_FOUND error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'KeyID': grpc.unary_unary_rpc_method_handler(servicer.KeyID, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyIDRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyIDResponse.SerializeToString), 'NextKeyID': grpc.unary_unary_rpc_method_handler(servicer.NextKeyID, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.NextKeyIDRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.NextKeyIDResponse.SerializeToString), 'Key': grpc.unary_unary_rpc_method_handler(servicer.Key, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyResponse.SerializeToString), 'KeygenSession': grpc.unary_unary_rpc_method_handler(servicer.KeygenSession, request_deserializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeygenSessionRequest.FromString, response_serializer=axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeygenSessionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.multisig.v1beta1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class QueryService(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def KeyID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.QueryService/KeyID', axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyIDRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NextKeyID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.QueryService/NextKeyID', axelar_dot_multisig_dot_v1beta1_dot_query__pb2.NextKeyIDRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_query__pb2.NextKeyIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Key(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.QueryService/Key', axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeygenSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.multisig.v1beta1.QueryService/KeygenSession', axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeygenSessionRequest.SerializeToString, axelar_dot_multisig_dot_v1beta1_dot_query__pb2.KeygenSessionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)