import boto3
import os
import uuid
import logging
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError


def new_post(event, context):
    data = event['data']
    if 'text' not in data or "voice" not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    recordId = str(uuid.uuid4())

    voice = data["voice"]
    text = data["text"]

    # Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    table.put_item(
        Item={
            'id': recordId,
            'text': text,
            'voice': voice,
            'status': 'PROCESSING'
        }
    )

    # Sending notification about new post to kafka

    try:
        producer = KafkaProducer(bootstrap_servers='kafka.kubeless:9092')
        producer.send('new-post', recordId)
    except KafkaError as e:
        print e
        logging.error("error %s" % str(e))
        raise e
    finally:
        producer.close()

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({'id': recordId})
    }

    return response
