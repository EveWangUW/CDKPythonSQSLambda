import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_python_v2.cdk_python_v2_stack import CdkPythonV2Stack


def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonV2Stack(app, "cdk-python-v2")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })
