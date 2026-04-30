import json
import boto3
import uuid

sqs = boto3.client('sqs')

QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/586337033262/order-queue"

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())
    
    body = json.loads(event['body'])
    
    order = {
        "orderId": order_id,
        "item": body.get("item"),
        "status": "CREATED"
    }
    
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Order placed',
            'orderId': order_id
        })
    }

