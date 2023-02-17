from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_s3_notifications as s3n,
    # aws_sqs as sqs,
)
from constructs import Construct

class AwsPlaygroundStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwsPlaygroundQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        s3 = _s3.Bucket(self, 'testing-bucket')

        lamb = _lambda.Function(self, 'testing-lambda', runtime=_lambda.Runtime.PYTHON_3_7, handler='lambda_handler.main', code=_lambda.Code.from_asset('./lambda'))

        notification = s3n.LambdaDestination(lamb)

        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
