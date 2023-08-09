"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.tss.v1beta1 import params_pb2 as axelar_dot_tss_dot_v1beta1_dot_params__pb2
from ....axelar.tss.v1beta1 import types_pb2 as axelar_dot_tss_dot_v1beta1_dot_types__pb2
from ....axelar.tss.exported.v1beta1 import types_pb2 as axelar_dot_tss_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/tss/v1beta1/genesis.proto\x12\x12axelar.tss.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1faxelar/tss/v1beta1/params.proto\x1a\x1eaxelar/tss/v1beta1/types.proto\x1a\'axelar/tss/exported/v1beta1/types.proto"@\n\x0cGenesisState\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.axelar.tss.v1beta1.ParamsB\x04\xc8\xde\x1f\x00B6Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc8\xe1\x1e\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 184
    _globals['_GENESISSTATE']._serialized_end = 248