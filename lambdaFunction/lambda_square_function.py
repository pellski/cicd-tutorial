import json

def lambda_square_handler(event, context):
    
    data = {
        'output': event['input']*event['input']
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
