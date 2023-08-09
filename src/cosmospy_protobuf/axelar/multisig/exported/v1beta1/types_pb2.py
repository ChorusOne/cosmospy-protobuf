"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n,axelar/multisig/exported/v1beta1/types.proto\x12 axelar.multisig.exported.v1beta1\x1a\x14gogoproto/gogo.proto*\xa0\x01\n\rMultisigState\x12/\n\x1aMULTISIG_STATE_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bNonExistent\x12'\n\x16MULTISIG_STATE_PENDING\x10\x01\x1a\x0b\x8a\x9d \x07Pending\x12+\n\x18MULTISIG_STATE_COMPLETED\x10\x02\x1a\r\x8a\x9d \tCompleted\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01*\x85\x01\n\x08KeyState\x12'\n\x15KEY_STATE_UNSPECIFIED\x10\x00\x1a\x0c\x8a\x9d \x08Inactive\x12$\n\x12KEY_STATE_ASSIGNED\x10\x01\x1a\x0c\x8a\x9d \x08Assigned\x12 \n\x10KEY_STATE_ACTIVE\x10\x02\x1a\n\x8a\x9d \x06Active\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01B>Z8github.com/axelarnetwork/axelar-core/x/multisig/exported\xc8\xe1\x1e\x00b\x06proto3")
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.exported.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/axelarnetwork/axelar-core/x/multisig/exported\xc8\xe1\x1e\x00'
    _MULTISIGSTATE._options = None
    _MULTISIGSTATE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _MULTISIGSTATE.values_by_name['MULTISIG_STATE_UNSPECIFIED']._options = None
    _MULTISIGSTATE.values_by_name['MULTISIG_STATE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bNonExistent'
    _MULTISIGSTATE.values_by_name['MULTISIG_STATE_PENDING']._options = None
    _MULTISIGSTATE.values_by_name['MULTISIG_STATE_PENDING']._serialized_options = b'\x8a\x9d \x07Pending'
    _MULTISIGSTATE.values_by_name['MULTISIG_STATE_COMPLETED']._options = None
    _MULTISIGSTATE.values_by_name['MULTISIG_STATE_COMPLETED']._serialized_options = b'\x8a\x9d \tCompleted'
    _KEYSTATE._options = None
    _KEYSTATE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _KEYSTATE.values_by_name['KEY_STATE_UNSPECIFIED']._options = None
    _KEYSTATE.values_by_name['KEY_STATE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x08Inactive'
    _KEYSTATE.values_by_name['KEY_STATE_ASSIGNED']._options = None
    _KEYSTATE.values_by_name['KEY_STATE_ASSIGNED']._serialized_options = b'\x8a\x9d \x08Assigned'
    _KEYSTATE.values_by_name['KEY_STATE_ACTIVE']._options = None
    _KEYSTATE.values_by_name['KEY_STATE_ACTIVE']._serialized_options = b'\x8a\x9d \x06Active'
    _globals['_MULTISIGSTATE']._serialized_start = 105
    _globals['_MULTISIGSTATE']._serialized_end = 265
    _globals['_KEYSTATE']._serialized_start = 268
    _globals['_KEYSTATE']._serialized_end = 401