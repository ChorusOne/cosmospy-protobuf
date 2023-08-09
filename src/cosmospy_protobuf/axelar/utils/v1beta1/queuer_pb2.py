"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/utils/v1beta1/queuer.proto\x12\x14axelar.utils.v1beta1\x1a\x14gogoproto/gogo.proto"\xcd\x01\n\nQueueState\x12@\n\x05items\x18\x01 \x03(\x0b2+.axelar.utils.v1beta1.QueueState.ItemsEntryB\x04\xc8\xde\x1f\x00\x1a"\n\x04Item\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x1aS\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x124\n\x05value\x18\x02 \x01(\x0b2%.axelar.utils.v1beta1.QueueState.Item:\x028\x01:\x04\x98\xa1\x1f\x01B0Z*github.com/axelarnetwork/axelar-core/utils\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.utils.v1beta1.queuer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z*github.com/axelarnetwork/axelar-core/utils\xc8\xe1\x1e\x00'
    _QUEUESTATE_ITEMSENTRY._options = None
    _QUEUESTATE_ITEMSENTRY._serialized_options = b'8\x01'
    _QUEUESTATE.fields_by_name['items']._options = None
    _QUEUESTATE.fields_by_name['items']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUEUESTATE._options = None
    _QUEUESTATE._serialized_options = b'\x98\xa1\x1f\x01'
    _globals['_QUEUESTATE']._serialized_start = 82
    _globals['_QUEUESTATE']._serialized_end = 287
    _globals['_QUEUESTATE_ITEM']._serialized_start = 162
    _globals['_QUEUESTATE_ITEM']._serialized_end = 196
    _globals['_QUEUESTATE_ITEMSENTRY']._serialized_start = 198
    _globals['_QUEUESTATE_ITEMSENTRY']._serialized_end = 281