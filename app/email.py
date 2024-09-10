import smtplib
from email.mime.text import MIMEText
from decouple import config


def send_email(subject, message):
    # Read the env variables
    MAIL_RECIPIENT = config("MAIL_RECIPIENT")
    MAIL_FROM = config("MAIL_FROM")
    MAIL_SERVER = config("MAIL_SERVER")
    MAIL_PORT = config("MAIL_PORT", cast=int)
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")

    # Create a MIMEText object with the message content
    email_message = MIMEText(message)

    # Set the email headers
    email_message["Subject"] = subject
    email_message["From"] = f"Domain Tracker <{MAIL_FROM}>"
    email_message["To"] = MAIL_RECIPIENT

    # Connect to the SMTP server
    smtp_server = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)

    # Login to the sender's email account
    smtp_server.login(MAIL_FROM, MAIL_PASSWORD)

    # Send the email
    smtp_server.send_message(email_message)

    # Disconnect from the SMTP server
    smtp_server.quit()


def send_notification_for_domain_expiration(domain, results):
    subject = f"{domain} expiration date has changed"
    message = f"""
        The expiration date for {domain} has changed to {results.expiration_date}.\n\n
        {results}
        """
    try:
        send_email(subject, message)
        print(f"Email notification sent for {domain}.")
    except Exception as e:
        print(f"Error sending email: {e}")
