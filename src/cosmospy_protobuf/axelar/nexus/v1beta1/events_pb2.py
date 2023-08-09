"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....axelar.nexus.exported.v1beta1 import types_pb2 as axelar_dot_nexus_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!axelar/nexus/v1beta1/events.proto\x12\x14axelar.nexus.v1beta1\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a)axelar/nexus/exported/v1beta1/types.proto"\xce\x02\n\x0bFeeDeducted\x12g\n\x0btransfer_id\x18\x01 \x01(\x04BR\xe2\xde\x1f\nTransferID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\\\n\x0frecipient_chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x19\n\x11recipient_address\x18\x03 \x01(\t\x12/\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12,\n\x03fee\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\xd2\x02\n\x0fInsufficientFee\x12g\n\x0btransfer_id\x18\x01 \x01(\x04BR\xe2\xde\x1f\nTransferID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\\\n\x0frecipient_chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x19\n\x11recipient_address\x18\x03 \x01(\t\x12/\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12,\n\x03fee\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\xcb\x01\n\x10RateLimitUpdated\x12R\n\x05chain\x18\x01 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12.\n\x05limit\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x123\n\x06window\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01"\xce\x01\n\x0fMessageReceived\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cpayload_hash\x18\x02 \x01(\x0c\x12F\n\x06sender\x18\x03 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00\x12I\n\trecipient\x18\x04 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00"\'\n\x11MessageProcessing\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID"%\n\x0fMessageExecuted\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID"#\n\rMessageFailed\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02IDB8Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.v1beta1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe3\x1e\x01'
    _FEEDEDUCTED.fields_by_name['transfer_id']._options = None
    _FEEDEDUCTED.fields_by_name['transfer_id']._serialized_options = b'\xe2\xde\x1f\nTransferID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _FEEDEDUCTED.fields_by_name['recipient_chain']._options = None
    _FEEDEDUCTED.fields_by_name['recipient_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _FEEDEDUCTED.fields_by_name['amount']._options = None
    _FEEDEDUCTED.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _FEEDEDUCTED.fields_by_name['fee']._options = None
    _FEEDEDUCTED.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _INSUFFICIENTFEE.fields_by_name['transfer_id']._options = None
    _INSUFFICIENTFEE.fields_by_name['transfer_id']._serialized_options = b'\xe2\xde\x1f\nTransferID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _INSUFFICIENTFEE.fields_by_name['recipient_chain']._options = None
    _INSUFFICIENTFEE.fields_by_name['recipient_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _INSUFFICIENTFEE.fields_by_name['amount']._options = None
    _INSUFFICIENTFEE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _INSUFFICIENTFEE.fields_by_name['fee']._options = None
    _INSUFFICIENTFEE.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _RATELIMITUPDATED.fields_by_name['chain']._options = None
    _RATELIMITUPDATED.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _RATELIMITUPDATED.fields_by_name['limit']._options = None
    _RATELIMITUPDATED.fields_by_name['limit']._serialized_options = b'\xc8\xde\x1f\x00'
    _RATELIMITUPDATED.fields_by_name['window']._options = None
    _RATELIMITUPDATED.fields_by_name['window']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _MESSAGERECEIVED.fields_by_name['id']._options = None
    _MESSAGERECEIVED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MESSAGERECEIVED.fields_by_name['sender']._options = None
    _MESSAGERECEIVED.fields_by_name['sender']._serialized_options = b'\xc8\xde\x1f\x00'
    _MESSAGERECEIVED.fields_by_name['recipient']._options = None
    _MESSAGERECEIVED.fields_by_name['recipient']._serialized_options = b'\xc8\xde\x1f\x00'
    _MESSAGEPROCESSING.fields_by_name['id']._options = None
    _MESSAGEPROCESSING.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MESSAGEEXECUTED.fields_by_name['id']._options = None
    _MESSAGEEXECUTED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MESSAGEFAILED.fields_by_name['id']._options = None
    _MESSAGEFAILED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_FEEDEDUCTED']._serialized_start = 189
    _globals['_FEEDEDUCTED']._serialized_end = 523
    _globals['_INSUFFICIENTFEE']._serialized_start = 526
    _globals['_INSUFFICIENTFEE']._serialized_end = 864
    _globals['_RATELIMITUPDATED']._serialized_start = 867
    _globals['_RATELIMITUPDATED']._serialized_end = 1070
    _globals['_MESSAGERECEIVED']._serialized_start = 1073
    _globals['_MESSAGERECEIVED']._serialized_end = 1279
    _globals['_MESSAGEPROCESSING']._serialized_start = 1281
    _globals['_MESSAGEPROCESSING']._serialized_end = 1320
    _globals['_MESSAGEEXECUTED']._serialized_start = 1322
    _globals['_MESSAGEEXECUTED']._serialized_end = 1359
    _globals['_MESSAGEFAILED']._serialized_start = 1361
    _globals['_MESSAGEFAILED']._serialized_end = 1396