import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

sns = boto3.client('sns')
TOPIC_ARN = "arn:aws:sns:ap-south-1:586337033262:order-notification"

def lambda_handler(event, context):
    print("Full event:", event)

    for record in event['Records']:
        print("Processing record:", record)

        order = json.loads(record['body'])
        print("Order data:", order)

        item = {
            "orderId": str(order["orderId"]),
            "item": str(order.get("item", "")),
            "status": str(order.get("status", "CREATED"))
        }

        print("Final item to insert:", item)

        table.put_item(Item=item)

        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=f"Order {item['orderId']} processed"
        )


      
