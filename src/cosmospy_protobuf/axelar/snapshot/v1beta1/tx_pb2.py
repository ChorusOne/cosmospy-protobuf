"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/snapshot/v1beta1/tx.proto\x12\x17axelar.snapshot.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\xa6\x01\n\x14RegisterProxyRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12E\n\nproxy_addr\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x01"\x17\n\x15RegisterProxyResponse"a\n\x16DeactivateProxyRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress:\x04\x80\xb5\x18\x01"\x19\n\x17DeactivateProxyResponseB;Z5github.com/axelarnetwork/axelar-core/x/snapshot/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.snapshot.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/snapshot/types\xc8\xe1\x1e\x00'
    _REGISTERPROXYREQUEST.fields_by_name['sender']._options = None
    _REGISTERPROXYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _REGISTERPROXYREQUEST.fields_by_name['proxy_addr']._options = None
    _REGISTERPROXYREQUEST.fields_by_name['proxy_addr']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERPROXYREQUEST._options = None
    _REGISTERPROXYREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _DEACTIVATEPROXYREQUEST.fields_by_name['sender']._options = None
    _DEACTIVATEPROXYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _DEACTIVATEPROXYREQUEST._options = None
    _DEACTIVATEPROXYREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _globals['_REGISTERPROXYREQUEST']._serialized_start = 162
    _globals['_REGISTERPROXYREQUEST']._serialized_end = 328
    _globals['_REGISTERPROXYRESPONSE']._serialized_start = 330
    _globals['_REGISTERPROXYRESPONSE']._serialized_end = 353
    _globals['_DEACTIVATEPROXYREQUEST']._serialized_start = 355
    _globals['_DEACTIVATEPROXYREQUEST']._serialized_end = 452
    _globals['_DEACTIVATEPROXYRESPONSE']._serialized_start = 454
    _globals['_DEACTIVATEPROXYRESPONSE']._serialized_end = 479