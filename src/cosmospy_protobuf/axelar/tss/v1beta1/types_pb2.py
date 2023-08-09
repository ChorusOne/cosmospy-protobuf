"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.tss.exported.v1beta1 import types_pb2 as axelar_dot_tss_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eaxelar/tss/v1beta1/types.proto\x12\x12axelar.tss.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\'axelar/tss/exported/v1beta1/types.proto">\n\x0eKeygenVoteData\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x1b\n\x13group_recovery_info\x18\x02 \x01(\x0c"\xd1\x01\n\x07KeyInfo\x12V\n\x06key_id\x18\x01 \x01(\tBF\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID\x126\n\x08key_role\x18\x02 \x01(\x0e2$.axelar.tss.exported.v1beta1.KeyRole\x126\n\x08key_type\x18\x03 \x01(\x0e2$.axelar.tss.exported.v1beta1.KeyType"\xdb\x01\n\x0cMultisigInfo\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID\x12\x0f\n\x07timeout\x18\x02 \x01(\x03\x12\x12\n\ntarget_num\x18\x03 \x01(\x03\x124\n\x05infos\x18\x04 \x03(\x0b2%.axelar.tss.v1beta1.MultisigInfo.Info\x1a\\\n\x04Info\x12F\n\x0bparticipant\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12\x0c\n\x04data\x18\x02 \x03(\x0c"\xf2\x01\n\x0fKeyRecoveryInfo\x12V\n\x06key_id\x18\x01 \x01(\tBF\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID\x12\x0e\n\x06public\x18\x02 \x01(\x0c\x12G\n\x07private\x18\x03 \x03(\x0b20.axelar.tss.v1beta1.KeyRecoveryInfo.PrivateEntryB\x04\xc8\xde\x1f\x00\x1a.\n\x0cPrivateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01"\xbc\x01\n\x0cExternalKeys\x12R\n\x05chain\x18\x01 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12X\n\x07key_ids\x18\x02 \x03(\tBG\xe2\xde\x1f\x06KeyIDs\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID"p\n\x0fValidatorStatus\x12D\n\tvalidator\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12\x17\n\x0fsuspended_until\x18\x02 \x01(\x04B2Z0github.com/axelarnetwork/axelar-core/x/tss/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/types'
    _KEYINFO.fields_by_name['key_id']._options = None
    _KEYINFO.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _MULTISIGINFO_INFO.fields_by_name['participant']._options = None
    _MULTISIGINFO_INFO.fields_by_name['participant']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _MULTISIGINFO.fields_by_name['id']._options = None
    _MULTISIGINFO.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _KEYRECOVERYINFO_PRIVATEENTRY._options = None
    _KEYRECOVERYINFO_PRIVATEENTRY._serialized_options = b'8\x01'
    _KEYRECOVERYINFO.fields_by_name['key_id']._options = None
    _KEYRECOVERYINFO.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _KEYRECOVERYINFO.fields_by_name['private']._options = None
    _KEYRECOVERYINFO.fields_by_name['private']._serialized_options = b'\xc8\xde\x1f\x00'
    _EXTERNALKEYS.fields_by_name['chain']._options = None
    _EXTERNALKEYS.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _EXTERNALKEYS.fields_by_name['key_ids']._options = None
    _EXTERNALKEYS.fields_by_name['key_ids']._serialized_options = b'\xe2\xde\x1f\x06KeyIDs\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _VALIDATORSTATUS.fields_by_name['validator']._options = None
    _VALIDATORSTATUS.fields_by_name['validator']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _globals['_KEYGENVOTEDATA']._serialized_start = 117
    _globals['_KEYGENVOTEDATA']._serialized_end = 179
    _globals['_KEYINFO']._serialized_start = 182
    _globals['_KEYINFO']._serialized_end = 391
    _globals['_MULTISIGINFO']._serialized_start = 394
    _globals['_MULTISIGINFO']._serialized_end = 613
    _globals['_MULTISIGINFO_INFO']._serialized_start = 521
    _globals['_MULTISIGINFO_INFO']._serialized_end = 613
    _globals['_KEYRECOVERYINFO']._serialized_start = 616
    _globals['_KEYRECOVERYINFO']._serialized_end = 858
    _globals['_KEYRECOVERYINFO_PRIVATEENTRY']._serialized_start = 812
    _globals['_KEYRECOVERYINFO_PRIVATEENTRY']._serialized_end = 858
    _globals['_EXTERNALKEYS']._serialized_start = 861
    _globals['_EXTERNALKEYS']._serialized_end = 1049
    _globals['_VALIDATORSTATUS']._serialized_start = 1051
    _globals['_VALIDATORSTATUS']._serialized_end = 1163