"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....axelar.multisig.v1beta1 import tx_pb2 as axelar_dot_multisig_dot_v1beta1_dot_tx__pb2
from ....axelar.multisig.v1beta1 import query_pb2 as axelar_dot_multisig_dot_v1beta1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%axelar/multisig/v1beta1/service.proto\x12\x17axelar.multisig.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a axelar/multisig/v1beta1/tx.proto\x1a#axelar/multisig/v1beta1/query.proto2\xad\x07\n\nMsgService\x12\x92\x01\n\x0bStartKeygen\x12+.axelar.multisig.v1beta1.StartKeygenRequest\x1a,.axelar.multisig.v1beta1.StartKeygenResponse"(\x82\xd3\xe4\x93\x02""\x1d/axelar/multisig/start_keygen:\x01*\x12\x97\x01\n\x0cSubmitPubKey\x12,.axelar.multisig.v1beta1.SubmitPubKeyRequest\x1a-.axelar.multisig.v1beta1.SubmitPubKeyResponse"*\x82\xd3\xe4\x93\x02$"\x1f/axelar/multisig/submit_pub_key:\x01*\x12\xa2\x01\n\x0fSubmitSignature\x12/.axelar.multisig.v1beta1.SubmitSignatureRequest\x1a0.axelar.multisig.v1beta1.SubmitSignatureResponse",\x82\xd3\xe4\x93\x02&"!/axelar/multisig/submit_signature:\x01*\x12\x8a\x01\n\tRotateKey\x12).axelar.multisig.v1beta1.RotateKeyRequest\x1a*.axelar.multisig.v1beta1.RotateKeyResponse"&\x82\xd3\xe4\x93\x02 "\x1b/axelar/multisig/rotate_key:\x01*\x12\x9f\x01\n\x0cKeygenOptOut\x12,.axelar.multisig.v1beta1.KeygenOptOutRequest\x1a-.axelar.multisig.v1beta1.KeygenOptOutResponse"2\x82\xd3\xe4\x93\x02,"\'/axelar/multisig/v1beta1/keygen_opt_out:\x01*\x12\x9b\x01\n\x0bKeygenOptIn\x12+.axelar.multisig.v1beta1.KeygenOptInRequest\x1a,.axelar.multisig.v1beta1.KeygenOptInResponse"1\x82\xd3\xe4\x93\x02+"&/axelar/multisig/v1beta1/keygen_opt_in:\x01*2\xcd\x04\n\x0cQueryService\x12\x87\x01\n\x05KeyID\x12%.axelar.multisig.v1beta1.KeyIDRequest\x1a&.axelar.multisig.v1beta1.KeyIDResponse"/\x82\xd3\xe4\x93\x02)\x12\'/axelar/multisig/v1beta1/key_id/{chain}\x12\x98\x01\n\tNextKeyID\x12).axelar.multisig.v1beta1.NextKeyIDRequest\x1a*.axelar.multisig.v1beta1.NextKeyIDResponse"4\x82\xd3\xe4\x93\x02.\x12,/axelar/multisig/v1beta1/next_key_id/{chain}\x12v\n\x03Key\x12#.axelar.multisig.v1beta1.KeyRequest\x1a$.axelar.multisig.v1beta1.KeyResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/axelar/multisig/v1beta1/key\x12\x9f\x01\n\rKeygenSession\x12-.axelar.multisig.v1beta1.KeygenSessionRequest\x1a..axelar.multisig.v1beta1.KeygenSessionResponse"/\x82\xd3\xe4\x93\x02)\x12\'/axelar/multisig/v1beta1/keygen_sessionB;Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.multisig.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/multisig/types\xc0\xe3\x1e\x01'
    _MSGSERVICE.methods_by_name['StartKeygen']._options = None
    _MSGSERVICE.methods_by_name['StartKeygen']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/axelar/multisig/start_keygen:\x01*'
    _MSGSERVICE.methods_by_name['SubmitPubKey']._options = None
    _MSGSERVICE.methods_by_name['SubmitPubKey']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/axelar/multisig/submit_pub_key:\x01*'
    _MSGSERVICE.methods_by_name['SubmitSignature']._options = None
    _MSGSERVICE.methods_by_name['SubmitSignature']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/axelar/multisig/submit_signature:\x01*'
    _MSGSERVICE.methods_by_name['RotateKey']._options = None
    _MSGSERVICE.methods_by_name['RotateKey']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/axelar/multisig/rotate_key:\x01*'
    _MSGSERVICE.methods_by_name['KeygenOptOut']._options = None
    _MSGSERVICE.methods_by_name['KeygenOptOut']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/axelar/multisig/v1beta1/keygen_opt_out:\x01*'
    _MSGSERVICE.methods_by_name['KeygenOptIn']._options = None
    _MSGSERVICE.methods_by_name['KeygenOptIn']._serialized_options = b'\x82\xd3\xe4\x93\x02+"&/axelar/multisig/v1beta1/keygen_opt_in:\x01*'
    _QUERYSERVICE.methods_by_name['KeyID']._options = None
    _QUERYSERVICE.methods_by_name['KeyID']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/axelar/multisig/v1beta1/key_id/{chain}"
    _QUERYSERVICE.methods_by_name['NextKeyID']._options = None
    _QUERYSERVICE.methods_by_name['NextKeyID']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/axelar/multisig/v1beta1/next_key_id/{chain}'
    _QUERYSERVICE.methods_by_name['Key']._options = None
    _QUERYSERVICE.methods_by_name['Key']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/axelar/multisig/v1beta1/key'
    _QUERYSERVICE.methods_by_name['KeygenSession']._options = None
    _QUERYSERVICE.methods_by_name['KeygenSession']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/axelar/multisig/v1beta1/keygen_session"
    _globals['_MSGSERVICE']._serialized_start = 190
    _globals['_MSGSERVICE']._serialized_end = 1131
    _globals['_QUERYSERVICE']._serialized_start = 1134
    _globals['_QUERYSERVICE']._serialized_end = 1723