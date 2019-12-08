import boto3

iam = boto3.client('iam')

response = iam.list_mfa_devices(
        UserName="name"
        )

print(response)
