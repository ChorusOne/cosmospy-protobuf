"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
from ....axelar.evm.v1beta1 import types_pb2 as axelar_dot_evm_dot_v1beta1_dot_types__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.nexus.exported.v1beta1 import types_pb2 as axelar_dot_nexus_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1faxelar/evm/v1beta1/params.proto\x12\x12axelar.evm.v1beta1\x1a$axelar/utils/v1beta1/threshold.proto\x1a\x1eaxelar/evm/v1beta1/types.proto\x1a\x14gogoproto/gogo.proto\x1a)axelar/nexus/exported/v1beta1/types.proto"\xda\x03\n\x06Params\x12R\n\x05chain\x18\x01 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x1b\n\x13confirmation_height\x18\x02 \x01(\x04\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x12\n\ntoken_code\x18\x05 \x01(\x0c\x12\x10\n\x08burnable\x18\x06 \x01(\x0c\x12\x1d\n\x15revote_locking_period\x18\x07 \x01(\x03\x127\n\x08networks\x18\x08 \x03(\x0b2\x1f.axelar.evm.v1beta1.NetworkInfoB\x04\xc8\xde\x1f\x00\x12?\n\x10voting_threshold\x18\t \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12\x17\n\x0fmin_voter_count\x18\n \x01(\x03\x12\x1a\n\x12commands_gas_limit\x18\x0b \x01(\r\x12\x1b\n\x13voting_grace_period\x18\r \x01(\x03\x12\x19\n\x11end_blocker_limit\x18\x0e \x01(\x03\x12\x16\n\x0etransfer_limit\x18\x0f \x01(\x04J\x04\x08\x04\x10\x05J\x04\x08\x0c\x10\r"{\n\x0cPendingChain\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.axelar.evm.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x129\n\x05chain\x18\x02 \x01(\x0b2$.axelar.nexus.exported.v1beta1.ChainB\x04\xc8\xde\x1f\x00B6Z0github.com/axelarnetwork/axelar-core/x/evm/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.evm.v1beta1.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/evm/types\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['chain']._options = None
    _PARAMS.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _PARAMS.fields_by_name['networks']._options = None
    _PARAMS.fields_by_name['networks']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['voting_threshold']._options = None
    _PARAMS.fields_by_name['voting_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _PENDINGCHAIN.fields_by_name['params']._options = None
    _PENDINGCHAIN.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _PENDINGCHAIN.fields_by_name['chain']._options = None
    _PENDINGCHAIN.fields_by_name['chain']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS']._serialized_start = 191
    _globals['_PARAMS']._serialized_end = 665
    _globals['_PENDINGCHAIN']._serialized_start = 667
    _globals['_PENDINGCHAIN']._serialized_end = 790