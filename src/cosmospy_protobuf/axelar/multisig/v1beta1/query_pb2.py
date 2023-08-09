"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....axelar.multisig.exported.v1beta1 import types_pb2 as axelar_dot_multisig_dot_exported_dot_v1beta1_dot_types__pb2
from ....axelar.multisig.v1beta1 import types_pb2 as axelar_dot_multisig_dot_v1beta1_dot_types__pb2
from ....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#axelar/multisig/v1beta1/query.proto\x12\x17axelar.multisig.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a,axelar/multisig/exported/v1beta1/types.proto\x1a#axelar/multisig/v1beta1/types.proto\x1a$axelar/utils/v1beta1/threshold.proto"\x1d\n\x0cKeyIDRequest\x12\r\n\x05chain\x18\x01 \x01(\t"l\n\rKeyIDResponse\x12[\n\x06key_id\x18\x01 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID"!\n\x10NextKeyIDRequest\x12\r\n\x05chain\x18\x01 \x01(\t"p\n\x11NextKeyIDResponse\x12[\n\x06key_id\x18\x01 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID"i\n\nKeyRequest\x12[\n\x06key_id\x18\x01 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID"v\n\x11KeygenParticipant\x12\x0f\n\x07address\x18\x01 \x01(\t\x12?\n\x06weight\x18\x02 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12\x0f\n\x07pub_key\x18\x03 \x01(\t"\xd8\x03\n\x0bKeyResponse\x12[\n\x06key_id\x18\x01 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x129\n\x05state\x18\x02 \x01(\x0e2*.axelar.multisig.exported.v1beta1.KeyState\x12\x12\n\nstarted_at\x18\x03 \x01(\x03\x12B\n\x14started_at_timestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12I\n\x10threshold_weight\x18\x05 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12F\n\rbonded_weight\x18\x06 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12F\n\x0cparticipants\x18\x07 \x03(\x0b2*.axelar.multisig.v1beta1.KeygenParticipantB\x04\xc8\xde\x1f\x00"s\n\x14KeygenSessionRequest\x12[\n\x06key_id\x18\x01 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID"\xa4\x04\n\x15KeygenSessionResponse\x12\x12\n\nstarted_at\x18\x01 \x01(\x03\x12B\n\x14started_at_timestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x12\n\nexpires_at\x18\x03 \x01(\x03\x12\x14\n\x0ccompleted_at\x18\x04 \x01(\x03\x12\x14\n\x0cgrace_period\x18\x05 \x01(\x03\x12>\n\x05state\x18\x06 \x01(\x0e2/.axelar.multisig.exported.v1beta1.MultisigState\x12P\n\x17keygen_threshold_weight\x18\x07 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12Q\n\x18signing_threshold_weight\x18\x08 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12F\n\rbonded_weight\x18\t \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x12F\n\x0cparticipants\x18\n \x03(\x0b2*.axelar.multisig.v1beta1.KeygenParticipantB\x04\xc8\xde\x1f\x00B;Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00'
    _KEYIDRESPONSE.fields_by_name['key_id']._options = None
    _KEYIDRESPONSE.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _NEXTKEYIDRESPONSE.fields_by_name['key_id']._options = None
    _NEXTKEYIDRESPONSE.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYREQUEST.fields_by_name['key_id']._options = None
    _KEYREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYGENPARTICIPANT.fields_by_name['weight']._options = None
    _KEYGENPARTICIPANT.fields_by_name['weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _KEYRESPONSE.fields_by_name['key_id']._options = None
    _KEYRESPONSE.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYRESPONSE.fields_by_name['started_at_timestamp']._options = None
    _KEYRESPONSE.fields_by_name['started_at_timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _KEYRESPONSE.fields_by_name['threshold_weight']._options = None
    _KEYRESPONSE.fields_by_name['threshold_weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _KEYRESPONSE.fields_by_name['bonded_weight']._options = None
    _KEYRESPONSE.fields_by_name['bonded_weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _KEYRESPONSE.fields_by_name['participants']._options = None
    _KEYRESPONSE.fields_by_name['participants']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEYGENSESSIONREQUEST.fields_by_name['key_id']._options = None
    _KEYGENSESSIONREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYGENSESSIONRESPONSE.fields_by_name['started_at_timestamp']._options = None
    _KEYGENSESSIONRESPONSE.fields_by_name['started_at_timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _KEYGENSESSIONRESPONSE.fields_by_name['keygen_threshold_weight']._options = None
    _KEYGENSESSIONRESPONSE.fields_by_name['keygen_threshold_weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _KEYGENSESSIONRESPONSE.fields_by_name['signing_threshold_weight']._options = None
    _KEYGENSESSIONRESPONSE.fields_by_name['signing_threshold_weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _KEYGENSESSIONRESPONSE.fields_by_name['bonded_weight']._options = None
    _KEYGENSESSIONRESPONSE.fields_by_name['bonded_weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _KEYGENSESSIONRESPONSE.fields_by_name['participants']._options = None
    _KEYGENSESSIONRESPONSE.fields_by_name['participants']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_KEYIDREQUEST']._serialized_start = 240
    _globals['_KEYIDREQUEST']._serialized_end = 269
    _globals['_KEYIDRESPONSE']._serialized_start = 271
    _globals['_KEYIDRESPONSE']._serialized_end = 379
    _globals['_NEXTKEYIDREQUEST']._serialized_start = 381
    _globals['_NEXTKEYIDREQUEST']._serialized_end = 414
    _globals['_NEXTKEYIDRESPONSE']._serialized_start = 416
    _globals['_NEXTKEYIDRESPONSE']._serialized_end = 528
    _globals['_KEYREQUEST']._serialized_start = 530
    _globals['_KEYREQUEST']._serialized_end = 635
    _globals['_KEYGENPARTICIPANT']._serialized_start = 637
    _globals['_KEYGENPARTICIPANT']._serialized_end = 755
    _globals['_KEYRESPONSE']._serialized_start = 758
    _globals['_KEYRESPONSE']._serialized_end = 1230
    _globals['_KEYGENSESSIONREQUEST']._serialized_start = 1232
    _globals['_KEYGENSESSIONREQUEST']._serialized_end = 1347
    _globals['_KEYGENSESSIONRESPONSE']._serialized_start = 1350
    _globals['_KEYGENSESSIONRESPONSE']._serialized_end = 1898