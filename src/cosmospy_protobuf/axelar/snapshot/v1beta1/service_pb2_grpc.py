"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.snapshot.v1beta1 import tx_pb2 as axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the snapshot Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterProxy = channel.unary_unary('/axelar.snapshot.v1beta1.MsgService/RegisterProxy', request_serializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.RegisterProxyRequest.SerializeToString, response_deserializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.RegisterProxyResponse.FromString)
        self.DeactivateProxy = channel.unary_unary('/axelar.snapshot.v1beta1.MsgService/DeactivateProxy', request_serializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.DeactivateProxyRequest.SerializeToString, response_deserializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.DeactivateProxyResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the snapshot Msg service.
    """

    def RegisterProxy(self, request, context):
        """RegisterProxy defines a method for registering a proxy account that can act
        in a validator account's stead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateProxy(self, request, context):
        """DeactivateProxy defines a method for deregistering a proxy account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RegisterProxy': grpc.unary_unary_rpc_method_handler(servicer.RegisterProxy, request_deserializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.RegisterProxyRequest.FromString, response_serializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.RegisterProxyResponse.SerializeToString), 'DeactivateProxy': grpc.unary_unary_rpc_method_handler(servicer.DeactivateProxy, request_deserializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.DeactivateProxyRequest.FromString, response_serializer=axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.DeactivateProxyResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.snapshot.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the snapshot Msg service.
    """

    @staticmethod
    def RegisterProxy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.snapshot.v1beta1.MsgService/RegisterProxy', axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.RegisterProxyRequest.SerializeToString, axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.RegisterProxyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeactivateProxy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.snapshot.v1beta1.MsgService/DeactivateProxy', axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.DeactivateProxyRequest.SerializeToString, axelar_dot_snapshot_dot_v1beta1_dot_tx__pb2.DeactivateProxyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)