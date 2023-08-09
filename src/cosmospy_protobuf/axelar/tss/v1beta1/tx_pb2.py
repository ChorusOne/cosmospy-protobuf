"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.tss.exported.v1beta1 import types_pb2 as axelar_dot_tss_dot_exported_dot_v1beta1_dot_types__pb2
from ....axelar.tss.v1beta1 import types_pb2 as axelar_dot_tss_dot_v1beta1_dot_types__pb2
from ....axelar.tss.tofnd.v1beta1 import tofnd_pb2 as axelar_dot_tss_dot_tofnd_dot_v1beta1_dot_tofnd__pb2
from ....axelar.vote.exported.v1beta1 import types_pb2 as axelar_dot_vote_dot_exported_dot_v1beta1_dot_types__pb2
from ....cosmos.crypto.multisig import keys_pb2 as cosmos_dot_crypto_dot_multisig_dot_keys__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1baxelar/tss/v1beta1/tx.proto\x12\x12axelar.tss.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\'axelar/tss/exported/v1beta1/types.proto\x1a\x1eaxelar/tss/v1beta1/types.proto\x1a$axelar/tss/tofnd/v1beta1/tofnd.proto\x1a(axelar/vote/exported/v1beta1/types.proto\x1a!cosmos/crypto/multisig/keys.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\x92\x01\n\x12StartKeygenRequest\x12A\n\x06sender\x18\x01 \x01(\tB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x123\n\x08key_info\x18\x02 \x01(\x0b2\x1b.axelar.tss.v1beta1.KeyInfoB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x02"\x15\n\x13StartKeygenResponse"\xbf\x02\n\x10RotateKeyRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x126\n\x08key_role\x18\x03 \x01(\x0e2$.axelar.tss.exported.v1beta1.KeyRole\x12V\n\x06key_id\x18\x04 \x01(\tBF\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID:\x04\x80\xb5\x18\x02"\x13\n\x11RotateKeyResponse"\xc6\x01\n\x1bProcessKeygenTrafficRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12!\n\nsession_id\x18\x02 \x01(\tB\r\xe2\xde\x1f\tSessionID\x12;\n\x07payload\x18\x03 \x01(\x0b2$.axelar.tss.tofnd.v1beta1.TrafficOutB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x01"\x1e\n\x1cProcessKeygenTrafficResponse"\xc4\x01\n\x19ProcessSignTrafficRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12!\n\nsession_id\x18\x02 \x01(\tB\r\xe2\xde\x1f\tSessionID\x12;\n\x07payload\x18\x03 \x01(\x0b2$.axelar.tss.tofnd.v1beta1.TrafficOutB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x01"\x1c\n\x1aProcessSignTrafficResponse"\xe4\x01\n\x11VotePubKeyRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12=\n\x08poll_key\x18\x02 \x01(\x0b2%.axelar.vote.exported.v1beta1.PollKeyB\x04\xc8\xde\x1f\x00\x12G\n\x06result\x18\x03 \x01(\x0b21.axelar.tss.tofnd.v1beta1.MessageOut.KeygenResultB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x01"!\n\x12VotePubKeyResponse\x12\x0b\n\x03log\x18\x01 \x01(\t"\xdf\x01\n\x0eVoteSigRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12=\n\x08poll_key\x18\x02 \x01(\x0b2%.axelar.vote.exported.v1beta1.PollKeyB\x04\xc8\xde\x1f\x00\x12E\n\x06result\x18\x03 \x01(\x0b2/.axelar.tss.tofnd.v1beta1.MessageOut.SignResultB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x01"\x1e\n\x0fVoteSigResponse\x12\x0b\n\x03log\x18\x01 \x01(\t"\xb5\x01\n\x10HeartBeatRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12X\n\x07key_ids\x18\x02 \x03(\tBG\xe2\xde\x1f\x06KeyIDs\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID:\x04\x80\xb5\x18\x01"\x13\n\x11HeartBeatResponse"\x85\x03\n\x1bRegisterExternalKeysRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12X\n\rexternal_keys\x18\x03 \x03(\x0b2;.axelar.tss.v1beta1.RegisterExternalKeysRequest.ExternalKeyB\x04\xc8\xde\x1f\x00\x1ao\n\x0bExternalKey\x12O\n\x02id\x18\x01 \x01(\tBC\xe2\xde\x1f\x02ID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID\x12\x0f\n\x07pub_key\x18\x02 \x01(\x0c:\x04\x80\xb5\x18\x02"\x1e\n\x1cRegisterExternalKeysResponse"\x85\x02\n\x1cSubmitMultisigPubKeysRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12V\n\x06key_id\x18\x02 \x01(\tBF\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID\x12D\n\rsig_key_pairs\x18\x03 \x03(\x0b2\'.axelar.tss.exported.v1beta1.SigKeyPairB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x01"\x1f\n\x1dSubmitMultisigPubKeysResponse"\x99\x01\n\x1fSubmitMultisigSignaturesRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x19\n\x06sig_id\x18\x02 \x01(\tB\t\xe2\xde\x1f\x05SigID\x12\x12\n\nsignatures\x18\x03 \x03(\x0c:\x04\x80\xb5\x18\x01""\n SubmitMultisigSignaturesResponseB6Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/types\xc8\xe1\x1e\x00'
    _STARTKEYGENREQUEST.fields_by_name['sender']._options = None
    _STARTKEYGENREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _STARTKEYGENREQUEST.fields_by_name['key_info']._options = None
    _STARTKEYGENREQUEST.fields_by_name['key_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _STARTKEYGENREQUEST._options = None
    _STARTKEYGENREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _ROTATEKEYREQUEST.fields_by_name['sender']._options = None
    _ROTATEKEYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _ROTATEKEYREQUEST.fields_by_name['chain']._options = None
    _ROTATEKEYREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _ROTATEKEYREQUEST.fields_by_name['key_id']._options = None
    _ROTATEKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _ROTATEKEYREQUEST._options = None
    _ROTATEKEYREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _PROCESSKEYGENTRAFFICREQUEST.fields_by_name['sender']._options = None
    _PROCESSKEYGENTRAFFICREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _PROCESSKEYGENTRAFFICREQUEST.fields_by_name['session_id']._options = None
    _PROCESSKEYGENTRAFFICREQUEST.fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _PROCESSKEYGENTRAFFICREQUEST.fields_by_name['payload']._options = None
    _PROCESSKEYGENTRAFFICREQUEST.fields_by_name['payload']._serialized_options = b'\xc8\xde\x1f\x00'
    _PROCESSKEYGENTRAFFICREQUEST._options = None
    _PROCESSKEYGENTRAFFICREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _PROCESSSIGNTRAFFICREQUEST.fields_by_name['sender']._options = None
    _PROCESSSIGNTRAFFICREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _PROCESSSIGNTRAFFICREQUEST.fields_by_name['session_id']._options = None
    _PROCESSSIGNTRAFFICREQUEST.fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _PROCESSSIGNTRAFFICREQUEST.fields_by_name['payload']._options = None
    _PROCESSSIGNTRAFFICREQUEST.fields_by_name['payload']._serialized_options = b'\xc8\xde\x1f\x00'
    _PROCESSSIGNTRAFFICREQUEST._options = None
    _PROCESSSIGNTRAFFICREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _VOTEPUBKEYREQUEST.fields_by_name['sender']._options = None
    _VOTEPUBKEYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _VOTEPUBKEYREQUEST.fields_by_name['poll_key']._options = None
    _VOTEPUBKEYREQUEST.fields_by_name['poll_key']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTEPUBKEYREQUEST.fields_by_name['result']._options = None
    _VOTEPUBKEYREQUEST.fields_by_name['result']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTEPUBKEYREQUEST._options = None
    _VOTEPUBKEYREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _VOTESIGREQUEST.fields_by_name['sender']._options = None
    _VOTESIGREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _VOTESIGREQUEST.fields_by_name['poll_key']._options = None
    _VOTESIGREQUEST.fields_by_name['poll_key']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTESIGREQUEST.fields_by_name['result']._options = None
    _VOTESIGREQUEST.fields_by_name['result']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTESIGREQUEST._options = None
    _VOTESIGREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _HEARTBEATREQUEST.fields_by_name['sender']._options = None
    _HEARTBEATREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _HEARTBEATREQUEST.fields_by_name['key_ids']._options = None
    _HEARTBEATREQUEST.fields_by_name['key_ids']._serialized_options = b'\xe2\xde\x1f\x06KeyIDs\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _HEARTBEATREQUEST._options = None
    _HEARTBEATREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _REGISTEREXTERNALKEYSREQUEST_EXTERNALKEY.fields_by_name['id']._options = None
    _REGISTEREXTERNALKEYSREQUEST_EXTERNALKEY.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _REGISTEREXTERNALKEYSREQUEST.fields_by_name['sender']._options = None
    _REGISTEREXTERNALKEYSREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTEREXTERNALKEYSREQUEST.fields_by_name['chain']._options = None
    _REGISTEREXTERNALKEYSREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _REGISTEREXTERNALKEYSREQUEST.fields_by_name['external_keys']._options = None
    _REGISTEREXTERNALKEYSREQUEST.fields_by_name['external_keys']._serialized_options = b'\xc8\xde\x1f\x00'
    _REGISTEREXTERNALKEYSREQUEST._options = None
    _REGISTEREXTERNALKEYSREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _SUBMITMULTISIGPUBKEYSREQUEST.fields_by_name['sender']._options = None
    _SUBMITMULTISIGPUBKEYSREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _SUBMITMULTISIGPUBKEYSREQUEST.fields_by_name['key_id']._options = None
    _SUBMITMULTISIGPUBKEYSREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f9github.com/axelarnetwork/axelar-core/x/tss/exported.KeyID'
    _SUBMITMULTISIGPUBKEYSREQUEST.fields_by_name['sig_key_pairs']._options = None
    _SUBMITMULTISIGPUBKEYSREQUEST.fields_by_name['sig_key_pairs']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUBMITMULTISIGPUBKEYSREQUEST._options = None
    _SUBMITMULTISIGPUBKEYSREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _SUBMITMULTISIGSIGNATURESREQUEST.fields_by_name['sender']._options = None
    _SUBMITMULTISIGSIGNATURESREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _SUBMITMULTISIGSIGNATURESREQUEST.fields_by_name['sig_id']._options = None
    _SUBMITMULTISIGSIGNATURESREQUEST.fields_by_name['sig_id']._serialized_options = b'\xe2\xde\x1f\x05SigID'
    _SUBMITMULTISIGSIGNATURESREQUEST._options = None
    _SUBMITMULTISIGSIGNATURESREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _globals['_STARTKEYGENREQUEST']._serialized_start = 310
    _globals['_STARTKEYGENREQUEST']._serialized_end = 456
    _globals['_STARTKEYGENRESPONSE']._serialized_start = 458
    _globals['_STARTKEYGENRESPONSE']._serialized_end = 479
    _globals['_ROTATEKEYREQUEST']._serialized_start = 482
    _globals['_ROTATEKEYREQUEST']._serialized_end = 801
    _globals['_ROTATEKEYRESPONSE']._serialized_start = 803
    _globals['_ROTATEKEYRESPONSE']._serialized_end = 822
    _globals['_PROCESSKEYGENTRAFFICREQUEST']._serialized_start = 825
    _globals['_PROCESSKEYGENTRAFFICREQUEST']._serialized_end = 1023
    _globals['_PROCESSKEYGENTRAFFICRESPONSE']._serialized_start = 1025
    _globals['_PROCESSKEYGENTRAFFICRESPONSE']._serialized_end = 1055
    _globals['_PROCESSSIGNTRAFFICREQUEST']._serialized_start = 1058
    _globals['_PROCESSSIGNTRAFFICREQUEST']._serialized_end = 1254
    _globals['_PROCESSSIGNTRAFFICRESPONSE']._serialized_start = 1256
    _globals['_PROCESSSIGNTRAFFICRESPONSE']._serialized_end = 1284
    _globals['_VOTEPUBKEYREQUEST']._serialized_start = 1287
    _globals['_VOTEPUBKEYREQUEST']._serialized_end = 1515
    _globals['_VOTEPUBKEYRESPONSE']._serialized_start = 1517
    _globals['_VOTEPUBKEYRESPONSE']._serialized_end = 1550
    _globals['_VOTESIGREQUEST']._serialized_start = 1553
    _globals['_VOTESIGREQUEST']._serialized_end = 1776
    _globals['_VOTESIGRESPONSE']._serialized_start = 1778
    _globals['_VOTESIGRESPONSE']._serialized_end = 1808
    _globals['_HEARTBEATREQUEST']._serialized_start = 1811
    _globals['_HEARTBEATREQUEST']._serialized_end = 1992
    _globals['_HEARTBEATRESPONSE']._serialized_start = 1994
    _globals['_HEARTBEATRESPONSE']._serialized_end = 2013
    _globals['_REGISTEREXTERNALKEYSREQUEST']._serialized_start = 2016
    _globals['_REGISTEREXTERNALKEYSREQUEST']._serialized_end = 2405
    _globals['_REGISTEREXTERNALKEYSREQUEST_EXTERNALKEY']._serialized_start = 2288
    _globals['_REGISTEREXTERNALKEYSREQUEST_EXTERNALKEY']._serialized_end = 2399
    _globals['_REGISTEREXTERNALKEYSRESPONSE']._serialized_start = 2407
    _globals['_REGISTEREXTERNALKEYSRESPONSE']._serialized_end = 2437
    _globals['_SUBMITMULTISIGPUBKEYSREQUEST']._serialized_start = 2440
    _globals['_SUBMITMULTISIGPUBKEYSREQUEST']._serialized_end = 2701
    _globals['_SUBMITMULTISIGPUBKEYSRESPONSE']._serialized_start = 2703
    _globals['_SUBMITMULTISIGPUBKEYSRESPONSE']._serialized_end = 2734
    _globals['_SUBMITMULTISIGSIGNATURESREQUEST']._serialized_start = 2737
    _globals['_SUBMITMULTISIGSIGNATURESREQUEST']._serialized_end = 2890
    _globals['_SUBMITMULTISIGSIGNATURESRESPONSE']._serialized_start = 2892
    _globals['_SUBMITMULTISIGSIGNATURESRESPONSE']._serialized_end = 2926