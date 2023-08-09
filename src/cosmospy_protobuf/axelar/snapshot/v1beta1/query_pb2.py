"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#axelar/snapshot/v1beta1/query.proto\x12\x17axelar.snapshot.v1beta1\x1a\x14gogoproto/gogo.proto"\xdb\x03\n\x17QueryValidatorsResponse\x12N\n\nvalidators\x18\x01 \x03(\x0b2:.axelar.snapshot.v1beta1.QueryValidatorsResponse.Validator\x1a\xcb\x01\n\x13TssIllegibilityInfo\x12\x12\n\ntombstoned\x18\x01 \x01(\x08\x12\x0e\n\x06jailed\x18\x02 \x01(\x08\x12\x1e\n\x16missed_too_many_blocks\x18\x03 \x01(\x08\x12\x1b\n\x13no_proxy_registered\x18\x04 \x01(\x08\x12\x15\n\rtss_suspended\x18\x05 \x01(\x08\x12\x1f\n\x17proxy_insuficient_funds\x18\x06 \x01(\x08\x12\x1b\n\x13stale_tss_heartbeat\x18\x07 \x01(\x08\x1a\xa1\x01\n\tValidator\x12\x18\n\x10operator_address\x18\x01 \x01(\t\x12\x0f\n\x07moniker\x18\x02 \x01(\t\x12i\n\x15tss_illegibility_info\x18\x03 \x01(\x0b2D.axelar.snapshot.v1beta1.QueryValidatorsResponse.TssIllegibilityInfoB\x04\xc8\xde\x1f\x00B;Z5github.com/axelarnetwork/axelar-core/x/snapshot/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.snapshot.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/axelarnetwork/axelar-core/x/snapshot/types\xc8\xe1\x1e\x00'
    _QUERYVALIDATORSRESPONSE_VALIDATOR.fields_by_name['tss_illegibility_info']._options = None
    _QUERYVALIDATORSRESPONSE_VALIDATOR.fields_by_name['tss_illegibility_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYVALIDATORSRESPONSE']._serialized_start = 87
    _globals['_QUERYVALIDATORSRESPONSE']._serialized_end = 562
    _globals['_QUERYVALIDATORSRESPONSE_TSSILLEGIBILITYINFO']._serialized_start = 195
    _globals['_QUERYVALIDATORSRESPONSE_TSSILLEGIBILITYINFO']._serialized_end = 398
    _globals['_QUERYVALIDATORSRESPONSE_VALIDATOR']._serialized_start = 401
    _globals['_QUERYVALIDATORSRESPONSE_VALIDATOR']._serialized_end = 562