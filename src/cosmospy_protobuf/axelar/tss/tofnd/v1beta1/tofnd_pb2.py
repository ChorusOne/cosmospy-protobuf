"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....axelar.tss.tofnd.v1beta1 import common_pb2 as axelar_dot_tss_dot_tofnd_dot_v1beta1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$axelar/tss/tofnd/v1beta1/tofnd.proto\x12\x18axelar.tss.tofnd.v1beta1\x1a\x14gogoproto/gogo.proto\x1a%axelar/tss/tofnd/v1beta1/common.proto"\x8a\x01\n\x0eRecoverRequest\x129\n\x0bkeygen_init\x18\x01 \x01(\x0b2$.axelar.tss.tofnd.v1beta1.KeygenInit\x12=\n\rkeygen_output\x18\x02 \x01(\x0b2&.axelar.tss.tofnd.v1beta1.KeygenOutput"\xa6\x01\n\x0fRecoverResponse\x12D\n\x08response\x18\x01 \x01(\x0e22.axelar.tss.tofnd.v1beta1.RecoverResponse.Response"M\n\x08Response\x12\x18\n\x14RESPONSE_UNSPECIFIED\x10\x00\x12\x14\n\x10RESPONSE_SUCCESS\x10\x01\x12\x11\n\rRESPONSE_FAIL\x10\x02"Y\n\x0cKeygenOutput\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x1a\n\x12group_recover_info\x18\x02 \x01(\x0c\x12\x1c\n\x14private_recover_info\x18\x03 \x01(\x0c"\xd2\x01\n\tMessageIn\x12;\n\x0bkeygen_init\x18\x01 \x01(\x0b2$.axelar.tss.tofnd.v1beta1.KeygenInitH\x00\x127\n\tsign_init\x18\x02 \x01(\x0b2".axelar.tss.tofnd.v1beta1.SignInitH\x00\x126\n\x07traffic\x18\x03 \x01(\x0b2#.axelar.tss.tofnd.v1beta1.TrafficInH\x00\x12\x0f\n\x05abort\x18\x04 \x01(\x08H\x00B\x06\n\x04data"\xe0\x06\n\nMessageOut\x127\n\x07traffic\x18\x01 \x01(\x0b2$.axelar.tss.tofnd.v1beta1.TrafficOutH\x00\x12J\n\rkeygen_result\x18\x02 \x01(\x0b21.axelar.tss.tofnd.v1beta1.MessageOut.KeygenResultH\x00\x12F\n\x0bsign_result\x18\x03 \x01(\x0b2/.axelar.tss.tofnd.v1beta1.MessageOut.SignResultH\x00\x12\x16\n\x0cneed_recover\x18\x04 \x01(\x08H\x00\x1a\xa4\x01\n\x0cKeygenResult\x126\n\x04data\x18\x01 \x01(\x0b2&.axelar.tss.tofnd.v1beta1.KeygenOutputH\x00\x12F\n\tcriminals\x18\x02 \x01(\x0b21.axelar.tss.tofnd.v1beta1.MessageOut.CriminalListH\x00B\x14\n\x12keygen_result_data\x1a}\n\nSignResult\x12\x13\n\tsignature\x18\x01 \x01(\x0cH\x00\x12F\n\tcriminals\x18\x02 \x01(\x0b21.axelar.tss.tofnd.v1beta1.MessageOut.CriminalListH\x00B\x12\n\x10sign_result_data\x1a\xbe\x02\n\x0cCriminalList\x12M\n\tcriminals\x18\x01 \x03(\x0b2:.axelar.tss.tofnd.v1beta1.MessageOut.CriminalList.Criminal\x1a\xde\x01\n\x08Criminal\x12\x11\n\tparty_uid\x18\x01 \x01(\t\x12X\n\ncrime_type\x18\x02 \x01(\x0e2D.axelar.tss.tofnd.v1beta1.MessageOut.CriminalList.Criminal.CrimeType"e\n\tCrimeType\x12\x1a\n\x16CRIME_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18CRIME_TYPE_NON_MALICIOUS\x10\x01\x12\x18\n\x14CRIME_TYPE_MALICIOUS\x10\x02\x1a\x04\x88\xa3\x1e\x00B\x06\n\x04data"J\n\tTrafficIn\x12\x16\n\x0efrom_party_uid\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x14\n\x0cis_broadcast\x18\x03 \x01(\x08"I\n\nTrafficOut\x12\x14\n\x0cto_party_uid\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x14\n\x0cis_broadcast\x18\x03 \x01(\x08"|\n\nKeygenInit\x12\x13\n\x0bnew_key_uid\x18\x01 \x01(\t\x12\x12\n\nparty_uids\x18\x02 \x03(\t\x12\x1a\n\x12party_share_counts\x18\x05 \x03(\r\x12\x16\n\x0emy_party_index\x18\x03 \x01(\r\x12\x11\n\tthreshold\x18\x04 \x01(\r"]\n\x08SignInit\x12\x13\n\x0bnew_sig_uid\x18\x01 \x01(\t\x12\x0f\n\x07key_uid\x18\x02 \x01(\t\x12\x12\n\nparty_uids\x18\x03 \x03(\t\x12\x17\n\x0fmessage_to_sign\x18\x04 \x01(\x0cB2Z0github.com/axelarnetwork/axelar-core/x/tss/tofndb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.tss.tofnd.v1beta1.tofnd_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/axelarnetwork/axelar-core/x/tss/tofnd'
    _MESSAGEOUT_CRIMINALLIST_CRIMINAL_CRIMETYPE._options = None
    _MESSAGEOUT_CRIMINALLIST_CRIMINAL_CRIMETYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _globals['_RECOVERREQUEST']._serialized_start = 128
    _globals['_RECOVERREQUEST']._serialized_end = 266
    _globals['_RECOVERRESPONSE']._serialized_start = 269
    _globals['_RECOVERRESPONSE']._serialized_end = 435
    _globals['_RECOVERRESPONSE_RESPONSE']._serialized_start = 358
    _globals['_RECOVERRESPONSE_RESPONSE']._serialized_end = 435
    _globals['_KEYGENOUTPUT']._serialized_start = 437
    _globals['_KEYGENOUTPUT']._serialized_end = 526
    _globals['_MESSAGEIN']._serialized_start = 529
    _globals['_MESSAGEIN']._serialized_end = 739
    _globals['_MESSAGEOUT']._serialized_start = 742
    _globals['_MESSAGEOUT']._serialized_end = 1606
    _globals['_MESSAGEOUT_KEYGENRESULT']._serialized_start = 986
    _globals['_MESSAGEOUT_KEYGENRESULT']._serialized_end = 1150
    _globals['_MESSAGEOUT_SIGNRESULT']._serialized_start = 1152
    _globals['_MESSAGEOUT_SIGNRESULT']._serialized_end = 1277
    _globals['_MESSAGEOUT_CRIMINALLIST']._serialized_start = 1280
    _globals['_MESSAGEOUT_CRIMINALLIST']._serialized_end = 1598
    _globals['_MESSAGEOUT_CRIMINALLIST_CRIMINAL']._serialized_start = 1376
    _globals['_MESSAGEOUT_CRIMINALLIST_CRIMINAL']._serialized_end = 1598
    _globals['_MESSAGEOUT_CRIMINALLIST_CRIMINAL_CRIMETYPE']._serialized_start = 1497
    _globals['_MESSAGEOUT_CRIMINALLIST_CRIMINAL_CRIMETYPE']._serialized_end = 1598
    _globals['_TRAFFICIN']._serialized_start = 1608
    _globals['_TRAFFICIN']._serialized_end = 1682
    _globals['_TRAFFICOUT']._serialized_start = 1684
    _globals['_TRAFFICOUT']._serialized_end = 1757
    _globals['_KEYGENINIT']._serialized_start = 1759
    _globals['_KEYGENINIT']._serialized_end = 1883
    _globals['_SIGNINIT']._serialized_start = 1885
    _globals['_SIGNINIT']._serialized_end = 1978