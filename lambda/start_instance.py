import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    ec2.start_instances(InstanceIds=['i-xxxxxxxxxxxxxx'])  # Replace with your actual instance ID
    return {
        'statusCode': 200,
        'body': 'EC2 instance starting...'
    }
