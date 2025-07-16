import openai
import base64
import os
import schedule
import time
import json

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

# Load OpenAI API Key
openai.api_key = os.getenv('OPEN_API_KEY')

# Define Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# List of customers' email addresses
customer_emails = ['jasonpresher@att.net', 'customer2@example.com']

def create_email_content():
    # Use ChatGPT to create the content
    response = openai.Completion.create(
        engine="gpt-4",
        prompt="Act as a highly skilled email creator capable of writing fluently in English. Write a short email about Medicare updates for this month.",
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    email_content = response.choices[0].text.strip()
    return email_content

def create_message(to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(service, user_id, message):
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Email sent to {message["to"]}')
        return sent_message
    except Exception as error:
        print(f'An error occurred: {error}')
        return None

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def send_monthly_email():
    service = authenticate_gmail()
    subject = "Monthly Medicare Update"
    email_content = create_email_content()

    for customer_email in customer_emails:
        message = create_message(customer_email, subject, email_content)
        send_email(service, 'me', message)

# Schedule to send once a month
schedule.every().month.do(send_monthly_email)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
