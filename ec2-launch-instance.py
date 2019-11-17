import boto3

ec2 = boto3.client('ec2')

ec2.run_instances(
	ImageId='ami-00dc79254d0461090',
	InstanceType='t3a.small',
	MinCount=1,
	MaxCount=1,
	KeyName='coretest',
	SecurityGroupIds=[
		'sg-0cdd323fcfaf0d32c'
	],
	SubnetId='subnet-8274388d',
	TagSpecifications=[
		{
			'ResourceType':'instance',
			'Tags': [
				{
					'Key': 'Name',
					'Value': 'testEC2'
				}
			]
		},
	]
)
