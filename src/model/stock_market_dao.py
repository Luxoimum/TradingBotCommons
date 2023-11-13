import logging
import os
import time

from decimal import Decimal

from boto3.dynamodb.conditions import Key

from botocore.exceptions import ClientError

from src.model.stock_market import StockMarket

from src.helpers.dynamodb_helper import dynamodb_resource

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class StockMarketDAO:
    dynamodb = None
    table_name = None
    index_name = None

    def __init__(self):
        self.dynamodb = dynamodb_resource()
        self.table_name = os.environ["STOCK_MARKET_TABLE"]
        self.index_name = os.environ["STOCK_MARKET_INDEX"]

    def get_stock_market_records(self, limit=200, market="BTCUSDT") -> list:
        """
        :param market:
        :param limit:
        :return: list of StockMarket records
        """
        table = self._get_stock_market_table()
        stock_market_items = []
        try:
            logger.info("Try to get %s items", limit)

            # Set the search criteria
            last_operation_time = str(time.time())  # current timestamp

            # Set the KeyConditionExpression and ScanIndexForward parameters
            key_condition_expression = Key("market").eq(market) & Key(
                "last_operation_time"
            ).lt(last_operation_time)

            # Execute the query
            response = table.query(
                IndexName=self.index_name,
                KeyConditionExpression=key_condition_expression,
                ScanIndexForward=False,
                Limit=limit,
            )

            stock_market_items = [
                self._get_stock_market_from_ddb_item(item) for item in response["Items"]
            ]
            logger.info("Items found: %s", len(stock_market_items))
        except ClientError as error:
            logger.error(error)

        return stock_market_items

    def store_stock_market(self, stock_market_record: StockMarket) -> bool:
        """
        :param stock_market_record:
        :return: True if the record is stored, False otherwise
        """
        table = self._get_stock_market_table()
        try:
            logger.info("Try put item: %s", stock_market_record)
            response = table.put_item(Item=stock_market_record.to_dict())
            logger.info("Put successful response: %s", response)
            return response["ResponseMetadata"]["HTTPStatusCode"] == 200
        except ClientError as error:
            logger.error(error)
            return False

    def _get_stock_market_table(self):
        """
        :return: DynamoDB StockMarket table
        """
        logger.info("Using DynamoDB Table: %s", self.table_name)

        return self.dynamodb.Table(self.table_name)

    @staticmethod
    def _get_stock_market_from_ddb_item(ddb_item: dict) -> StockMarket:
        for key, value in ddb_item.items():
            if isinstance(value, Decimal):
                ddb_item[key] = float(value)
        return StockMarket(**ddb_item)
