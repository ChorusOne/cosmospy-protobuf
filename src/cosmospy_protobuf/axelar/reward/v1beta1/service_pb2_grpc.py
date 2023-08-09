"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.reward.v1beta1 import query_pb2 as axelar_dot_reward_dot_v1beta1_dot_query__pb2
from ....axelar.reward.v1beta1 import tx_pb2 as axelar_dot_reward_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the axelarnet Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RefundMsg = channel.unary_unary('/axelar.reward.v1beta1.MsgService/RefundMsg', request_serializer=axelar_dot_reward_dot_v1beta1_dot_tx__pb2.RefundMsgRequest.SerializeToString, response_deserializer=axelar_dot_reward_dot_v1beta1_dot_tx__pb2.RefundMsgResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the axelarnet Msg service.
    """

    def RefundMsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RefundMsg': grpc.unary_unary_rpc_method_handler(servicer.RefundMsg, request_deserializer=axelar_dot_reward_dot_v1beta1_dot_tx__pb2.RefundMsgRequest.FromString, response_serializer=axelar_dot_reward_dot_v1beta1_dot_tx__pb2.RefundMsgResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.reward.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the axelarnet Msg service.
    """

    @staticmethod
    def RefundMsg(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.reward.v1beta1.MsgService/RefundMsg', axelar_dot_reward_dot_v1beta1_dot_tx__pb2.RefundMsgRequest.SerializeToString, axelar_dot_reward_dot_v1beta1_dot_tx__pb2.RefundMsgResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class QueryServiceStub(object):
    """QueryService defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InflationRate = channel.unary_unary('/axelar.reward.v1beta1.QueryService/InflationRate', request_serializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.InflationRateRequest.SerializeToString, response_deserializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.InflationRateResponse.FromString)
        self.Params = channel.unary_unary('/axelar.reward.v1beta1.QueryService/Params', request_serializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, response_deserializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString)

class QueryServiceServicer(object):
    """QueryService defines the gRPC querier service.
    """

    def InflationRate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'InflationRate': grpc.unary_unary_rpc_method_handler(servicer.InflationRate, request_deserializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.InflationRateRequest.FromString, response_serializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.InflationRateResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.ParamsRequest.FromString, response_serializer=axelar_dot_reward_dot_v1beta1_dot_query__pb2.ParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.reward.v1beta1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class QueryService(object):
    """QueryService defines the gRPC querier service.
    """

    @staticmethod
    def InflationRate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.reward.v1beta1.QueryService/InflationRate', axelar_dot_reward_dot_v1beta1_dot_query__pb2.InflationRateRequest.SerializeToString, axelar_dot_reward_dot_v1beta1_dot_query__pb2.InflationRateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.reward.v1beta1.QueryService/Params', axelar_dot_reward_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, axelar_dot_reward_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)