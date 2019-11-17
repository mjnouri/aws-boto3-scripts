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
print("VPC ID: " + vpc.id + ".")

ig = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=ig.id)
print("Internet Gateway ID: " + ig.id + ".")

route_table = vpc.create_route_table()
route = route_table.create_route(
	DestinationCidrBlock='0.0.0.0/0',
	GatewayId=ig.id
)
print("Route table ID: " + route_table.id + ".")


