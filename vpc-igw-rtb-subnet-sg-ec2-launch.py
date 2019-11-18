import boto3

ec2 = boto3.resource('ec2')

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

ig = ec2.create_internet_gateway()
print("Internet Gateway created with ID " + ig.id + ".")

vpc.attach_internet_gateway(InternetGatewayId=ig.id)
print("Internet Gateway " + ig.id + " attached to VPC " + vpc.id + ".")

route_table = vpc.create_route_table()
print("Route table created with ID " + route_table.id + ".")

route = route_table.create_route(
	DestinationCidrBlock='0.0.0.0/0',
	GatewayId=ig.id
)
print("Route 0.0.0.0/0 created under Route Table " + route_table.id + ".")

subnet = ec2.create_subnet(CidrBlock='192.168.1.0/24', VpcId=vpc.id)
print("Subnet created with ID " + subnet.id + ".")

route_table.associate_with_subnet(SubnetId=subnet.id)
print("Subnet ID " + subnet.id + " associated with Route Table " + route_table.id + ".")








# when creating our subnet, make sure the route table created here is the one attached
# probably is since we aren't working with the default route table make when making the VPC


# find way to make 0.0.0.0/0 a variable and call it when you need it
# find a way to have user input EC2 instance type for customization
# find a way to make a prod/env conditional parameter
# add these to issues
