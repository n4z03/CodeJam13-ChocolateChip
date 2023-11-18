import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import logging

def send_email(target_email, html_file_path):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = "chocolate_chip_reminder@outlook.com"
    TO_EMAIL = "marachljll@gmail.com"
    PASSWORD = "oqjoayjmaoqboowi" #getpass.getpass("HackathonHotties2023")

    message = MIMEMultipart("alternative")
    message['Subject'] = "Chocolate Chip Reminder"
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL
    message['Cc'] = FROM_EMAIL
    message['Bcc'] = FROM_EMAIL

    html = ""
    with open(html_file_path, "r") as file:
        html = file.read()

    html_part = MIMEText(html, 'html')
    message.attach(html_part)

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
    smtp.quit()

if __name__ == "__main__":

    while True:
        try:
            send_email("marachljll@gmail.com", "C:/Users/llimge/Documents/Mcgill Classes/CJAM 2023/CodeJam13/templates/email.html")
            logging.info("Function executed successfully.")
        except Exception as e:
            logging.error(f"Error during function execution: {e}")
        
        time.sleep(300)
    
