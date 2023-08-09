"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....axelar.nexus.exported.v1beta1 import types_pb2 as axelar_dot_nexus_dot_exported_dot_v1beta1_dot_types__pb2
from ....axelar.permission.exported.v1beta1 import types_pb2 as axelar_dot_permission_dot_exported_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1daxelar/nexus/v1beta1/tx.proto\x12\x14axelar.nexus.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a)axelar/nexus/exported/v1beta1/types.proto\x1a.axelar/permission/exported/v1beta1/types.proto"\xbe\x01\n\x1eRegisterChainMaintainerRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12S\n\x06chains\x18\x02 \x03(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName:\x04\x80\xb5\x18\x01"!\n\x1fRegisterChainMaintainerResponse"\xc0\x01\n DeregisterChainMaintainerRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12S\n\x06chains\x18\x02 \x03(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName:\x04\x80\xb5\x18\x01"#\n!DeregisterChainMaintainerResponse"\xb4\x01\n\x14ActivateChainRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12S\n\x06chains\x18\x02 \x03(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName:\x04\x80\xb5\x18\x03"\x17\n\x15ActivateChainResponse"\xb6\x01\n\x16DeactivateChainRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12S\n\x06chains\x18\x02 \x03(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName:\x04\x80\xb5\x18\x03"\x19\n\x17DeactivateChainResponse"\xa2\x01\n\x17RegisterAssetFeeRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12>\n\x08fee_info\x18\x02 \x01(\x0b2&.axelar.nexus.exported.v1beta1.FeeInfoB\x04\xc8\xde\x1f\x00:\x04\x80\xb5\x18\x02"\x1a\n\x18RegisterAssetFeeResponse"\x9f\x02\n\x1bSetTransferRateLimitRequest\x12A\n\x06sender\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12R\n\x05chain\x18\x02 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12.\n\x05limit\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x123\n\x06window\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01:\x04\x80\xb5\x18\x03"\x1e\n\x1cSetTransferRateLimitResponseB8Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00'
    _REGISTERCHAINMAINTAINERREQUEST.fields_by_name['sender']._options = None
    _REGISTERCHAINMAINTAINERREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERCHAINMAINTAINERREQUEST.fields_by_name['chains']._options = None
    _REGISTERCHAINMAINTAINERREQUEST.fields_by_name['chains']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _REGISTERCHAINMAINTAINERREQUEST._options = None
    _REGISTERCHAINMAINTAINERREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _DEREGISTERCHAINMAINTAINERREQUEST.fields_by_name['sender']._options = None
    _DEREGISTERCHAINMAINTAINERREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _DEREGISTERCHAINMAINTAINERREQUEST.fields_by_name['chains']._options = None
    _DEREGISTERCHAINMAINTAINERREQUEST.fields_by_name['chains']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _DEREGISTERCHAINMAINTAINERREQUEST._options = None
    _DEREGISTERCHAINMAINTAINERREQUEST._serialized_options = b'\x80\xb5\x18\x01'
    _ACTIVATECHAINREQUEST.fields_by_name['sender']._options = None
    _ACTIVATECHAINREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _ACTIVATECHAINREQUEST.fields_by_name['chains']._options = None
    _ACTIVATECHAINREQUEST.fields_by_name['chains']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _ACTIVATECHAINREQUEST._options = None
    _ACTIVATECHAINREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _DEACTIVATECHAINREQUEST.fields_by_name['sender']._options = None
    _DEACTIVATECHAINREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _DEACTIVATECHAINREQUEST.fields_by_name['chains']._options = None
    _DEACTIVATECHAINREQUEST.fields_by_name['chains']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _DEACTIVATECHAINREQUEST._options = None
    _DEACTIVATECHAINREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _REGISTERASSETFEEREQUEST.fields_by_name['sender']._options = None
    _REGISTERASSETFEEREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _REGISTERASSETFEEREQUEST.fields_by_name['fee_info']._options = None
    _REGISTERASSETFEEREQUEST.fields_by_name['fee_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _REGISTERASSETFEEREQUEST._options = None
    _REGISTERASSETFEEREQUEST._serialized_options = b'\x80\xb5\x18\x02'
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['sender']._options = None
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['sender']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress'
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['chain']._options = None
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['limit']._options = None
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['limit']._serialized_options = b'\xc8\xde\x1f\x00'
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['window']._options = None
    _SETTRANSFERRATELIMITREQUEST.fields_by_name['window']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _SETTRANSFERRATELIMITREQUEST._options = None
    _SETTRANSFERRATELIMITREQUEST._serialized_options = b'\x80\xb5\x18\x03'
    _globals['_REGISTERCHAINMAINTAINERREQUEST']._serialized_start = 263
    _globals['_REGISTERCHAINMAINTAINERREQUEST']._serialized_end = 453
    _globals['_REGISTERCHAINMAINTAINERRESPONSE']._serialized_start = 455
    _globals['_REGISTERCHAINMAINTAINERRESPONSE']._serialized_end = 488
    _globals['_DEREGISTERCHAINMAINTAINERREQUEST']._serialized_start = 491
    _globals['_DEREGISTERCHAINMAINTAINERREQUEST']._serialized_end = 683
    _globals['_DEREGISTERCHAINMAINTAINERRESPONSE']._serialized_start = 685
    _globals['_DEREGISTERCHAINMAINTAINERRESPONSE']._serialized_end = 720
    _globals['_ACTIVATECHAINREQUEST']._serialized_start = 723
    _globals['_ACTIVATECHAINREQUEST']._serialized_end = 903
    _globals['_ACTIVATECHAINRESPONSE']._serialized_start = 905
    _globals['_ACTIVATECHAINRESPONSE']._serialized_end = 928
    _globals['_DEACTIVATECHAINREQUEST']._serialized_start = 931
    _globals['_DEACTIVATECHAINREQUEST']._serialized_end = 1113
    _globals['_DEACTIVATECHAINRESPONSE']._serialized_start = 1115
    _globals['_DEACTIVATECHAINRESPONSE']._serialized_end = 1140
    _globals['_REGISTERASSETFEEREQUEST']._serialized_start = 1143
    _globals['_REGISTERASSETFEEREQUEST']._serialized_end = 1305
    _globals['_REGISTERASSETFEERESPONSE']._serialized_start = 1307
    _globals['_REGISTERASSETFEERESPONSE']._serialized_end = 1333
    _globals['_SETTRANSFERRATELIMITREQUEST']._serialized_start = 1336
    _globals['_SETTRANSFERRATELIMITREQUEST']._serialized_end = 1623
    _globals['_SETTRANSFERRATELIMITRESPONSE']._serialized_start = 1625
    _globals['_SETTRANSFERRATELIMITRESPONSE']._serialized_end = 1655