import os
import boto3
from ...domain.ses_repository import ISesRepository


class SesRepository(ISesRepository):

    def send(self, email, subject, body_html):
        sender = 'Marlon Inga Cahuana <marlonricslim@gmail.com>'
        client = boto3.client('ses',
                              region_name=os.getenv('AWS_REGION'),
                              aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                              aws_secret_access_key=os.getenv('AWS_SECRET_KEY'))
        client.send_email(
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': body_html,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=sender
        )
