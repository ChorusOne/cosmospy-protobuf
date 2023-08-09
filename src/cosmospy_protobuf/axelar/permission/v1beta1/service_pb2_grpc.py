"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.permission.v1beta1 import query_pb2 as axelar_dot_permission_dot_v1beta1_dot_query__pb2
from ....axelar.permission.v1beta1 import tx_pb2 as axelar_dot_permission_dot_v1beta1_dot_tx__pb2

class MsgStub(object):
    """Msg defines the gov Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterController = channel.unary_unary('/axelar.permission.v1beta1.Msg/RegisterController', request_serializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.RegisterControllerRequest.SerializeToString, response_deserializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.RegisterControllerResponse.FromString)
        self.DeregisterController = channel.unary_unary('/axelar.permission.v1beta1.Msg/DeregisterController', request_serializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.DeregisterControllerRequest.SerializeToString, response_deserializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.DeregisterControllerResponse.FromString)
        self.UpdateGovernanceKey = channel.unary_unary('/axelar.permission.v1beta1.Msg/UpdateGovernanceKey', request_serializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.UpdateGovernanceKeyRequest.SerializeToString, response_deserializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.UpdateGovernanceKeyResponse.FromString)

class MsgServicer(object):
    """Msg defines the gov Msg service.
    """

    def RegisterController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeregisterController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateGovernanceKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {'RegisterController': grpc.unary_unary_rpc_method_handler(servicer.RegisterController, request_deserializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.RegisterControllerRequest.FromString, response_serializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.RegisterControllerResponse.SerializeToString), 'DeregisterController': grpc.unary_unary_rpc_method_handler(servicer.DeregisterController, request_deserializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.DeregisterControllerRequest.FromString, response_serializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.DeregisterControllerResponse.SerializeToString), 'UpdateGovernanceKey': grpc.unary_unary_rpc_method_handler(servicer.UpdateGovernanceKey, request_deserializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.UpdateGovernanceKeyRequest.FromString, response_serializer=axelar_dot_permission_dot_v1beta1_dot_tx__pb2.UpdateGovernanceKeyResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.permission.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Msg(object):
    """Msg defines the gov Msg service.
    """

    @staticmethod
    def RegisterController(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.permission.v1beta1.Msg/RegisterController', axelar_dot_permission_dot_v1beta1_dot_tx__pb2.RegisterControllerRequest.SerializeToString, axelar_dot_permission_dot_v1beta1_dot_tx__pb2.RegisterControllerResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeregisterController(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.permission.v1beta1.Msg/DeregisterController', axelar_dot_permission_dot_v1beta1_dot_tx__pb2.DeregisterControllerRequest.SerializeToString, axelar_dot_permission_dot_v1beta1_dot_tx__pb2.DeregisterControllerResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateGovernanceKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.permission.v1beta1.Msg/UpdateGovernanceKey', axelar_dot_permission_dot_v1beta1_dot_tx__pb2.UpdateGovernanceKeyRequest.SerializeToString, axelar_dot_permission_dot_v1beta1_dot_tx__pb2.UpdateGovernanceKeyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GovernanceKey = channel.unary_unary('/axelar.permission.v1beta1.Query/GovernanceKey', request_serializer=axelar_dot_permission_dot_v1beta1_dot_query__pb2.QueryGovernanceKeyRequest.SerializeToString, response_deserializer=axelar_dot_permission_dot_v1beta1_dot_query__pb2.QueryGovernanceKeyResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def GovernanceKey(self, request, context):
        """GovernanceKey returns the multisig governance key
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'GovernanceKey': grpc.unary_unary_rpc_method_handler(servicer.GovernanceKey, request_deserializer=axelar_dot_permission_dot_v1beta1_dot_query__pb2.QueryGovernanceKeyRequest.FromString, response_serializer=axelar_dot_permission_dot_v1beta1_dot_query__pb2.QueryGovernanceKeyResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.permission.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def GovernanceKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.permission.v1beta1.Query/GovernanceKey', axelar_dot_permission_dot_v1beta1_dot_query__pb2.QueryGovernanceKeyRequest.SerializeToString, axelar_dot_permission_dot_v1beta1_dot_query__pb2.QueryGovernanceKeyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)