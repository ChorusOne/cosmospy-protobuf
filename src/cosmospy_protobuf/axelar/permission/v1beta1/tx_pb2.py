"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.crypto.multisig import keys_pb2 as cosmos_dot_crypto_dot_multisig_dot_keys__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"axelar/permission/v1beta1/tx.proto\x12\x19axelar.permission.v1beta1\x1a\x14gogoproto/gogo.proto\x1a!cosmos/crypto/multisig/keys.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\xae\x01\n\x1aUpdateGovernanceKeyRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12G\n\x0egovernance_key\x18\x02 \x01(\x0b2).cosmos.crypto.multisig.LegacyAminoPubKeyB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x03"\x1d\n\x1bUpdateGovernanceKeyResponse"\xab\x01\n\x19RegisterControllerRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12E\n\ncontroller\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x03"\x1c\n\x1aRegisterControllerResponse"\xad\x01\n\x1bDeregisterControllerRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12E\n\ncontroller\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x03"\x1e\n\x1cDeregisterControllerResponseB=Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.permission.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/axelarnetwork/axelar-core/x/permission/types\xc8\xe1\x1e\x00'
    _UPDATEGOVERNANCEKEYREQUEST.fields_by_name['sender']._options = None
    _UPDATEGOVERNANCEKEYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _UPDATEGOVERNANCEKEYREQUEST.fields_by_name['governance_key']._options = None
    _UPDATEGOVERNANCEKEYREQUEST.fields_by_name['governance_key']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPDATEGOVERNANCEKEYREQUEST._options = None
    _UPDATEGOVERNANCEKEYREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _REGISTERCONTROLLERREQUEST.fields_by_name['sender']._options = None
    _REGISTERCONTROLLERREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERCONTROLLERREQUEST.fields_by_name['controller']._options = None
    _REGISTERCONTROLLERREQUEST.fields_by_name['controller']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERCONTROLLERREQUEST._options = None
    _REGISTERCONTROLLERREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _DEREGISTERCONTROLLERREQUEST.fields_by_name['sender']._options = None
    _DEREGISTERCONTROLLERREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _DEREGISTERCONTROLLERREQUEST.fields_by_name['controller']._options = None
    _DEREGISTERCONTROLLERREQUEST.fields_by_name['controller']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _DEREGISTERCONTROLLERREQUEST._options = None
    _DEREGISTERCONTROLLERREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _globals['_UPDATEGOVERNANCEKEYREQUEST']._serialized_start = 171
    _globals['_UPDATEGOVERNANCEKEYREQUEST']._serialized_end = 345
    _globals['_UPDATEGOVERNANCEKEYRESPONSE']._serialized_start = 347
    _globals['_UPDATEGOVERNANCEKEYRESPONSE']._serialized_end = 376
    _globals['_REGISTERCONTROLLERREQUEST']._serialized_start = 379
    _globals['_REGISTERCONTROLLERREQUEST']._serialized_end = 550
    _globals['_REGISTERCONTROLLERRESPONSE']._serialized_start = 552
    _globals['_REGISTERCONTROLLERRESPONSE']._serialized_end = 580
    _globals['_DEREGISTERCONTROLLERREQUEST']._serialized_start = 583
    _globals['_DEREGISTERCONTROLLERREQUEST']._serialized_end = 756
    _globals['_DEREGISTERCONTROLLERRESPONSE']._serialized_start = 758
    _globals['_DEREGISTERCONTROLLERRESPONSE']._serialized_end = 788