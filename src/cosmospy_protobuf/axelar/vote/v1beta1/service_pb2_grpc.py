"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....axelar.vote.v1beta1 import tx_pb2 as axelar_dot_vote_dot_v1beta1_dot_tx__pb2

class MsgServiceStub(object):
    """Msg defines the vote Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Vote = channel.unary_unary('/axelar.vote.v1beta1.MsgService/Vote', request_serializer=axelar_dot_vote_dot_v1beta1_dot_tx__pb2.VoteRequest.SerializeToString, response_deserializer=axelar_dot_vote_dot_v1beta1_dot_tx__pb2.VoteResponse.FromString)

class MsgServiceServicer(object):
    """Msg defines the vote Msg service.
    """

    def Vote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Vote': grpc.unary_unary_rpc_method_handler(servicer.Vote, request_deserializer=axelar_dot_vote_dot_v1beta1_dot_tx__pb2.VoteRequest.FromString, response_serializer=axelar_dot_vote_dot_v1beta1_dot_tx__pb2.VoteResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('axelar.vote.v1beta1.MsgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MsgService(object):
    """Msg defines the vote Msg service.
    """

    @staticmethod
    def Vote(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/axelar.vote.v1beta1.MsgService/Vote', axelar_dot_vote_dot_v1beta1_dot_tx__pb2.VoteRequest.SerializeToString, axelar_dot_vote_dot_v1beta1_dot_tx__pb2.VoteResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)