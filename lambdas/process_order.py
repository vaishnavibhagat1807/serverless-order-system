def lambda_handler(event, context):
    print("Processing order:", event)
    return {"status": "processed"}
