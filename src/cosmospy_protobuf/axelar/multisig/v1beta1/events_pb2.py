"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$axelar/multisig/v1beta1/events.proto\x12\x17axelar.multisig.v1beta1\x1a\x14gogoproto/gogo.proto"\xc5\x01\n\rKeygenStarted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12[\n\x06key_id\x18\x02 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x12G\n\x0cparticipants\x18\x03 \x03(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress"\x84\x01\n\x0fKeygenCompleted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12[\n\x06key_id\x18\x02 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID:\x04\x88\xa2\x1f\x01"\x82\x01\n\rKeygenExpired\x12\x0e\n\x06module\x18\x01 \x01(\t\x12[\n\x06key_id\x18\x02 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID:\x04\x88\xa2\x1f\x01"\x9f\x02\n\x0fPubKeySubmitted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12[\n\x06key_id\x18\x02 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x12F\n\x0bparticipant\x18\x03 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12W\n\x07pub_key\x18\x04 \x01(\x0cBF\xfa\xde\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey"\xd3\x03\n\x0eSigningStarted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x19\n\x06sig_id\x18\x02 \x01(\x04B\t\xe2\xde\x1f\x05SigID\x12[\n\x06key_id\x18\x03 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x12\x8e\x01\n\x08pub_keys\x18\x04 \x03(\x0b24.axelar.multisig.v1beta1.SigningStarted.PubKeysEntryBF\x8a\xdf\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey\x12W\n\x0cpayload_hash\x18\x05 \x01(\x0cBA\xfa\xde\x1f=github.com/axelarnetwork/axelar-core/x/multisig/exported.Hash\x12\x19\n\x11requesting_module\x18\x06 \x01(\t\x1a.\n\x0cPubKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01:\x04\x98\xa1\x1f\x01"=\n\x10SigningCompleted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x19\n\x06sig_id\x18\x02 \x01(\x04B\t\xe2\xde\x1f\x05SigID";\n\x0eSigningExpired\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x19\n\x06sig_id\x18\x02 \x01(\x04B\t\xe2\xde\x1f\x05SigID"\xa9\x01\n\x12SignatureSubmitted\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x19\n\x06sig_id\x18\x02 \x01(\x04B\t\xe2\xde\x1f\x05SigID\x12F\n\x0bparticipant\x18\x03 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x12 \n\tsignature\x18\x04 \x01(\x0cB\r\xfa\xde\x1f\tSignature"\xce\x01\n\x0bKeyAssigned\x12\x0e\n\x06module\x18\x01 \x01(\t\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12[\n\x06key_id\x18\x03 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID"\xcd\x01\n\nKeyRotated\x12\x0e\n\x06module\x18\x01 \x01(\t\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12[\n\x06key_id\x18\x03 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID"V\n\x0cKeygenOptOut\x12F\n\x0bparticipant\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress"U\n\x0bKeygenOptIn\x12F\n\x0bparticipant\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddressB7Z5github.com/axelarnetwork/axelar-core/x/multisig/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types'
    _KEYGENSTARTED.fields_by_name['key_id']._options = None
    _KEYGENSTARTED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYGENSTARTED.fields_by_name['participants']._options = None
    _KEYGENSTARTED.fields_by_name['participants']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _KEYGENCOMPLETED.fields_by_name['key_id']._options = None
    _KEYGENCOMPLETED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYGENCOMPLETED._options = None
    _KEYGENCOMPLETED._serialized_options = b'\x88\xa2\x1f\x01'
    _KEYGENEXPIRED.fields_by_name['key_id']._options = None
    _KEYGENEXPIRED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYGENEXPIRED._options = None
    _KEYGENEXPIRED._serialized_options = b'\x88\xa2\x1f\x01'
    _PUBKEYSUBMITTED.fields_by_name['key_id']._options = None
    _PUBKEYSUBMITTED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _PUBKEYSUBMITTED.fields_by_name['participant']._options = None
    _PUBKEYSUBMITTED.fields_by_name['participant']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _PUBKEYSUBMITTED.fields_by_name['pub_key']._options = None
    _PUBKEYSUBMITTED.fields_by_name['pub_key']._serialized_options = b'\xfa\xde\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey'
    _SIGNINGSTARTED_PUBKEYSENTRY._options = None
    _SIGNINGSTARTED_PUBKEYSENTRY._serialized_options = b'8\x01'
    _SIGNINGSTARTED.fields_by_name['sig_id']._options = None
    _SIGNINGSTARTED.fields_by_name['sig_id']._serialized_options = b'\xe2\xde\x1f\x05SigID'
    _SIGNINGSTARTED.fields_by_name['key_id']._options = None
    _SIGNINGSTARTED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _SIGNINGSTARTED.fields_by_name['pub_keys']._options = None
    _SIGNINGSTARTED.fields_by_name['pub_keys']._serialized_options = b'\x8a\xdf\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey'
    _SIGNINGSTARTED.fields_by_name['payload_hash']._options = None
    _SIGNINGSTARTED.fields_by_name['payload_hash']._serialized_options = b'\xfa\xde\x1f=github.com/axelarnetwork/axelar-core/x/multisig/exported.Hash'
    _SIGNINGSTARTED._options = None
    _SIGNINGSTARTED._serialized_options = b'\x98\xa1\x1f\x01'
    _SIGNINGCOMPLETED.fields_by_name['sig_id']._options = None
    _SIGNINGCOMPLETED.fields_by_name['sig_id']._serialized_options = b'\xe2\xde\x1f\x05SigID'
    _SIGNINGEXPIRED.fields_by_name['sig_id']._options = None
    _SIGNINGEXPIRED.fields_by_name['sig_id']._serialized_options = b'\xe2\xde\x1f\x05SigID'
    _SIGNATURESUBMITTED.fields_by_name['sig_id']._options = None
    _SIGNATURESUBMITTED.fields_by_name['sig_id']._serialized_options = b'\xe2\xde\x1f\x05SigID'
    _SIGNATURESUBMITTED.fields_by_name['participant']._options = None
    _SIGNATURESUBMITTED.fields_by_name['participant']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _SIGNATURESUBMITTED.fields_by_name['signature']._options = None
    _SIGNATURESUBMITTED.fields_by_name['signature']._serialized_options = b'\xfa\xde\x1f\tSignature'
    _KEYASSIGNED.fields_by_name['chain']._options = None
    _KEYASSIGNED.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _KEYASSIGNED.fields_by_name['key_id']._options = None
    _KEYASSIGNED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYROTATED.fields_by_name['chain']._options = None
    _KEYROTATED.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _KEYROTATED.fields_by_name['key_id']._options = None
    _KEYROTATED.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEYGENOPTOUT.fields_by_name['participant']._options = None
    _KEYGENOPTOUT.fields_by_name['participant']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _KEYGENOPTIN.fields_by_name['participant']._options = None
    _KEYGENOPTIN.fields_by_name['participant']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _globals['_KEYGENSTARTED']._serialized_start = 88
    _globals['_KEYGENSTARTED']._serialized_end = 285
    _globals['_KEYGENCOMPLETED']._serialized_start = 288
    _globals['_KEYGENCOMPLETED']._serialized_end = 420
    _globals['_KEYGENEXPIRED']._serialized_start = 423
    _globals['_KEYGENEXPIRED']._serialized_end = 553
    _globals['_PUBKEYSUBMITTED']._serialized_start = 556
    _globals['_PUBKEYSUBMITTED']._serialized_end = 843
    _globals['_SIGNINGSTARTED']._serialized_start = 846
    _globals['_SIGNINGSTARTED']._serialized_end = 1313
    _globals['_SIGNINGSTARTED_PUBKEYSENTRY']._serialized_start = 1261
    _globals['_SIGNINGSTARTED_PUBKEYSENTRY']._serialized_end = 1307
    _globals['_SIGNINGCOMPLETED']._serialized_start = 1315
    _globals['_SIGNINGCOMPLETED']._serialized_end = 1376
    _globals['_SIGNINGEXPIRED']._serialized_start = 1378
    _globals['_SIGNINGEXPIRED']._serialized_end = 1437
    _globals['_SIGNATURESUBMITTED']._serialized_start = 1440
    _globals['_SIGNATURESUBMITTED']._serialized_end = 1609
    _globals['_KEYASSIGNED']._serialized_start = 1612
    _globals['_KEYASSIGNED']._serialized_end = 1818
    _globals['_KEYROTATED']._serialized_start = 1821
    _globals['_KEYROTATED']._serialized_end = 2026
    _globals['_KEYGENOPTOUT']._serialized_start = 2028
    _globals['_KEYGENOPTOUT']._serialized_end = 2114
    _globals['_KEYGENOPTIN']._serialized_start = 2116
    _globals['_KEYGENOPTIN']._serialized_end = 2201