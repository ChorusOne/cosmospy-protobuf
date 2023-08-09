"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/multisig/v1beta1/tx.proto\x12\x17axelar.multisig.v1beta1\x1a\x14gogoproto/gogo.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\xba\x01\n\x12StartKeygenRequest\x12A\n\x06sender\x18\x01 \x01(\tB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12[\n\x06key_id\x18\x02 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID:\x04\x80\xb5\x18\x02"\x15\n\x13StartKeygenResponse"\xb6\x02\n\x13SubmitPubKeyRequest\x12A\n\x06sender\x18\x01 \x01(\tB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12[\n\x06key_id\x18\x02 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x12W\n\x07pub_key\x18\x03 \x01(\x0cBF\xfa\xde\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey\x12 \n\tsignature\x18\x04 \x01(\x0cB\r\xfa\xde\x1f\tSignature:\x04\x80\xb5\x18\x01"\x16\n\x14SubmitPubKeyResponse"\x9e\x01\n\x16SubmitSignatureRequest\x12A\n\x06sender\x18\x01 \x01(\tB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x19\n\x06sig_id\x18\x02 \x01(\x04B\t\xe2\xde\x1f\x05SigID\x12 \n\tsignature\x18\x03 \x01(\x0cB\r\xfa\xde\x1f\tSignature:\x04\x80\xb5\x18\x01"\x19\n\x17SubmitSignatureResponse"\x8c\x02\n\x10RotateKeyRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12[\n\x06key_id\x18\x03 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID:\x04\x80\xb5\x18\x02"\x13\n\x11RotateKeyResponse"^\n\x13KeygenOptOutRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x01"\x16\n\x14KeygenOptOutResponse"]\n\x12KeygenOptInRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress:\x04\x80\xb5\x18\x01"\x15\n\x13KeygenOptInResponseB;Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc8\xe1\x1e\x00'
    _STARTKEYGENREQUEST.fields_by_name['sender']._options = None
    _STARTKEYGENREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _STARTKEYGENREQUEST.fields_by_name['key_id']._options = None
    _STARTKEYGENREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _STARTKEYGENREQUEST._options = None
    _STARTKEYGENREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _SUBMITPUBKEYREQUEST.fields_by_name['sender']._options = None
    _SUBMITPUBKEYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _SUBMITPUBKEYREQUEST.fields_by_name['key_id']._options = None
    _SUBMITPUBKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _SUBMITPUBKEYREQUEST.fields_by_name['pub_key']._options = None
    _SUBMITPUBKEYREQUEST.fields_by_name['pub_key']._serialized_options = b'\xfa\xde\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey'
    _SUBMITPUBKEYREQUEST.fields_by_name['signature']._options = None
    _SUBMITPUBKEYREQUEST.fields_by_name['signature']._serialized_options = b'\xfa\xde\x1f\tSignature'
    _SUBMITPUBKEYREQUEST._options = None
    _SUBMITPUBKEYREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _SUBMITSIGNATUREREQUEST.fields_by_name['sender']._options = None
    _SUBMITSIGNATUREREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _SUBMITSIGNATUREREQUEST.fields_by_name['sig_id']._options = None
    _SUBMITSIGNATUREREQUEST.fields_by_name['sig_id']._serialized_options = b'\xe2\xde\x1f\x05SigID'
    _SUBMITSIGNATUREREQUEST.fields_by_name['signature']._options = None
    _SUBMITSIGNATUREREQUEST.fields_by_name['signature']._serialized_options = b'\xfa\xde\x1f\tSignature'
    _SUBMITSIGNATUREREQUEST._options = None
    _SUBMITSIGNATUREREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _ROTATEKEYREQUEST.fields_by_name['sender']._options = None
    _ROTATEKEYREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _ROTATEKEYREQUEST.fields_by_name['chain']._options = None
    _ROTATEKEYREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _ROTATEKEYREQUEST.fields_by_name['key_id']._options = None
    _ROTATEKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _ROTATEKEYREQUEST._options = None
    _ROTATEKEYREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _KEYGENOPTOUTREQUEST.fields_by_name['sender']._options = None
    _KEYGENOPTOUTREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _KEYGENOPTOUTREQUEST._options = None
    _KEYGENOPTOUTREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _KEYGENOPTINREQUEST.fields_by_name['sender']._options = None
    _KEYGENOPTINREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _KEYGENOPTINREQUEST._options = None
    _KEYGENOPTINREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _globals['_STARTKEYGENREQUEST']._serialized_start = 132
    _globals['_STARTKEYGENREQUEST']._serialized_end = 318
    _globals['_STARTKEYGENRESPONSE']._serialized_start = 320
    _globals['_STARTKEYGENRESPONSE']._serialized_end = 341
    _globals['_SUBMITPUBKEYREQUEST']._serialized_start = 344
    _globals['_SUBMITPUBKEYREQUEST']._serialized_end = 654
    _globals['_SUBMITPUBKEYRESPONSE']._serialized_start = 656
    _globals['_SUBMITPUBKEYRESPONSE']._serialized_end = 678
    _globals['_SUBMITSIGNATUREREQUEST']._serialized_start = 681
    _globals['_SUBMITSIGNATUREREQUEST']._serialized_end = 839
    _globals['_SUBMITSIGNATURERESPONSE']._serialized_start = 841
    _globals['_SUBMITSIGNATURERESPONSE']._serialized_end = 866
    _globals['_ROTATEKEYREQUEST']._serialized_start = 869
    _globals['_ROTATEKEYREQUEST']._serialized_end = 1137
    _globals['_ROTATEKEYRESPONSE']._serialized_start = 1139
    _globals['_ROTATEKEYRESPONSE']._serialized_end = 1158
    _globals['_KEYGENOPTOUTREQUEST']._serialized_start = 1160
    _globals['_KEYGENOPTOUTREQUEST']._serialized_end = 1254
    _globals['_KEYGENOPTOUTRESPONSE']._serialized_start = 1256
    _globals['_KEYGENOPTOUTRESPONSE']._serialized_end = 1278
    _globals['_KEYGENOPTINREQUEST']._serialized_start = 1280
    _globals['_KEYGENOPTINREQUEST']._serialized_end = 1373
    _globals['_KEYGENOPTINRESPONSE']._serialized_start = 1375
    _globals['_KEYGENOPTINRESPONSE']._serialized_end = 1396