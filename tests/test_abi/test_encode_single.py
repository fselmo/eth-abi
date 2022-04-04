import pytest

from eth_abi.abi import (
    encode_single,
)

from ..common.unit import (
    CORRECT_SINGLE_ENCODINGS,
)


@pytest.mark.parametrize(
    'typ,python_value,abi_encoding,_',
    CORRECT_SINGLE_ENCODINGS,
)
def test_encode_single(typ, python_value, abi_encoding, _):
    with pytest.warns(
        DeprecationWarning,
        match="abi.encode_single\(\) is deprecated and will be removed in version 4.0.0 in favor "
              "of "
              "abi.encode\(\)"
    ):
        actual = encode_single(typ, python_value)
        assert actual == abi_encoding
