#!/usr/bin/python

import boto3
import sys

ec2 = boto3.client('ec2')

ec2.stop_instances(
    InstanceIds=[(sys.argv[1])]
    )
