#!/usr/bin/env python3

from aws_cdk import core

from my_cdk.my_cdk_stack import MyCdkStack


app = core.App()
MyCdkStack(app, "my-cdk")

app.synth()
