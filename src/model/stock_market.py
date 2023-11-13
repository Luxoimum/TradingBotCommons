from dataclasses import dataclass, astuple
from decimal import Decimal
import numpy as np


@dataclass
class Candle:
    low: float
    high: float
    open: float
    close: float
    volume: float
    market: str
    last_operation_time: str

    def __array__(self):
        """
        :return: numpy array of self
        """
        return np.array(astuple(self))

    def __len__(self):  # method for compatibility with arrays of self
        """
        :return: length of self
        """
        return astuple(self).__len__()

    def __getitem__(self, item):  # method for compatibility with arrays of self
        """
        :param item: index of the item to get
        :return: item at index item
        """
        return astuple(self).__getitem__(item)

    def to_dict(self) -> dict:
        """
        :return: dict representation of self
        """
        return {
            "last_operation_time": str(self.last_operation_time),
            "market": self.market,
            "volume": Decimal(str(self.volume)),
            "open": Decimal(str(self.open)),
            "close": Decimal(str(self.close)),
            "high": Decimal(str(self.high)),
            "low": Decimal(str(self.low)),
        }


# Class that contains typical values of a candle and our custom values for a strategy
# !!ref: Startey1 from main strategy document
@dataclass
class StockMarket(Candle):
    sma: float = None
    ema: float = None
    chop: float = None
    rsi: float = None
    long_signal: bool = False
    short_signal: bool = False

    def to_dict(self) -> dict:
        """
        :return: dict representation of self
        """
        super_dict = super().to_dict()
        super_dict.update(
            {
                "ema": Decimal(str(self.ema)),
                "sma": Decimal(str(self.sma)),
                "chop": Decimal(str(self.chop)),
                "rsi": Decimal(str(self.rsi)),
            }
        )
        return super_dict
