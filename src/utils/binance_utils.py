class BinanceUtils:
    @staticmethod
    def convert_stream_to_dict(stream: dict) -> dict:
        """
        :param stream: stream from Binance kline socket
        :return: dict representation of stream
        """
        if "e" in stream and stream["e"] == "kline":
            return {
                "last_operation_time": stream["k"]["T"],
                "market": stream["k"]["s"],
                "volume": float(stream["k"]["v"]),
                "open": float(stream["k"]["o"]),
                "close": float(stream["k"]["c"]),
                "high": float(stream["k"]["h"]),
                "low": float(stream["k"]["l"]),
            }
        return {}
