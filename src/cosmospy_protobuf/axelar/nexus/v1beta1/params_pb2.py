"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/nexus/v1beta1/params.proto\x12\x14axelar.nexus.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$axelar/utils/v1beta1/threshold.proto"\xac\x02\n\x06Params\x12I\n\x1achain_activation_threshold\x18\x01 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12V\n\'chain_maintainer_missing_vote_threshold\x18\x02 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12X\n)chain_maintainer_incorrect_vote_threshold\x18\x03 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12%\n\x1dchain_maintainer_check_window\x18\x04 \x01(\x05B8Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.v1beta1.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['chain_activation_threshold']._options = None
    _PARAMS.fields_by_name['chain_activation_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['chain_maintainer_missing_vote_threshold']._options = None
    _PARAMS.fields_by_name['chain_maintainer_missing_vote_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['chain_maintainer_incorrect_vote_threshold']._options = None
    _PARAMS.fields_by_name['chain_maintainer_incorrect_vote_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS']._serialized_start = 120
    _globals['_PARAMS']._serialized_end = 420