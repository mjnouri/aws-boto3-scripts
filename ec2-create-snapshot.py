import boto3

ec2 = boto3.resource('ec2')

volumeid = raw_input("Enter a volume ID to snapshot: ")
snapshotdescription = raw_input("Enter a description for your snapshot: ")

ec2.create_snapshot(
	VolumeId=volumeid,
	Description=snapshotdescription,
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
