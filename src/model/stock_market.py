from dataclasses import dataclass, astuple
from decimal import Decimal


@dataclass
class StockMarket:
    low: float
    high: float
    open: float
    close: float
    volume: float
    market: str
    last_operation_time: str

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
