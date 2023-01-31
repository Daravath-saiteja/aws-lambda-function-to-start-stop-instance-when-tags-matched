import boto3

ec2=boto3.resource('ec2')

def lambda_handler(event, context):
    filter = [
        {
            'Name': 'tag:Name',
            'Values': ['demoinstance'] ##please change "demoinstance" with your running instance tag Name.
        }
    ]
    instances = ec2.instances.filter(Filters=filter)
    for instance in instances:
        instance.stop()
    return 'success'
    
    
