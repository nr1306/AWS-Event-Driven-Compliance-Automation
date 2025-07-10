import json
import boto3

def extractVolumeId(volume_arn):
    arn_parts = volume_arn.split(':')
    return arn_parts[-1].split('/')[-1]

def lambda_handler(event, context):
    volume_arn = event['resources'][0]
    volume_id = extractVolumeId(volume_arn)

    client = boto3.client('ec2')

    response = client.modify_volume(
        VolumeId=volume_id, # volume time we need
        VolumeType='gp3',
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }