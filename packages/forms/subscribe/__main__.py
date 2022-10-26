import boto3
import os


def _setup_boto3_client(session):
    try:
        region_name = os.environ['BOTO3_REGION_NAME']
        endpoint_url = os.environ['BOTO3_ENDPOINT_URL']
        aws_access_key_id = os.environ['BOTO3_ACCESS_KEY']
        aws_secret_access_key = os.environ['BOTO3_SECRET_KEY']
    except KeyError:
        return {
            "success": False,
            "message": "Misconfigued environment variables"
        }
    return session.client(
        "s3",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def _add_email_subcriber_using_boto3(session, client, email_address):
    '''
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object
    '''
    client.put_object(
        Bucket="sounds-radiant",
        Key=f"private/email-subscribers/{email_address}",
    )


def main(args):
    boto3_session = boto3.session.Session()
    boto3_client = _setup_boto3_client(boto3_session)
    email_address = args.get("email", "josh@schultheiss.io")
    _add_email_subcriber_using_boto3(boto3_session, boto3_client, email_address)
    return { "status": 200, "message": "Ok" }
