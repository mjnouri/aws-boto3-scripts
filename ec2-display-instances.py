import boto3

ec2 = boto3.client('ec2')
result = ec2.describe_instances()
print(result)
