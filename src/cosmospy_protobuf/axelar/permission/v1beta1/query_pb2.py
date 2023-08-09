"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos.crypto.multisig import keys_pb2 as cosmos_dot_crypto_dot_multisig_dot_keys__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%axelar/permission/v1beta1/query.proto\x12\x19axelar.permission.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!cosmos/crypto/multisig/keys.proto"\x1b\n\x19QueryGovernanceKeyRequest"e\n\x1aQueryGovernanceKeyResponse\x12G\n\x0egovernance_key\x18\x01 \x01(\x0b2).cosmos.crypto.multisig.LegacyAminoPubKeyB\x04\xc8\xde\x1f\x00B=Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.permission.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00'
    _QUERYGOVERNANCEKEYRESPONSE.fields_by_name['governance_key']._options = None
    _QUERYGOVERNANCEKEYRESPONSE.fields_by_name['governance_key']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYGOVERNANCEKEYREQUEST']._serialized_start = 158
    _globals['_QUERYGOVERNANCEKEYREQUEST']._serialized_end = 185
    _globals['_QUERYGOVERNANCEKEYRESPONSE']._serialized_start = 187
    _globals['_QUERYGOVERNANCEKEYRESPONSE']._serialized_end = 288