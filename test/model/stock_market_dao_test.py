# pylint: disable=missing-docstring
import os

from src.model.stock_market_dao import StockMarketDAO
from src.model.stock_market import StockMarket
from moto import mock_dynamodb

from test.conftest import setup, assert_stock_market_record

from test.constants import STOCK_MARKET_ITEM_TEST, MARKET_TEST

import boto3


@mock_dynamodb
def test_get_stock_market_records_call_succeed():
    setup()
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["STOCK_MARKET_TABLE"])
    response = table.scan()

    stock_market_dao = StockMarketDAO()
    stock_market_records = stock_market_dao.get_stock_market_records(
        limit=1, market=MARKET_TEST
    )

    assert stock_market_records is not None
    assert type(stock_market_records) is list
    assert len(stock_market_records) == 1

    assert_stock_market_record(stock_market_records[0])


@mock_dynamodb
def test_store_stock_market_record_call_succeed():
    setup()
    stock_market_dao = StockMarketDAO()
    stock_market_object = StockMarket(**STOCK_MARKET_ITEM_TEST)

    result = stock_market_dao.store_stock_market(stock_market_object)

    assert result is True
