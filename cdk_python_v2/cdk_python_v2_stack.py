from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources
)


class CdkPythonV2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create our queue
        queue = sqs.Queue(
            self, "CdkPythonV2Queue",
            visibility_timeout=Duration.seconds(300),
        )

        # create our lambda function
        sqs_lambda=lambda_.Function(self, "SQSLambda",
                                    handler='lambda_handler.handler',
                                    runtime=lambda_.Runtime.PYTHON_3_12,
                                    code=lambda_.Code.from_asset('lambda')
                                    )
        # create our event source
        sqs_event_source = lambda_event_sources.SqsEventSource(queue)

        #add sqs event source to lambda
        sqs_lambda.add_event_source(sqs_event_source)