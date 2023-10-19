import json
import os
import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext


logger = Logger()

EVENT_BUS_ARN = os.environ["EVENT_BUS_ARN"]

event_client = boto3.client("events")


@logger.inject_lambda_context(log_event=False, clear_state=True)
def lambda_handler(event, _: LambdaContext):
    '''Lambda handler for the Ingestion Lambda function.
    This function is triggered by the IoT Rule and receives the IoT event, 
    which is then sent to the EventBridge event bus.'''

    response = event_client.put_events(
        Entries=[
            {
                'Detail': json.dumps(event),
                'DetailType': 'scan-event',
                'Source': 'iot.ingestion',
                'EventBusName': EVENT_BUS_ARN
            }
        ]
    )
