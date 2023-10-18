import boto3
import exceptions
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext


logger = Logger()

EVENT_BUS_ARN = os.environ["EVENT_BUS_ARN"]

event_client = boto3.client("events")


@logger.inject_lambda_context(log_event=False, clear_state=True)
def lambda_handler(event, _: LambdaContext):

    # TODO send event with IoT event
