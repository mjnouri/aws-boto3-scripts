import boto3

iam = boto3.client('iam')

response = iam.deactivate_mfa_device(
        UserName="name",
        SerialNumber="arn:aws:iam::123:mfa/name"
        )

print(response)
