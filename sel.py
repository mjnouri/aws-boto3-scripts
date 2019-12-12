import boto3

ec2 = boto3.resource('ec2')

print("Welcome to Simple EC2 Launcher.")
print("")
print("1 = Windows Server 2016")
print("2 = Windows Server 2019")
print("3 = Ubuntu")
print("4 = CentOS 7")
print("5 = Amazon Linux 2")
userosselection = raw_input("Choose your Operating System: ")

print("")

print("1 - t3.medium - 2 CPU, 4 GB RAM")
print("2 - m5.large  - 2 CPU, 8 GB RAM")
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

userpublicip = raw_input("What IP should have access to the EC2: ")
print("")

print("You selected " + os + " with an AMI ID of " + ami + " to run on a " + instancetype + " instance type, and only " + userpublicip + " will have ICMP and SSH access to the EC2.")

print("")

vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')
vpc.wait_until_exists()
vpc.create_tags(
	Tags=[
		{
			"Key": "Name",
			"Value": "Test VPC"
		}
	]
)
print("VPC created with ID " + vpc.id + ".")
print("")

ig = ec2.create_internet_gateway()
print("Internet Gateway created with ID " + ig.id + ".")
print("")

vpc.attach_internet_gateway(InternetGatewayId=ig.id)
print("Internet Gateway " + ig.id + " attached to VPC " + vpc.id + ".")
print("")

route_table = vpc.create_route_table()
print("Route table created with ID " + route_table.id + ".")
print("")

route = route_table.create_route(
	DestinationCidrBlock='0.0.0.0/0',
	GatewayId=ig.id
)
print("Route 0.0.0.0/0 created under Route Table " + route_table.id + ".")
print("")

subnet = ec2.create_subnet(CidrBlock='192.168.1.0/24', VpcId=vpc.id)
print("Subnet created with ID " + subnet.id + ".")
print("")

route_table.associate_with_subnet(SubnetId=subnet.id)
print("Subnet ID " + subnet.id + " associated with Route Table " + route_table.id + ".")
print("")

sec_group = ec2.create_security_group(
	GroupName='Test Security Group',
	Description='Test Security Group',
	VpcId=vpc.id
)
print("Security Group created with ID " + sec_group.id + ".")
print("")

sec_group.authorize_ingress(
	CidrIp=userpublicip,
	IpProtocol='icmp',
	FromPort=-1,
	ToPort=-1
)

sec_group.authorize_ingress(
	CidrIp=userpublicip,
	IpProtocol='tcp',
	FromPort=22,
	ToPort=22
)

print("Opened ICMP and SSH to " + userpublicip + " on Security Group ID " + sec_group.id + ".")
print("")

print("Launching EC2...")
print("")

instance = ec2.create_instances(
	ImageId=ami,
	InstanceType=instancetype,
	MinCount=1,
	MaxCount=1,
	KeyName='coretest',
	NetworkInterfaces=[
		{
			'SubnetId': subnet.id,
			'DeviceIndex': 0,
			'AssociatePublicIpAddress': True,
			'Groups': [sec_group.group_id]
		}
	],
	TagSpecifications=[
		{
			'ResourceType': 'instance',
			'Tags': [
				{
					'Key': 'Name',
					'Value': os
				},
			]
		},
	]
)
instance[0].wait_until_running()
print("EC2 Instance launched with instance ID " + instance[0].id + ".")
print("")

raw_input("Press enter to terminate EC2 instance: " + os + " ...")
ec2instanceids = [instance[0].id]
ec2.instances.filter(InstanceIds = ec2instanceids).terminate()
print ("")

print ("EC2 instance ID " + instance[0].id + " terminated.")
print ("")
