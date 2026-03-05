
import json
import boto3
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):

    body = json.loads(event['body'])

    item = {
        "id": str(uuid.uuid4()),
        "data": body.get("data")
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data stored",
            "item": item
        })
    }
