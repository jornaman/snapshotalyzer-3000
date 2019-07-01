import boto3
##import sys
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

## @ is called a decorator in Python
@click.command()
def list_instances():
    ## in Python called a doc string
	"List EC2 instances"
	for i in ec2.instances.all():
		##print(i)
		print(', '.join((
			i.id,
			i.instance_type,
			i.placement['AvailabilityZone'],
			i.state['Name'],
			i.public_dns_name)))
			
	return

if __name__ == '__main__':
    ##print(sys.argv)
    list_instances()
    