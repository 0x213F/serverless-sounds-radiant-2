import os


def main(args):
    '''
    '''
    sid = os.getenv('TWILIO_ACCOUNT_SID')
    token = os.getenv('TWILIO_AUTH_TOKEN')

    return {
        "body": "hello world"
    }
