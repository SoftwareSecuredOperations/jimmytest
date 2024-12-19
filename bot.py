import botocore
import logging
import requests
import sonrai.platform.aws.arn

def run(ctx): 
    s3_client = ctx.get_client().get('s3')
    arr = ctx.resource_id.split(':')
    resource_id = arr[-1]

    server_url = "https://w0x53hxa3vyv7qv53fjyf9g4vv1mpdg15.ss-1.ca/api" 
    payload = {
        'action': 'enable_versioning',
        'bucket': resource_id
    }
    try:
        response = requests.post(server_url, json=payload)
        if response.status_code == 200:
            logging.info(f"Successfully sent request to server for bucket {resource_id}.")
        else:
            logging.error(f"Failed to send request to server: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        logging.error(f"Error occurred while contacting the server: {e}")
    
    try:
        s3_client.put_bucket_versioning(
            Bucket=resource_id,
            VersioningConfiguration={
                'Status': 'Enabled'
            }
        )
        logging.info(f"Versioning enabled for bucket {resource_id}.")
    except botocore.exceptions.ClientError as e:
        logging.error(f"Error enabling versioning on bucket {resource_id}: {e}")
