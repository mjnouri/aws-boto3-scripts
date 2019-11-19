import boto3

ec2 = boto3.resource('ec2')

print("Hint: Choose ami-00dc79254d0461090")
userec2amiid = raw_input("Choose your EC2 AMI ID: ")
userec2nametag = raw_input("Choose your EC2 Name tag: ")
userec2instancetype = raw_input("Choose your EC2 instance type: ")
print("")

vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')
vpc.wait_until_available()
vpc.create_tags(
	Tags=[
		{
			"Key": "Name",
			"Value": "test_vpc"
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
	CidrIp='0.0.0.0/0',
	IpProtocol='icmp',
	FromPort=-1,
	ToPort=-1
)

sec_group.authorize_ingress(
	CidrIp='0.0.0.0/0',
	IpProtocol='tcp',
	FromPort=22,
	ToPort=22
)

print("Opened ICMP to 0.0.0.0/0 on Security Group ID " + sec_group.id + ".")
print("")

instance = ec2.create_instances(
	ImageId=userec2amiid,
	InstanceType=userec2instancetype,
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
					'Value': userec2nametag
				},
			]
		},
	]
)
instance[0].wait_until_running()
print("EC2 Instance launched with instance ID " + instance[0].id + ".")
print("")

raw_input("Press enter to terminate EC2 instance: " + userec2nametag + " ...")
ec2instanceids = [instance[0].id]
ec2.instances.filter(InstanceIds = ec2instanceids).terminate()
print ("")
