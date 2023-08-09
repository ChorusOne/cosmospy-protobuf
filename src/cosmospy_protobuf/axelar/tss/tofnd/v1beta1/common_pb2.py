"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%axelar/tss/tofnd/v1beta1/common.proto\x12\x18axelar.tss.tofnd.v1beta1\x1a\x14gogoproto/gogo.proto"6\n\x12KeyPresenceRequest\x12\x0f\n\x07key_uid\x18\x01 \x01(\t\x12\x0f\n\x07pub_key\x18\x02 \x01(\x0c"\xc9\x01\n\x13KeyPresenceResponse\x12H\n\x08response\x18\x01 \x01(\x0e26.axelar.tss.tofnd.v1beta1.KeyPresenceResponse.Response"h\n\x08Response\x12\x18\n\x14RESPONSE_UNSPECIFIED\x10\x00\x12\x14\n\x10RESPONSE_PRESENT\x10\x01\x12\x13\n\x0fRESPONSE_ABSENT\x10\x02\x12\x11\n\rRESPONSE_FAIL\x10\x03\x1a\x04\x88\xa3\x1e\x00B2Z0github.com/axelarnetwork/axelar-core/x/tss/tofndb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.tofnd.v1beta1.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/tofnd'
    _KEYPRESENCERESPONSE_RESPONSE._options = None
    _KEYPRESENCERESPONSE_RESPONSE._serialized_options = b'\x88\xa3\x1e\x00'
    _globals['_KEYPRESENCEREQUEST']._serialized_start = 89
    _globals['_KEYPRESENCEREQUEST']._serialized_end = 143
    _globals['_KEYPRESENCERESPONSE']._serialized_start = 146
    _globals['_KEYPRESENCERESPONSE']._serialized_end = 347
    _globals['_KEYPRESENCERESPONSE_RESPONSE']._serialized_start = 243
    _globals['_KEYPRESENCERESPONSE_RESPONSE']._serialized_end = 347