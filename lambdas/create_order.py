import json
import uuid

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Order Created',
            'order_id': order_id
        })
    }
