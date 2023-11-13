# py test for binance utils
# Path: test/utils/binance_utils_test.py
# Compare this snippet from test/utils/binance_utils_test.py:
# # pylint: disable=missing-docstring
# from src.utils.binance_utils import BinanceUtils
#
# from test.constants import RAW_BINANCE_CANDLE_ITEM_TEST
#

# pylint: disable=missing-docstring
from src.utils.binance_utils import BinanceUtils

from test.constants import RAW_BINANCE_STREAM_TEST


def test_stream_is_converted_to_dict():
    result = BinanceUtils.convert_stream_to_dict(RAW_BINANCE_STREAM_TEST)
    assert_stream_to_dict(result)


def test_empty_stream_is_converted_to_empty_dict():
    result = BinanceUtils.convert_stream_to_dict({})

    assert result == {}


def assert_stream_to_dict(expected_dict: dict):
    assert expected_dict["last_operation_time"] == "1678538039999"
    assert expected_dict["market"] == "BTCUSDT"
    assert expected_dict["volume"] == 146.24541
    assert expected_dict["open"] == 20075.7
    assert expected_dict["close"] == 20101.39
    assert expected_dict["high"] == 20102.05
    assert expected_dict["low"] == 20074.95
