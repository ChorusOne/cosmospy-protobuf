"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'axelar/tss/exported/v1beta1/types.proto\x12\x1baxelar.tss.exported.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19cosmos_proto/cosmos.proto\x1a$axelar/utils/v1beta1/threshold.proto\x1a\x14gogoproto/gogo.proto"\xe0\x04\n\x0eKeyRequirement\x126\n\x08key_role\x18\x01 \x01(\x0e2$.axelar.tss.exported.v1beta1.KeyRole\x126\n\x08key_type\x18\x02 \x01(\x0e2$.axelar.tss.exported.v1beta1.KeyType\x12C\n\x14min_keygen_threshold\x18\x03 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12?\n\x10safety_threshold\x18\x04 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12^\n\x1dkey_share_distribution_policy\x18\x05 \x01(\x0e27.axelar.tss.exported.v1beta1.KeyShareDistributionPolicy\x12\x1d\n\x15max_total_share_count\x18\x06 \x01(\x03\x12\x1d\n\x15min_total_share_count\x18\x07 \x01(\x03\x12F\n\x17keygen_voting_threshold\x18\x08 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12D\n\x15sign_voting_threshold\x18\t \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12\x16\n\x0ekeygen_timeout\x18\n \x01(\x03\x12\x14\n\x0csign_timeout\x18\x0b \x01(\x03"0\n\nSigKeyPair\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c*\xbc\x01\n\x07KeyRole\x12%\n\x14KEY_ROLE_UNSPECIFIED\x10\x00\x1a\x0b\x8a\x9d \x07Unknown\x12&\n\x13KEY_ROLE_MASTER_KEY\x10\x01\x1a\r\x8a\x9d \tMasterKey\x12,\n\x16KEY_ROLE_SECONDARY_KEY\x10\x02\x1a\x10\x8a\x9d \x0cSecondaryKey\x12*\n\x15KEY_ROLE_EXTERNAL_KEY\x10\x03\x1a\x0f\x8a\x9d \x0bExternalKey\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01*\x96\x01\n\x07KeyType\x12\x18\n\x14KEY_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\rKEY_TYPE_NONE\x10\x01\x1a\x08\x8a\x9d \x04None\x12%\n\x12KEY_TYPE_THRESHOLD\x10\x02\x1a\r\x8a\x9d \tThreshold\x12#\n\x11KEY_TYPE_MULTISIG\x10\x03\x1a\x0c\x8a\x9d \x08Multisig\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01*\xfa\x01\n\x1aKeyShareDistributionPolicy\x12>\n)KEY_SHARE_DISTRIBUTION_POLICY_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12H\n/KEY_SHARE_DISTRIBUTION_POLICY_WEIGHTED_BY_STAKE\x10\x01\x1a\x13\x8a\x9d \x0fWeightedByStake\x12H\n/KEY_SHARE_DISTRIBUTION_POLICY_ONE_PER_VALIDATOR\x10\x02\x1a\x13\x8a\x9d \x0fOnePerValidator\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01B5Z3github.com/axelarnetwork/axelar-core/x/tss/exportedb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.exported.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z3github.com/axelarnetwork/axelar-core/x/tss/exported'
    _KEYROLE._options = None
    _KEYROLE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _KEYROLE.values_by_name['KEY_ROLE_UNSPECIFIED']._options = None
    _KEYROLE.values_by_name['KEY_ROLE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x07Unknown'
    _KEYROLE.values_by_name['KEY_ROLE_MASTER_KEY']._options = None
    _KEYROLE.values_by_name['KEY_ROLE_MASTER_KEY']._serialized_options = b'\x8a\x9d \tMasterKey'
    _KEYROLE.values_by_name['KEY_ROLE_SECONDARY_KEY']._options = None
    _KEYROLE.values_by_name['KEY_ROLE_SECONDARY_KEY']._serialized_options = b'\x8a\x9d \x0cSecondaryKey'
    _KEYROLE.values_by_name['KEY_ROLE_EXTERNAL_KEY']._options = None
    _KEYROLE.values_by_name['KEY_ROLE_EXTERNAL_KEY']._serialized_options = b'\x8a\x9d \x0bExternalKey'
    _KEYTYPE._options = None
    _KEYTYPE._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _KEYTYPE.values_by_name['KEY_TYPE_NONE']._options = None
    _KEYTYPE.values_by_name['KEY_TYPE_NONE']._serialized_options = b'\x8a\x9d \x04None'
    _KEYTYPE.values_by_name['KEY_TYPE_THRESHOLD']._options = None
    _KEYTYPE.values_by_name['KEY_TYPE_THRESHOLD']._serialized_options = b'\x8a\x9d \tThreshold'
    _KEYTYPE.values_by_name['KEY_TYPE_MULTISIG']._options = None
    _KEYTYPE.values_by_name['KEY_TYPE_MULTISIG']._serialized_options = b'\x8a\x9d \x08Multisig'
    _KEYSHAREDISTRIBUTIONPOLICY._options = None
    _KEYSHAREDISTRIBUTIONPOLICY._serialized_options = b'\x88\xa3\x1e\x00\xa8\xa4\x1e\x01'
    _KEYSHAREDISTRIBUTIONPOLICY.values_by_name['KEY_SHARE_DISTRIBUTION_POLICY_UNSPECIFIED']._options = None
    _KEYSHAREDISTRIBUTIONPOLICY.values_by_name['KEY_SHARE_DISTRIBUTION_POLICY_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bUnspecified'
    _KEYSHAREDISTRIBUTIONPOLICY.values_by_name['KEY_SHARE_DISTRIBUTION_POLICY_WEIGHTED_BY_STAKE']._options = None
    _KEYSHAREDISTRIBUTIONPOLICY.values_by_name['KEY_SHARE_DISTRIBUTION_POLICY_WEIGHTED_BY_STAKE']._serialized_options = b'\x8a\x9d \x0fWeightedByStake'
    _KEYSHAREDISTRIBUTIONPOLICY.values_by_name['KEY_SHARE_DISTRIBUTION_POLICY_ONE_PER_VALIDATOR']._options = None
    _KEYSHAREDISTRIBUTIONPOLICY.values_by_name['KEY_SHARE_DISTRIBUTION_POLICY_ONE_PER_VALIDATOR']._serialized_options = b'\x8a\x9d \x0fOnePerValidator'
    _KEYREQUIREMENT.fields_by_name['min_keygen_threshold']._options = None
    _KEYREQUIREMENT.fields_by_name['min_keygen_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEYREQUIREMENT.fields_by_name['safety_threshold']._options = None
    _KEYREQUIREMENT.fields_by_name['safety_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEYREQUIREMENT.fields_by_name['keygen_voting_threshold']._options = None
    _KEYREQUIREMENT.fields_by_name['keygen_voting_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEYREQUIREMENT.fields_by_name['sign_voting_threshold']._options = None
    _KEYREQUIREMENT.fields_by_name['sign_voting_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_KEYROLE']._serialized_start = 881
    _globals['_KEYROLE']._serialized_end = 1069
    _globals['_KEYTYPE']._serialized_start = 1072
    _globals['_KEYTYPE']._serialized_end = 1222
    _globals['_KEYSHAREDISTRIBUTIONPOLICY']._serialized_start = 1225
    _globals['_KEYSHAREDISTRIBUTIONPOLICY']._serialized_end = 1475
    _globals['_KEYREQUIREMENT']._serialized_start = 220
    _globals['_KEYREQUIREMENT']._serialized_end = 828
    _globals['_SIGKEYPAIR']._serialized_start = 830
    _globals['_SIGKEYPAIR']._serialized_end = 878