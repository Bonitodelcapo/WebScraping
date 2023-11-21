import imaplib
import email
from email.header import decode_header
from twilio.rest import Client

# Your email credentials
email_address = "youremail@example.com"
password = "yourpassword"

# Connect to the email server (e.g., Gmail)
mail = imaplib.IMAP4_SSL("imap.example.com")

# Log in to your email account
mail.login(email_address, password)

# Select the mailbox where you want to check for emails
mail.select("inbox")

# Search for all unseen emails
status, email_ids = mail.search(None, "UNSEEN")

# Fetch the latest unseen email
latest_5_email_id = email_ids[0].split()[-5::1]
for email_id in latest_5_email_id:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    email_message = email.message_from_bytes(msg_data[0][1])
# Get the sender and subject
    sender = email_message["From"]
    subject = email_message["Subject"]



if subject == "WBS":
    if "desired_sender@example.com" in sender:  # Replace with the actual sender's email
        # Send WhatsApp message using Twilio (explained in the next step)
        pass
    else:
        print("Email received from an unauthorized sender.")


# Twilio credentials
twilio_sid = "your_twilio_sid"
twilio_token = "your_twilio_token"

# Initialize Twilio client
client = Client(twilio_sid, twilio_token)

# Send a WhatsApp message
message = client.messages.create(
    body="You received an email with subject 'WBS'",
    from_="whatsapp:+1234567890",  # Your Twilio WhatsApp number
    to="whatsapp:+0987654321"  # Your WhatsApp number
)
# Close the email connection
mail.logout()
print("WhatsApp message sent.")

