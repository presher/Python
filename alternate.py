import openai
import os
import base64
import schedule
import time
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import json
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

from decrypt import decrypt_api_key

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API Key
decrypted_api_key = decrypt_api_key()
openai.api_key = decrypted_api_key

# Gmail Scopes and Client ID
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

# Function to authenticate Gmail API
def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            raise Exception("Token file is missing or invalid. Authenticate again.")
    return build('gmail', 'v1', credentials=creds)

# Function to generate email content using OpenAI GPT-4
def generate_email_content():
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a highly skilled ad copywriter specializing in Medicare-related content."},
            {"role": "user", "content": "Please write a professional email related to Medicare updates for the month."}
        ],
        max_tokens=300
    )
    
    # The response from ChatCompletion will be in a different structure
    email_content = response['choices'][0]['message']['content'].strip()
    print(email_content)
    return email_content

# Function to create and send an email
def send_email(service, recipient, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = recipient
    message['from'] = "your_email@gmail.com"
    message['subject'] = subject
    
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {
        'raw': encoded_message
    }
    
    try:
        sent_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f"Message sent to {recipient}: {sent_message['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")

# Function to send emails to all customers
def send_monthly_emails():
    # Load customer data
    with open('customers.json') as f:
        customers = json.load(f)
    
    # Generate email content
    email_content = generate_email_content()
    
    # Authenticate Gmail
    service = authenticate_gmail()
    
    # Send email to each customer
    for customer in customers:
        subject = f"Monthly Medicare Updates - {time.strftime('%B %Y')}"
        send_email(service, customer['email'], subject, email_content)

# Schedule the task to run once a month
# schedule.every().days(30).do(send_monthly_emails)
scheduler = BlockingScheduler()
scheduler.add_job(send_monthly_emails, 'cron', day=3, hour=11, minute=6)

if __name__ == "__main__":
    while True:
        # schedule.run_pending()
        scheduler.start()
        time.sleep(86400)  # Sleep for one day to avoid unnecessary CPU usage
