import boto3

ec2 = boto3.client('ec2')

print("Hint: Choose ami-00dc79254d0461090 for Amazon Linux 2")
useramiid = raw_input("Enter the AMI ID you wish to use: ")
userinstancetype = raw_input("Enter an instance type: ")
print("Launching EC2 instance using AMI ID " + useramiid + " with instance type " + userinstancetype)

ec2.run_instances(
	ImageId=useramiid,
	InstanceType=userinstancetype,
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
