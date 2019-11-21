import boto3

ec2 = boto3.client('ec2')

ec2.start_instances(InstanceIds = ['i-0d125db2132efe912'])


