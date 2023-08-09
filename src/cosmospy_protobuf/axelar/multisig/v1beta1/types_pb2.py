"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....axelar.utils.v1beta1 import threshold_pb2 as axelar_dot_utils_dot_v1beta1_dot_threshold__pb2
from ....axelar.snapshot.exported.v1beta1 import types_pb2 as axelar_dot_snapshot_dot_exported_dot_v1beta1_dot_types__pb2
from ....axelar.multisig.exported.v1beta1 import types_pb2 as axelar_dot_multisig_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#axelar/multisig/v1beta1/types.proto\x12\x17axelar.multisig.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a$axelar/utils/v1beta1/threshold.proto\x1a,axelar/snapshot/exported/v1beta1/types.proto\x1a,axelar/multisig/exported/v1beta1/types.proto"\xd8\x03\n\x03Key\x12T\n\x02id\x18\x01 \x01(\tBH\xe2\xde\x1f\x02ID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x12B\n\x08snapshot\x18\x02 \x01(\x0b2*.axelar.snapshot.exported.v1beta1.SnapshotB\x04\xc8\xde\x1f\x00\x12\x83\x01\n\x08pub_keys\x18\x03 \x03(\x0b2).axelar.multisig.v1beta1.Key.PubKeysEntryBF\x8a\xdf\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey\x12@\n\x11signing_threshold\x18\x04 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x129\n\x05state\x18\x05 \x01(\x0e2*.axelar.multisig.exported.v1beta1.KeyState\x1a.\n\x0cPubKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01:\x04\x98\xa1\x1f\x01"\x9b\x03\n\rKeygenSession\x12/\n\x03key\x18\x01 \x01(\x0b2\x1c.axelar.multisig.v1beta1.KeyB\x04\xc8\xde\x1f\x00\x12>\n\x05state\x18\x02 \x01(\x0e2/.axelar.multisig.exported.v1beta1.MultisigState\x12?\n\x10keygen_threshold\x18\x03 \x01(\x0b2\x1f.axelar.utils.v1beta1.ThresholdB\x04\xc8\xde\x1f\x00\x12\x12\n\nexpires_at\x18\x04 \x01(\x03\x12\x14\n\x0ccompleted_at\x18\x05 \x01(\x03\x12Y\n\x13is_pub_key_received\x18\x06 \x03(\x0b2<.axelar.multisig.v1beta1.KeygenSession.IsPubKeyReceivedEntry\x12\x14\n\x0cgrace_period\x18\x07 \x01(\x03\x1a7\n\x15IsPubKeyReceivedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x028\x01:\x04\x98\xa1\x1f\x01"\xbd\x02\n\x08MultiSig\x12[\n\x06key_id\x18\x01 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID\x12W\n\x0cpayload_hash\x18\x02 \x01(\x0cBA\xfa\xde\x1f=github.com/axelarnetwork/axelar-core/x/multisig/exported.Hash\x12H\n\x04sigs\x18\x03 \x03(\x0b2+.axelar.multisig.v1beta1.MultiSig.SigsEntryB\r\x8a\xdf\x1f\tSignature\x1a+\n\tSigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01:\x04\x98\xa1\x1f\x01"\x82\x03\n\x0eSigningSession\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12:\n\tmulti_sig\x18\x02 \x01(\x0b2!.axelar.multisig.v1beta1.MultiSigB\x04\xc8\xde\x1f\x00\x12>\n\x05state\x18\x03 \x01(\x0e2/.axelar.multisig.exported.v1beta1.MultisigState\x12/\n\x03key\x18\x04 \x01(\x0b2\x1c.axelar.multisig.v1beta1.KeyB\x04\xc8\xde\x1f\x00\x12\x12\n\nexpires_at\x18\x05 \x01(\x03\x12\x14\n\x0ccompleted_at\x18\x06 \x01(\x03\x12\x14\n\x0cgrace_period\x18\x07 \x01(\x03\x12\x0e\n\x06module\x18\x08 \x01(\t\x12Y\n\x0fmodule_metadata\x18\t \x01(\x0b2\x14.google.protobuf.AnyB*\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler:\x04\x98\xa1\x1f\x01"\xca\x01\n\x08KeyEpoch\x12\r\n\x05epoch\x18\x01 \x01(\x04\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12[\n\x06key_id\x18\x03 \x01(\tBK\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyIDB7Z5github.com/axelarnetwork/axelar-core/x/multisig/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types'
    _KEY_PUBKEYSENTRY._options = None
    _KEY_PUBKEYSENTRY._serialized_options = b'8\x01'
    _KEY.fields_by_name['id']._options = None
    _KEY.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _KEY.fields_by_name['snapshot']._options = None
    _KEY.fields_by_name['snapshot']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEY.fields_by_name['pub_keys']._options = None
    _KEY.fields_by_name['pub_keys']._serialized_options = b'\x8a\xdf\x1fBgithub.com/axelarnetwork/axelar-core/x/multisig/exported.PublicKey'
    _KEY.fields_by_name['signing_threshold']._options = None
    _KEY.fields_by_name['signing_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEY._options = None
    _KEY._serialized_options = b'\x98\xa1\x1f\x01'
    _KEYGENSESSION_ISPUBKEYRECEIVEDENTRY._options = None
    _KEYGENSESSION_ISPUBKEYRECEIVEDENTRY._serialized_options = b'8\x01'
    _KEYGENSESSION.fields_by_name['key']._options = None
    _KEYGENSESSION.fields_by_name['key']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEYGENSESSION.fields_by_name['keygen_threshold']._options = None
    _KEYGENSESSION.fields_by_name['keygen_threshold']._serialized_options = b'\xc8\xde\x1f\x00'
    _KEYGENSESSION._options = None
    _KEYGENSESSION._serialized_options = b'\x98\xa1\x1f\x01'
    _MULTISIG_SIGSENTRY._options = None
    _MULTISIG_SIGSENTRY._serialized_options = b'8\x01'
    _MULTISIG.fields_by_name['key_id']._options = None
    _MULTISIG.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _MULTISIG.fields_by_name['payload_hash']._options = None
    _MULTISIG.fields_by_name['payload_hash']._serialized_options = b'\xfa\xde\x1f=github.com/axelarnetwork/axelar-core/x/multisig/exported.Hash'
    _MULTISIG.fields_by_name['sigs']._options = None
    _MULTISIG.fields_by_name['sigs']._serialized_options = b'\x8a\xdf\x1f\tSignature'
    _MULTISIG._options = None
    _MULTISIG._serialized_options = b'\x98\xa1\x1f\x01'
    _SIGNINGSESSION.fields_by_name['id']._options = None
    _SIGNINGSESSION.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _SIGNINGSESSION.fields_by_name['multi_sig']._options = None
    _SIGNINGSESSION.fields_by_name['multi_sig']._serialized_options = b'\xc8\xde\x1f\x00'
    _SIGNINGSESSION.fields_by_name['key']._options = None
    _SIGNINGSESSION.fields_by_name['key']._serialized_options = b'\xc8\xde\x1f\x00'
    _SIGNINGSESSION.fields_by_name['module_metadata']._options = None
    _SIGNINGSESSION.fields_by_name['module_metadata']._serialized_options = b'\xca\xb4-&github.com/cosmos/codec/ProtoMarshaler'
    _SIGNINGSESSION._options = None
    _SIGNINGSESSION._serialized_options = b'\x98\xa1\x1f\x01'
    _KEYEPOCH.fields_by_name['chain']._options = None
    _KEYEPOCH.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _KEYEPOCH.fields_by_name['key_id']._options = None
    _KEYEPOCH.fields_by_name['key_id']._serialized_options = b'\xe2\xde\x1f\x05KeyID\xfa\xde\x1f>github.com/axelarnetwork/axelar-core/x/multisig/exported.KeyID'
    _globals['_KEY']._serialized_start = 271
    _globals['_KEY']._serialized_end = 743
    _globals['_KEY_PUBKEYSENTRY']._serialized_start = 691
    _globals['_KEY_PUBKEYSENTRY']._serialized_end = 737
    _globals['_KEYGENSESSION']._serialized_start = 746
    _globals['_KEYGENSESSION']._serialized_end = 1157
    _globals['_KEYGENSESSION_ISPUBKEYRECEIVEDENTRY']._serialized_start = 1096
    _globals['_KEYGENSESSION_ISPUBKEYRECEIVEDENTRY']._serialized_end = 1151
    _globals['_MULTISIG']._serialized_start = 1160
    _globals['_MULTISIG']._serialized_end = 1477
    _globals['_MULTISIG_SIGSENTRY']._serialized_start = 1428
    _globals['_MULTISIG_SIGSENTRY']._serialized_end = 1471
    _globals['_SIGNINGSESSION']._serialized_start = 1480
    _globals['_SIGNINGSESSION']._serialized_end = 1866
    _globals['_KEYEPOCH']._serialized_start = 1869
    _globals['_KEYEPOCH']._serialized_end = 2071