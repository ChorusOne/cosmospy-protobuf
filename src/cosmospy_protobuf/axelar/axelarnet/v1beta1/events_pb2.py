"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%axelar/axelarnet/v1beta1/events.proto\x12\x18axelar.axelarnet.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x96\x02\n\x0fIBCTransferSent\x12V\n\x02id\x18\x01 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\x16\n\nreceipient\x18\x02 \x01(\tB\x02\x18\x01\x12.\n\x05asset\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x10\n\x08sequence\x18\x04 \x01(\x04\x12\x1b\n\x07port_id\x18\x05 \x01(\tB\n\xe2\xde\x1f\x06PortID\x12!\n\nchannel_id\x18\x06 \x01(\tB\r\xe2\xde\x1f\tChannelID\x12\x11\n\trecipient\x18\x07 \x01(\t"\xc0\x01\n\x14IBCTransferCompleted\x12V\n\x02id\x18\x01 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x1b\n\x07port_id\x18\x03 \x01(\tB\n\xe2\xde\x1f\x06PortID\x12!\n\nchannel_id\x18\x04 \x01(\tB\r\xe2\xde\x1f\tChannelID"\xbd\x01\n\x11IBCTransferFailed\x12V\n\x02id\x18\x01 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x1b\n\x07port_id\x18\x03 \x01(\tB\n\xe2\xde\x1f\x06PortID\x12!\n\nchannel_id\x18\x04 \x01(\tB\r\xe2\xde\x1f\tChannelID"\x99\x02\n\x12IBCTransferRetried\x12V\n\x02id\x18\x01 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\x16\n\nreceipient\x18\x02 \x01(\tB\x02\x18\x01\x12.\n\x05asset\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x10\n\x08sequence\x18\x04 \x01(\x04\x12\x1b\n\x07port_id\x18\x05 \x01(\tB\n\xe2\xde\x1f\x06PortID\x12!\n\nchannel_id\x18\x06 \x01(\tB\r\xe2\xde\x1f\tChannelID\x12\x11\n\trecipient\x18\x07 \x01(\t"\xcc\x01\n\x17AxelarTransferCompleted\x12V\n\x02id\x18\x01 \x01(\x04BJ\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\x16\n\nreceipient\x18\x02 \x01(\tB\x02\x18\x01\x12.\n\x05asset\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x11\n\trecipient\x18\x04 \x01(\t"\x82\x01\n\x0cFeeCollected\x12D\n\tcollector\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12,\n\x03fee\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\xa0\x01\n\x07FeePaid\x12!\n\nmessage_id\x18\x01 \x01(\tB\r\xe2\xde\x1f\tMessageID\x12D\n\trecipient\x18\x02 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12,\n\x03fee\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\xc6\x02\n\x15ContractCallSubmitted\x12!\n\nmessage_id\x18\x01 \x01(\tB\r\xe2\xde\x1f\tMessageID\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12Y\n\x0csource_chain\x18\x03 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12^\n\x11destination_chain\x18\x04 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x18\n\x10contract_address\x18\x05 \x01(\t\x12\x0f\n\x07payload\x18\x06 \x01(\x0c\x12\x14\n\x0cpayload_hash\x18\x07 \x01(\x0c"\xff\x02\n\x1eContractCallWithTokenSubmitted\x12!\n\nmessage_id\x18\x01 \x01(\tB\r\xe2\xde\x1f\tMessageID\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12Y\n\x0csource_chain\x18\x03 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12^\n\x11destination_chain\x18\x04 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x18\n\x10contract_address\x18\x05 \x01(\t\x12\x0f\n\x07payload\x18\x06 \x01(\x0c\x12\x14\n\x0cpayload_hash\x18\x07 \x01(\x0c\x12.\n\x05asset\x18\x08 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\x8c\x03\n\tTokenSent\x12g\n\x0btransfer_id\x18\x01 \x01(\x04BR\xe2\xde\x1f\nTransferID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12Y\n\x0csource_chain\x18\x03 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12^\n\x11destination_chain\x18\x04 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12\x1b\n\x13destination_address\x18\x05 \x01(\t\x12.\n\x05asset\x18\x06 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00B<Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.axelarnet.v1beta1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/axelarnetwork/axelar-core/x/axelarnet/types\xc8\xe3\x1e\x01'
    _IBCTRANSFERSENT.fields_by_name['id']._options = None
    _IBCTRANSFERSENT.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _IBCTRANSFERSENT.fields_by_name['receipient']._options = None
    _IBCTRANSFERSENT.fields_by_name['receipient']._serialized_options = b'\x18\x01'
    _IBCTRANSFERSENT.fields_by_name['asset']._options = None
    _IBCTRANSFERSENT.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _IBCTRANSFERSENT.fields_by_name['port_id']._options = None
    _IBCTRANSFERSENT.fields_by_name['port_id']._serialized_options = b'\xe2\xde\x1f\x06PortID'
    _IBCTRANSFERSENT.fields_by_name['channel_id']._options = None
    _IBCTRANSFERSENT.fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _IBCTRANSFERCOMPLETED.fields_by_name['id']._options = None
    _IBCTRANSFERCOMPLETED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _IBCTRANSFERCOMPLETED.fields_by_name['port_id']._options = None
    _IBCTRANSFERCOMPLETED.fields_by_name['port_id']._serialized_options = b'\xe2\xde\x1f\x06PortID'
    _IBCTRANSFERCOMPLETED.fields_by_name['channel_id']._options = None
    _IBCTRANSFERCOMPLETED.fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _IBCTRANSFERFAILED.fields_by_name['id']._options = None
    _IBCTRANSFERFAILED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _IBCTRANSFERFAILED.fields_by_name['port_id']._options = None
    _IBCTRANSFERFAILED.fields_by_name['port_id']._serialized_options = b'\xe2\xde\x1f\x06PortID'
    _IBCTRANSFERFAILED.fields_by_name['channel_id']._options = None
    _IBCTRANSFERFAILED.fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _IBCTRANSFERRETRIED.fields_by_name['id']._options = None
    _IBCTRANSFERRETRIED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _IBCTRANSFERRETRIED.fields_by_name['receipient']._options = None
    _IBCTRANSFERRETRIED.fields_by_name['receipient']._serialized_options = b'\x18\x01'
    _IBCTRANSFERRETRIED.fields_by_name['asset']._options = None
    _IBCTRANSFERRETRIED.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _IBCTRANSFERRETRIED.fields_by_name['port_id']._options = None
    _IBCTRANSFERRETRIED.fields_by_name['port_id']._serialized_options = b'\xe2\xde\x1f\x06PortID'
    _IBCTRANSFERRETRIED.fields_by_name['channel_id']._options = None
    _IBCTRANSFERRETRIED.fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _AXELARTRANSFERCOMPLETED.fields_by_name['id']._options = None
    _AXELARTRANSFERCOMPLETED.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _AXELARTRANSFERCOMPLETED.fields_by_name['receipient']._options = None
    _AXELARTRANSFERCOMPLETED.fields_by_name['receipient']._serialized_options = b'\x18\x01'
    _AXELARTRANSFERCOMPLETED.fields_by_name['asset']._options = None
    _AXELARTRANSFERCOMPLETED.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _FEECOLLECTED.fields_by_name['collector']._options = None
    _FEECOLLECTED.fields_by_name['collector']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _FEECOLLECTED.fields_by_name['fee']._options = None
    _FEECOLLECTED.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _FEEPAID.fields_by_name['message_id']._options = None
    _FEEPAID.fields_by_name['message_id']._serialized_options = b'\xe2\xde\x1f\tMessageID'
    _FEEPAID.fields_by_name['recipient']._options = None
    _FEEPAID.fields_by_name['recipient']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _FEEPAID.fields_by_name['fee']._options = None
    _FEEPAID.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONTRACTCALLSUBMITTED.fields_by_name['message_id']._options = None
    _CONTRACTCALLSUBMITTED.fields_by_name['message_id']._serialized_options = b'\xe2\xde\x1f\tMessageID'
    _CONTRACTCALLSUBMITTED.fields_by_name['source_chain']._options = None
    _CONTRACTCALLSUBMITTED.fields_by_name['source_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CONTRACTCALLSUBMITTED.fields_by_name['destination_chain']._options = None
    _CONTRACTCALLSUBMITTED.fields_by_name['destination_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['message_id']._options = None
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['message_id']._serialized_options = b'\xe2\xde\x1f\tMessageID'
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['source_chain']._options = None
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['source_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['destination_chain']._options = None
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['destination_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['asset']._options = None
    _CONTRACTCALLWITHTOKENSUBMITTED.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _TOKENSENT.fields_by_name['transfer_id']._options = None
    _TOKENSENT.fields_by_name['transfer_id']._serialized_options = b'\xe2\xde\x1f\nTransferID\xfa\xde\x1f@github.com/axelarnetwork/axelar-core/x/nexus/exported.TransferID'
    _TOKENSENT.fields_by_name['source_chain']._options = None
    _TOKENSENT.fields_by_name['source_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _TOKENSENT.fields_by_name['destination_chain']._options = None
    _TOKENSENT.fields_by_name['destination_chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _TOKENSENT.fields_by_name['asset']._options = None
    _TOKENSENT.fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_IBCTRANSFERSENT']._serialized_start = 122
    _globals['_IBCTRANSFERSENT']._serialized_end = 400
    _globals['_IBCTRANSFERCOMPLETED']._serialized_start = 403
    _globals['_IBCTRANSFERCOMPLETED']._serialized_end = 595
    _globals['_IBCTRANSFERFAILED']._serialized_start = 598
    _globals['_IBCTRANSFERFAILED']._serialized_end = 787
    _globals['_IBCTRANSFERRETRIED']._serialized_start = 790
    _globals['_IBCTRANSFERRETRIED']._serialized_end = 1071
    _globals['_AXELARTRANSFERCOMPLETED']._serialized_start = 1074
    _globals['_AXELARTRANSFERCOMPLETED']._serialized_end = 1278
    _globals['_FEECOLLECTED']._serialized_start = 1281
    _globals['_FEECOLLECTED']._serialized_end = 1411
    _globals['_FEEPAID']._serialized_start = 1414
    _globals['_FEEPAID']._serialized_end = 1574
    _globals['_CONTRACTCALLSUBMITTED']._serialized_start = 1577
    _globals['_CONTRACTCALLSUBMITTED']._serialized_end = 1903
    _globals['_CONTRACTCALLWITHTOKENSUBMITTED']._serialized_start = 1906
    _globals['_CONTRACTCALLWITHTOKENSUBMITTED']._serialized_end = 2289
    _globals['_TOKENSENT']._serialized_start = 2292
    _globals['_TOKENSENT']._serialized_end = 2688