AWS boto3 python scripts

sel.py - Simple EC2 Launcher - Prompts user with a menu to select a desired operating system and instance type, then enter your public IP, and Simple EC2 Launcher creates and configures a VPC, internet gateway, route table, subnet, security group, and EC2 giving only your IP remote access. SEL then begins to delete resources after you continue so you don't have to manually delete resources.

ec2-display-instances.py - Prompts user with a menu to display all, running, or stopped EC2 instances.

/left-mfa-at-home - Replaced mobile phone and didn't move over IAM virtual MFA over. Conveniently had a locked down Amazon Linux 2 EC2 running with Administrator account access for scripting across the environment. Deleted MFA device with scripts, logged into the console, listed, deactivated, and deleted old MFA and created a new one.
