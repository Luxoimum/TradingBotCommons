import logging
import numpy as np
import pandas_ta as ta
from pandas import Series, DataFrame, concat
from src.model.stock_market import Candle, StockMarket
from src.constants.strategy_parameters import StrategyParameters


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class TradingBotStrategyUtils:
    @staticmethod
    def _calc_min_max(data_frame: DataFrame, last_relevant_max: float) -> float:
        window = StrategyParameters.window
        real_window = (window // 2) + (window // 4)
        ema_min_max = ta.ema(close=data_frame["close"], length=real_window)
        stdev = data_frame.ta.stdev(close=ema_min_max, length=real_window)

        if stdev.iloc[stdev.size - 1] >= stdev.iloc[stdev.size - 2]:
            return ema_min_max.iloc[ema_min_max.size - 1]

        return last_relevant_max

    @staticmethod
    def _compute_choppiness(data_frame: DataFrame) -> Series:
        print(data_frame["high"].iloc[-1])
        print(type(data_frame["high"].iloc[-1]))
        return ta.chop(
            high=data_frame["high"],
            low=data_frame["low"],
            close=data_frame["close"],
            length=StrategyParameters.chop_length,
        )

    @staticmethod
    def _compute_ema(data_frame: DataFrame) -> Series:
        return ta.ema(data_frame["close"], timeperiod=StrategyParameters.ema_length)

    @staticmethod
    def _compute_sma(data_frame: DataFrame) -> Series:
        return ta.sma(data_frame["close"], timeperiod=StrategyParameters.sma_length)

    @staticmethod
    def _compute_rsi(data_frame: DataFrame) -> Series:
        return ta.rsi(data_frame["close"], timeperiod=StrategyParameters.rsi_length)

    @staticmethod
    def _compute_cross_sma_ema_long(
        past_candles: np.ndarray, new_candle: Candle
    ) -> bool:
        return (
            past_candles[-1].sma > new_candle.close >= past_candles[-1].ema
            and past_candles[-1].ema < past_candles[-1].sma
        )

    @staticmethod
    def _compute_cross_sma_ema_short(
        past_candles: np.ndarray, new_candle: Candle
    ) -> bool:
        return (
            past_candles[-1].sma < new_candle.close <= past_candles[-1].ema
            and past_candles[-1].ema > past_candles[-1].sma
        )

    @staticmethod
    def compute_stock_market_aggregated_data(
        past_candles: DataFrame, new_candle: Candle
    ) -> DataFrame:
        logger.info("new_candle: %s", new_candle)
        new_candle_df = TradingBotStrategyUtils.map_stock_market_list_to_data_frame([new_candle])
        logger.info("new_candle_df: %s", new_candle_df)
        candles = concat([past_candles, new_candle_df])
        candles["sma"] = TradingBotStrategyUtils._compute_sma(candles)
        candles["ema"] = TradingBotStrategyUtils._compute_ema(candles)
        candles["chop"] = TradingBotStrategyUtils._compute_choppiness(candles)
        candles["rsi"] = TradingBotStrategyUtils._compute_rsi(candles)

        return candles

    @staticmethod
    def compute_stock_market_aggregated_data2(
        past_candles: list, new_candle: Candle
    ) -> list:
        stock_market_dict = {**new_candle.to_dict()}
        if past_candles:
            stock_market_dict["ema"] = 5.0
            stock_market_dict["sma"] = 5.0
            stock_market_dict[
                "long_signal"
            ] = TradingBotStrategyUtils._compute_cross_sma_ema_long(
                past_candles, new_candle
            )
            stock_market_dict[
                "short_signal"
            ] = TradingBotStrategyUtils._compute_cross_sma_ema_short(
                past_candles, new_candle
            )
        else:
            stock_market_dict["ema"] = new_candle.close
            stock_market_dict["sma"] = new_candle.close
            stock_market_dict["long_signal"] = False
            stock_market_dict["short_signal"] = False

        past_candles.append(StockMarket(**stock_market_dict))
        return past_candles

    @staticmethod
    def map_stock_market_list_to_data_frame(past_candles: list) -> DataFrame:
        return DataFrame(
            {
                "open": np.array(
                    [stockMarket.open for stockMarket in past_candles],
                    dtype=np.float64,
                ),
                "close": np.array(
                    [stockMarket.close for stockMarket in past_candles],
                    dtype=np.float64,
                ),
                "high": np.array(
                    [stockMarket.high for stockMarket in past_candles],
                    dtype=np.float64,
                ),
                "low": np.array(
                    [stockMarket.low for stockMarket in past_candles],
                    dtype=np.float64,
                ),
            },
            index=np.array(
                [stockMarket.last_operation_time for stockMarket in past_candles],
                dtype=str,
            ),
        )
