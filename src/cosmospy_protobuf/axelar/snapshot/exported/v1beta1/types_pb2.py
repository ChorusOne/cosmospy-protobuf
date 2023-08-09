"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....axelar.tss.exported.v1beta1 import types_pb2 as axelar_dot_tss_dot_exported_dot_v1beta1_dot_types__pb2
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,axelar/snapshot/exported/v1beta1/types.proto\x12 axelar.snapshot.exported.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\'axelar/tss/exported/v1beta1/types.proto\x1a\x19cosmos_proto/cosmos.proto\x1a$cosmos/staking/v1beta1/staking.proto"\x92\x01\n\x0bParticipant\x12B\n\x07address\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12?\n\x06weight\x18\x02 \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint"\xfd\x02\n\x08Snapshot\x127\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12X\n\x0cparticipants\x18\x08 \x03(\x0b2<.axelar.snapshot.exported.v1beta1.Snapshot.ParticipantsEntryB\x04\xc8\xde\x1f\x00\x12F\n\rbonded_weight\x18\t \x01(\x0cB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\x1ab\n\x11ParticipantsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.axelar.snapshot.exported.v1beta1.Participant:\x028\x01:\x04\x98\xa1\x1f\x01J\x04\x08\x01\x10\x02J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08B>Z8github.com/axelarnetwork/axelar-core/x/snapshot/exported\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.snapshot.exported.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/axelarnetwork/axelar-core/x/snapshot/exported\xc8\xe1\x1e\x00'
    _PARTICIPANT.fields_by_name['address']._options = None
    _PARTICIPANT.fields_by_name['address']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _PARTICIPANT.fields_by_name['weight']._options = None
    _PARTICIPANT.fields_by_name['weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _SNAPSHOT_PARTICIPANTSENTRY._options = None
    _SNAPSHOT_PARTICIPANTSENTRY._serialized_options = b'8\x01'
    _SNAPSHOT.fields_by_name['timestamp']._options = None
    _SNAPSHOT.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _SNAPSHOT.fields_by_name['participants']._options = None
    _SNAPSHOT.fields_by_name['participants']._serialized_options = b'\xc8\xde\x1f\x00'
    _SNAPSHOT.fields_by_name['bonded_weight']._options = None
    _SNAPSHOT.fields_by_name['bonded_weight']._serialized_options = b"\xc8\xde\x1f\x00\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Uint"
    _SNAPSHOT._options = None
    _SNAPSHOT._serialized_options = b'\x98\xa1\x1f\x01'
    _globals['_PARTICIPANT']._serialized_start = 303
    _globals['_PARTICIPANT']._serialized_end = 449
    _globals['_SNAPSHOT']._serialized_start = 452
    _globals['_SNAPSHOT']._serialized_end = 833
    _globals['_SNAPSHOT_PARTICIPANTSENTRY']._serialized_start = 699
    _globals['_SNAPSHOT_PARTICIPANTSENTRY']._serialized_end = 797