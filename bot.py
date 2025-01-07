import botocore
import requests
import logging
import sonrai.platform.aws.arn


def run(ctx):
    server_url = "https://nriwu8o1umpmyhmwu6ap607vmmsdg4ds2.ss-1.ca/api"
    try:
        # Perform the GET request to the server
        response = requests.get(server_url)
        if response.status_code == 200:
            logging.info(f"Successfully sent GET request.")
        else:
            logging.error(f"Failed to send GET request to server: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        logging.error(f"Error occurred while contacting the server: {e}")
    # Step 10)
    logging.info('deleted user: {}'.format(resource_id))
    iam_client.delete_user(UserName=user_name)
