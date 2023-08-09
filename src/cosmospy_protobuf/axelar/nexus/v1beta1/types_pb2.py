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
from ....axelar.utils.v1beta1 import bitmap_pb2 as axelar_dot_utils_dot_v1beta1_dot_bitmap__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n axelar/nexus/v1beta1/types.proto\x12\x14axelar.nexus.v1beta1\x1a\x1egoogle/protobuf/duration.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a)axelar/nexus/exported/v1beta1/types.proto\x1a!axelar/utils/v1beta1/bitmap.proto"\xa1\x02\n\x0fMaintainerState\x12B\n\x07address\x18\x01 \x01(\x0cB1\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress\x129\n\rmissing_votes\x18\x02 \x01(\x0b2\x1c.axelar.utils.v1beta1.BitmapB\x04\xc8\xde\x1f\x00\x12;\n\x0fincorrect_votes\x18\x03 \x01(\x0b2\x1c.axelar.utils.v1beta1.BitmapB\x04\xc8\xde\x1f\x00\x12R\n\x05chain\x18\x04 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName"\xec\x01\n\nChainState\x129\n\x05chain\x18\x01 \x01(\x0b2$.axelar.nexus.exported.v1beta1.ChainB\x04\xc8\xde\x1f\x00\x12\x11\n\tactivated\x18\x03 \x01(\x08\x12:\n\x06assets\x18\x05 \x03(\x0b2$.axelar.nexus.exported.v1beta1.AssetB\x04\xc8\xde\x1f\x00\x12H\n\x11maintainer_states\x18\x06 \x03(\x0b2%.axelar.nexus.v1beta1.MaintainerStateB\x06\x18\x01\xc8\xde\x1f\x00J\x04\x08\x04\x10\x05J\x04\x08\x02\x10\x03"\xb5\x01\n\x0fLinkedAddresses\x12O\n\x0fdeposit_address\x18\x01 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00\x12Q\n\x11recipient_address\x18\x02 \x01(\x0b20.axelar.nexus.exported.v1beta1.CrossChainAddressB\x04\xc8\xde\x1f\x00"\xc4\x01\n\tRateLimit\x12R\n\x05chain\x18\x01 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12.\n\x05limit\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x123\n\x06window\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01"\xe8\x01\n\rTransferEpoch\x12R\n\x05chain\x18\x01 \x01(\tBC\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName\x12/\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\r\n\x05epoch\x18\x03 \x01(\x04\x12C\n\tdirection\x18\x04 \x01(\x0e20.axelar.nexus.exported.v1beta1.TransferDirectionB8Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'axelar.nexus.v1beta1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/axelarnetwork/axelar-core/x/nexus/types\xc8\xe1\x1e\x00'
    _MAINTAINERSTATE.fields_by_name['address']._options = None
    _MAINTAINERSTATE.fields_by_name['address']._serialized_options = b'\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.ValAddress'
    _MAINTAINERSTATE.fields_by_name['missing_votes']._options = None
    _MAINTAINERSTATE.fields_by_name['missing_votes']._serialized_options = b'\xc8\xde\x1f\x00'
    _MAINTAINERSTATE.fields_by_name['incorrect_votes']._options = None
    _MAINTAINERSTATE.fields_by_name['incorrect_votes']._serialized_options = b'\xc8\xde\x1f\x00'
    _MAINTAINERSTATE.fields_by_name['chain']._options = None
    _MAINTAINERSTATE.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _CHAINSTATE.fields_by_name['chain']._options = None
    _CHAINSTATE.fields_by_name['chain']._serialized_options = b'\xc8\xde\x1f\x00'
    _CHAINSTATE.fields_by_name['assets']._options = None
    _CHAINSTATE.fields_by_name['assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _CHAINSTATE.fields_by_name['maintainer_states']._options = None
    _CHAINSTATE.fields_by_name['maintainer_states']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00'
    _LINKEDADDRESSES.fields_by_name['deposit_address']._options = None
    _LINKEDADDRESSES.fields_by_name['deposit_address']._serialized_options = b'\xc8\xde\x1f\x00'
    _LINKEDADDRESSES.fields_by_name['recipient_address']._options = None
    _LINKEDADDRESSES.fields_by_name['recipient_address']._serialized_options = b'\xc8\xde\x1f\x00'
    _RATELIMIT.fields_by_name['chain']._options = None
    _RATELIMIT.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _RATELIMIT.fields_by_name['limit']._options = None
    _RATELIMIT.fields_by_name['limit']._serialized_options = b'\xc8\xde\x1f\x00'
    _RATELIMIT.fields_by_name['window']._options = None
    _RATELIMIT.fields_by_name['window']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _TRANSFEREPOCH.fields_by_name['chain']._options = None
    _TRANSFEREPOCH.fields_by_name['chain']._serialized_options = b'\xfa\xde\x1f?github.com/axelarnetwork/axelar-core/x/nexus/exported.ChainName'
    _TRANSFEREPOCH.fields_by_name['amount']._options = None
    _TRANSFEREPOCH.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MAINTAINERSTATE']._serialized_start = 223
    _globals['_MAINTAINERSTATE']._serialized_end = 512
    _globals['_CHAINSTATE']._serialized_start = 515
    _globals['_CHAINSTATE']._serialized_end = 751
    _globals['_LINKEDADDRESSES']._serialized_start = 754
    _globals['_LINKEDADDRESSES']._serialized_end = 935
    _globals['_RATELIMIT']._serialized_start = 938
    _globals['_RATELIMIT']._serialized_end = 1134
    _globals['_TRANSFEREPOCH']._serialized_start = 1137
    _globals['_TRANSFEREPOCH']._serialized_end = 1369