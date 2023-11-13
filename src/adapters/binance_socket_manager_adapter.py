import logging
from binance.streams import BinanceSocketManager, AsyncClient


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class BinanceSocketManagerAdapter:
    def __init__(self):
        self._binance_socket_manager = None

    async def init(self):
        """
        Initialize the BinanceSocketManager
        """
        logger.info("Initializing BinanceSocketManagerAdapter")
        client = await AsyncClient.create()
        self._binance_socket_manager = BinanceSocketManager(client)

    def get_kline_socket(
        self, stream_name="BTCUSDT", interval=AsyncClient.KLINE_INTERVAL_15MINUTE
    ):
        """
        :param stream_name: name of the stream
        :param interval: time interval for market stream
        :return: BinanceSocketManager kline socket
        """
        logger.info("Getting kline socket")
        return self._binance_socket_manager.kline_socket(stream_name, interval=interval)
