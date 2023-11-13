import boto3

from boto3.dynamodb.conditions import Key

from decimal import Decimal

import os

from moto import mock_dynamodb

from src.model.stock_market import StockMarket
from test.constants import (
    STOCK_MARKET_ITEM_TEST,
    KEY_SCHEMA_TEST,
    ATTRIBUTE_DEFINITIONS_TEST,
    PROVISIONED_THROUGHPUT_TEST,
    LAST_OPERATION_TIME_TEST,
    MARKET_TEST,
    STOCK_MARKET_INDEX_TEST,
    ATTRIBUTE_DEFINITIONS_GSI_TEST,
    GLOBAL_SECONDARY_INDEXES_TEST,
)


def setup():
    os.environ["STOCK_MARKET_TABLE"] = "StockMarket"
    os.environ["STOCK_MARKET_INDEX"] = STOCK_MARKET_INDEX_TEST
    os.environ["AWS_DEFAULT_REGION"] = "ap-northeast-1"
    os.environ["AWS_ACCESS_KEY_ID"] = "AWS_ACCESS_KEY_ID"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS_SECRET_ACCESS_KEY"
    os.environ["AWS_SESSION_TOKEN"] = "AWS_SESSION_TOKEN"
    os.environ["AWS_SECURITY_TOKEN"] = "AWS_SECURITY_TOKEN"
    setup_dynamodb_table()


@mock_dynamodb
def setup_dynamodb_table():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.create_table(
        TableName=os.environ["STOCK_MARKET_TABLE"],
        KeySchema=KEY_SCHEMA_TEST,
        AttributeDefinitions=ATTRIBUTE_DEFINITIONS_TEST,
        ProvisionedThroughput=PROVISIONED_THROUGHPUT_TEST,
    )
    table.meta.client.get_waiter("table_exists").wait(
        TableName=os.environ["STOCK_MARKET_TABLE"]
    )

    # Add one record to the table
    table.update(
        AttributeDefinitions=ATTRIBUTE_DEFINITIONS_GSI_TEST,
        GlobalSecondaryIndexUpdates=GLOBAL_SECONDARY_INDEXES_TEST,
    )

    # Add some records to the table
    for _ in range(2):
        table.put_item(Item=STOCK_MARKET_ITEM_TEST)
        table.meta.client.get_waiter("table_exists").wait(
            TableName=os.environ["STOCK_MARKET_TABLE"]
        )


def assert_stock_market_record(stock_market_record):
    assert type(stock_market_record) is StockMarket
    assert stock_market_record.last_operation_time == LAST_OPERATION_TIME_TEST
    assert stock_market_record.market == MARKET_TEST
    assert stock_market_record.volume == 23
    assert stock_market_record.open == Decimal("1000.0")
    assert stock_market_record.close == Decimal("1000.0")
    assert stock_market_record.high == Decimal("1000.0")
    assert stock_market_record.low == Decimal("1000.0")
