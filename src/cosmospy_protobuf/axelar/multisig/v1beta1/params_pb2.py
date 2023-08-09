"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$axelar/multisig/v1beta1/params.proto\x12\x17axelar.multisig.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$axelar/utils/v1beta1/threshold.proto"\x93\x02\n\x06Params\x12?\n\x10keygen_threshold\x18\x01 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12@\n\x11signing_threshold\x18\x02 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12\x16\n\x0ekeygen_timeout\x18\x03 \x01(\x03\x12\x1b\n\x13keygen_grace_period\x18\x04 \x01(\x03\x12\x17\n\x0fsigning_timeout\x18\x05 \x01(\x03\x12\x1c\n\x14signing_grace_period\x18\x06 \x01(\x03\x12\x1a\n\x12active_epoch_count\x18\x07 \x01(\x04B;Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['keygen_threshold']._options = None
    _PARAMS.fields_by_name['keygen_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['signing_threshold']._options = None
    _PARAMS.fields_by_name['signing_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS']._serialized_start = 126
    _globals['_PARAMS']._serialized_end = 401