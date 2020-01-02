import boto3

ec2 = boto3.resource('ec2')

print("Welcome to EC2 Viewer")
print("")
print("1 - View all EC2 instances.")
print("2 - View running EC2 instances.")
print("3 - View stopped EC2 instances.")
userfilterselection = raw_input("Choose your EC2 filter: ")
print("")

if userfilterselection == "1":
	print("Displaying all EC2 instances.")
	for instance in ec2.instances.all():
		print(instance.id, instance.instance_type, instance.state)
	print("")
elif userfilterselection == "2":
	print("Displaying running EC2 instances.")
	instances = ec2.instances.filter(
	Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
	for instance in instances:
		print(instance.id, instance.instance_type, instance.state)
	print("")
elif userfilterselection == "3":
	print("Displaying stopped EC2 instances.")
	instances = ec2.instances.filter(
	Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
	for instance in instances:
		print(instance.id, instance.instance_type, instance.state)
	print("")
else:
	print("Please select a valid menu option.")
	print("")
