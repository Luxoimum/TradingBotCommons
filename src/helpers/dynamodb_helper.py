import boto3


DDB = None


def dynamodb_resource():
    """
    :return: DynamoDB resource
    """
    # pylint: disable=global-statement
    global DDB  # Using global statement for improving performance
    if not DDB:
        DDB = boto3.resource("dynamodb")
    return DDB
