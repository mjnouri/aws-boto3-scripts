import boto3

ec2 = boto3.client('ec2')

print("1 = Windows Server 2016")
print("2 = Windows Server 2019")
print("3 = Ubuntu")
print("4 = Centos 7")
print("5 = Amazon Linux 2")
print("")
userosselection = raw_input("Choose your Operating System: ")

print("")

print("1 - t3.medium - 2 CPU, 4 GB RAM")
print("2 - m5.large  - 2 CPU, 8 GB RAM")
print("")
userinstancetypeselection = raw_input("Choose your Instance Type: ")

print("")

if userosselection == "1":
 ami = "ami-08c7081300f7d9abb"
 os = "Windows Server 2016"
elif userosselection == "2":
 ami = "ami-08b11fc5bd2026dee"
 os = "Windows Server 2019"
elif userosselection == "3":
 ami = "ami-04763b3055de4860b"
 os = "Ubuntu"
elif userosselection == "4":
 ami = "ami-02eac2c0129f6376b"
 os = "CentOS 7"
elif userosselection == "5":
 ami = "ami-00068cd7555f543d5"
 os = "Amazon Linux 2"

if userinstancetypeselection == "1":
 instancetype = "t3.medium"
elif userinstancetypeselection == "2":
 instancetype = "m5.large"

print("You selected " + os + " with an AMI ID of " + ami + " to run on a " + instancetype + " instance type.")

print("")

print("Launching EC2...")

ec2.run_instances(
	ImageId=ami,
	InstanceType=instancetype,
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
					'Value': os
				}
			]
		},
	]
)
