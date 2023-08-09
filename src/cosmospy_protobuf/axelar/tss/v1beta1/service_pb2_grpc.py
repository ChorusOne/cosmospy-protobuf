"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.tss.v1beta1 import tx_pb2 as axelar_dot_tss_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the tss Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HeartBeat = channel.unary_unary('/axelar.tss.v1beta1.MsgService/HeartBeat', request_serializer=axelar_dot_tss_dot_v1beta1_dot_tx__pb2.HeartBeatRequest.SerializeToString, response_deserializer=axelar_dot_tss_dot_v1beta1_dot_tx__pb2.HeartBeatResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the tss Msg service.
    """

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'HeartBeat': grpc.unary_unary_rpc_method_handler(servicer.HeartBeat, request_deserializer=axelar_dot_tss_dot_v1beta1_dot_tx__pb2.HeartBeatRequest.FromString, response_serializer=axelar_dot_tss_dot_v1beta1_dot_tx__pb2.HeartBeatResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.tss.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the tss Msg service.
    """

    @staticmethod
    def HeartBeat(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.tss.v1beta1.MsgService/HeartBeat', axelar_dot_tss_dot_v1beta1_dot_tx__pb2.HeartBeatRequest.SerializeToString, axelar_dot_tss_dot_v1beta1_dot_tx__pb2.HeartBeatResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryServiceStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class QueryServiceServicer(object):
    """Query defines the gRPC querier service.
    """

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {}
    generic_handler = grpc.method_handlers_generic_handler('axelar.tss.v1beta1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class QueryService(object):
    """Query defines the gRPC querier service.
    """