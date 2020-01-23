#!/usr/bin/python

import boto3
import sys

ec2 = boto3.client('ec2')

print(sys.argv[1])

ec2.start_instances(
    InstanceIds = [(sys.argv[1])]
    )
