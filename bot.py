import logging
import sonrai.platform.aws.arn

log = logging.getLogger()

def run(ctx):
    x = 'hi there'
    print(f"{x}, {0/0}")