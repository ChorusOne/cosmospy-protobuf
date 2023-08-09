"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.axelarnet.v1beta1 import types_pb2 as axelar_dot_axelarnet_dot_v1beta1_dot_types__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....axelar.nexus.v1beta1 import query_pb2 as axelar_dot_nexus_dot_v1beta1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$axelar/axelarnet/v1beta1/query.proto\x12\x18axelar.axelarnet.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$axelar/axelarnet/v1beta1/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a axelar/nexus/v1beta1/query.proto" \n\x1ePendingIBCTransferCountRequest"\xcd\x01\n\x1fPendingIBCTransferCountResponse\x12q\n\x12transfers_by_chain\x18\x01 \x03(\x0b2O.axelar.axelarnet.v1beta1.PendingIBCTransferCountResponse.TransfersByChainEntryB\x04\xc8\xde\x1f\x00\x1a7\n\x15TransfersByChainEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x028\x01B<Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.axelarnet.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe1\x1e\x00'
    _PENDINGIBCTRANSFERCOUNTRESPONSE_TRANSFERSBYCHAINENTRY._options = None
    _PENDINGIBCTRANSFERCOUNTRESPONSE_TRANSFERSBYCHAINENTRY._serialized_options = b'8\x01'
    _PENDINGIBCTRANSFERCOUNTRESPONSE.fields_by_name['transfers_by_chain']._options = None
    _PENDINGIBCTRANSFERCOUNTRESPONSE.fields_by_name['transfers_by_chain']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PENDINGIBCTRANSFERCOUNTREQUEST']._serialized_start = 204
    _globals['_PENDINGIBCTRANSFERCOUNTREQUEST']._serialized_end = 236
    _globals['_PENDINGIBCTRANSFERCOUNTRESPONSE']._serialized_start = 239
    _globals['_PENDINGIBCTRANSFERCOUNTRESPONSE']._serialized_end = 444
    _globals['_PENDINGIBCTRANSFERCOUNTRESPONSE_TRANSFERSBYCHAINENTRY']._serialized_start = 389
    _globals['_PENDINGIBCTRANSFERCOUNTRESPONSE_TRANSFERSBYCHAINENTRY']._serialized_end = 444