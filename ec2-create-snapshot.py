import boto3

ec2 = boto3.resource('ec2')

volumeid = raw_input("Enter a volume ID to snapshot: ")

ec2.create_snapshot(
	VolumeId=volumeid,
	Description='Backed up by boto3',
	TagSpecifications=[
		{
			'ResourceType': 'snapshot',
			'Tags': [
				{
					'Key': 'Name',
					'Value': volumeid
				},
			]
		},
	]
)

print("Done.")
