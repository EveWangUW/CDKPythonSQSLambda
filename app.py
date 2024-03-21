#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_python_v2.cdk_python_v2_stack import CdkPythonV2Stack


app = cdk.App()
CdkPythonV2Stack(app, "CdkPythonV2Stack")

app.synth()
