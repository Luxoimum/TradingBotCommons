# py test for binance utils
# Path: test/utils/binance_utils_test.py
# Compare this snippet from test/utils/binance_utils_test.py:
# # pylint: disable=missing-docstring
# from src.utils.binance_utils import BinanceUtils
#
# from test.constants import RAW_BINANCE_CANDLE_ITEM_TEST
#

# pylint: disable=missing-docstring
from src.utils.trading_bot_strategy_utils import TradingBotStrategyUtils
from pandas import DataFrame
from test.constants import CLOSE, HIGH, LOW


df = DataFrame({"close": CLOSE, "high": HIGH, "low": LOW})


def test_calc_min_max():
    result = TradingBotStrategyUtils._calc_min_max(df, df["close"].iloc[0])
    assert result == 26051.747679381988


def test_choppiness():
    result = TradingBotStrategyUtils._compute_choppiness(df)
    print(result)
    assert result.iloc[result.size - 1] == 57.81961964651698


def test_rsi():
    result = TradingBotStrategyUtils._compute_rsi(df)
    print(result)
    assert result.iloc[result.size - 1] == 37.053192870005134


def test_ema():
    result = TradingBotStrategyUtils._compute_ema(df)
    print(result)
    assert result.iloc[result.size - 1] == 26030.204943065015


def test_sma():
    result = TradingBotStrategyUtils._compute_sma(df)
    print(result)
    assert result.iloc[result.size - 1] == 26029.7609375
