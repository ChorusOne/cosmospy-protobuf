"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/vote/v1beta1/events.proto\x12\x13axelar.vote.v1beta1\x1a\x14gogoproto/gogo.proto"S\n\x05Voted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x0e\n\x06action\x18\x02 \x01(\t\x12\x0c\n\x04poll\x18\x03 \x01(\t\x12\r\n\x05voter\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\tB7Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.vote.v1beta1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/axelarnetwork/axelar-core/x/vote/types\xc8\xe1\x1e\x00'
    _globals['_VOTED']._serialized_start = 79
    _globals['_VOTED']._serialized_end = 162