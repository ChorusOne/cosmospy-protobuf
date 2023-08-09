"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....axelar.tss.tofnd.v1beta1 import common_pb2 as axelar_dot_tss_dot_tofnd_dot_v1beta1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'axelar/tss/tofnd/v1beta1/multisig.proto\x12\x18axelar.tss.tofnd.v1beta1\x1a%axelar/tss/tofnd/v1beta1/common.proto"3\n\rKeygenRequest\x12\x0f\n\x07key_uid\x18\x01 \x01(\t\x12\x11\n\tparty_uid\x18\x02 \x01(\t"G\n\x0eKeygenResponse\x12\x11\n\x07pub_key\x18\x01 \x01(\x0cH\x00\x12\x0f\n\x05error\x18\x02 \x01(\tH\x00B\x11\n\x0fkeygen_response"W\n\x0bSignRequest\x12\x0f\n\x07key_uid\x18\x01 \x01(\t\x12\x13\n\x0bmsg_to_sign\x18\x02 \x01(\x0c\x12\x11\n\tparty_uid\x18\x03 \x01(\t\x12\x0f\n\x07pub_key\x18\x04 \x01(\x0c"E\n\x0cSignResponse\x12\x13\n\tsignature\x18\x01 \x01(\x0cH\x00\x12\x0f\n\x05error\x18\x02 \x01(\tH\x00B\x0f\n\rsign_responseB2Z0github.com/axelarnetwork/axelar-core/x/tss/tofndb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.tofnd.v1beta1.multisig_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/tofnd'
    _globals['_KEYGENREQUEST']._serialized_start = 108
    _globals['_KEYGENREQUEST']._serialized_end = 159
    _globals['_KEYGENRESPONSE']._serialized_start = 161
    _globals['_KEYGENRESPONSE']._serialized_end = 232
    _globals['_SIGNREQUEST']._serialized_start = 234
    _globals['_SIGNREQUEST']._serialized_end = 321
    _globals['_SIGNRESPONSE']._serialized_start = 323
    _globals['_SIGNRESPONSE']._serialized_end = 392