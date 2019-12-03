import boto3

iam = boto3.client('iam')

response = iam.delete_virtual_mfa_device(
        SerialNumber="arn:aws:iam::123:mfa/name"
        )

print(response)
