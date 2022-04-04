import pytest

from eth_abi.abi import (
    decode_single,
)

from ..common.unit import (
    CORRECT_SINGLE_ENCODINGS,
)


@pytest.mark.parametrize(
    'typ,expected,abi_encoding,_',
    CORRECT_SINGLE_ENCODINGS,
)
def test_decode_single(typ, expected, abi_encoding, _):
    with pytest.warns(
        DeprecationWarning,
        match="abi.decode_single\(\) is deprecated and will be removed in version 4.0.0 in favor "
              "of abi.decode\(\)"
    ):
        actual = decode_single(typ, abi_encoding)
        assert actual == expected


def test_decode_single_wrong_data_type_raises():
    with pytest.raises(TypeError):
        decode_single('uint32', '')
