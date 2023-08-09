"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
from ....axelar.tss.exported.v1beta1 import types_pb2 as axelar_dot_tss_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1faxelar/tss/v1beta1/params.proto\x12\x12axelar.tss.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$axelar/utils/v1beta1/threshold.proto\x1a\'axelar/tss/exported/v1beta1/types.proto"\xc9\x03\n\x06Params\x12K\n\x10key_requirements\x18\x01 \x03(\x0b2+.axelar.tss.exported.v1beta1.KeyRequirementB\x04\xc8\xde\x1f\x00\x12"\n\x1asuspend_duration_in_blocks\x18\x02 \x01(\x03\x12"\n\x1aheartbeat_period_in_blocks\x18\x03 \x01(\x03\x12K\n\x1cmax_missed_blocks_per_window\x18\x04 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12,\n$unbonding_locking_key_rotation_count\x18\x05 \x01(\x03\x12J\n\x1bexternal_multisig_threshold\x18\x06 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13max_sign_queue_size\x18\x07 \x01(\x03\x12$\n\x1cmax_simultaneous_sign_shares\x18\x08 \x01(\x03\x12 \n\x18tss_signed_blocks_window\x18\t \x01(\x03B6Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.v1beta1.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['key_requirements']._options = None
    _PARAMS.fields_by_name['key_requirements']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['max_missed_blocks_per_window']._options = None
    _PARAMS.fields_by_name['max_missed_blocks_per_window']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['external_multisig_threshold']._options = None
    _PARAMS.fields_by_name['external_multisig_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS']._serialized_start = 157
    _globals['_PARAMS']._serialized_end = 614