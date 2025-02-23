import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from os import getenv
load_dotenv()

def send_message(message: str, receiver: str) -> bool:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    GMAIL_USERNAME = getenv("GMAIL_USERNAME")
    GMAIL_PASSWORD = getenv("GMAIL_PASSWORD")

    receiver_email = receiver + "@tmomail.net"
    # receiver_email = "8177933636@txt.att.net"
    # receiver_email = "shrekdittakavi@gmail.com"
    body = "http://localhost:1234/patient/" + message + " ."
    subject = "GardenAid Reminder"

    msg = MIMEMultipart()
    msg["From"] = GMAIL_USERNAME
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))


    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        
        server.sendmail(GMAIL_USERNAME, receiver_email, msg.as_string())
        print(f"sent message to {receiver}, link is {body}")

        server.quit()

    except Exception as e:
        print(e)
        return False
    
    return True


if __name__ == '__main__':
    send_message("Take your meds!", "4695920546")