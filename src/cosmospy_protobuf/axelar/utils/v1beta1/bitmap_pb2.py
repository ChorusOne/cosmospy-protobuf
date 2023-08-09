"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/utils/v1beta1/bitmap.proto\x12\x14axelar.utils.v1beta1\x1a\x14gogoproto/gogo.proto"H\n\x06Bitmap\x12>\n\x10true_count_cache\x18\x02 \x01(\x0b2$.axelar.utils.v1beta1.CircularBuffer"K\n\x0eCircularBuffer\x12\x18\n\x10cumulative_value\x18\x01 \x03(\x04\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x10\n\x08max_size\x18\x03 \x01(\x05B0Z*github.com/axelarnetwork/axelar-core/utils\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.utils.v1beta1.bitmap_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z*github.com/axelarnetwork/axelar-core/utils\xc8\xe1\x1e\x00'
    _globals['_BITMAP']._serialized_start = 81
    _globals['_BITMAP']._serialized_end = 153
    _globals['_CIRCULARBUFFER']._serialized_start = 155
    _globals['_CIRCULARBUFFER']._serialized_end = 230