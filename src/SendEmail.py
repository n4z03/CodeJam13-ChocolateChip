import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def update_email_html(user):
    fobj = open("C:/Users/llimge/Documents/Mcgill Classes/CJAM 2023/CodeJam13/templates/email-template.html", "r")
    html_str = ""
    for i in fobj:
        html_str += i
    html_tokenized = html_str.split("|")
    for i in range(len(html_tokenized)):
        if html_tokenized[i] == "UserName":
            html_tokenized[i] = "Jam jam" #user.name
        elif html_tokenized[i] == "ChipName":
            html_tokenized[i] = "bruh"
        elif html_tokenized[i] == "Type":
            html_tokenized[i] = "ok"
        elif html_tokenized[i] == "Contact":
            html_tokenized[i] = "nice"
    html_str = ""
    for i in html_tokenized:
        html_str += i
    print(html_str)
    
        
    

def send_email(target_email):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = "chocolate_chip_reminder@outlook.com"
    TO_EMAIL = target_email
    PASSWORD = "oqjoayjmaoqboowi" #getpass.getpass("HackathonHotties2023")

    message = MIMEMultipart("alternative")
    message['Subject'] = "Chocolate Chip Reminder"
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL
    message['Cc'] = FROM_EMAIL
    message['Bcc'] = FROM_EMAIL

    html = ""
    with open("C:/Users/llimge/Documents/Mcgill Classes/CJAM 2023/CodeJam13/templates/email.html", "r") as file:
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
    update_email_html(1)
    """
    try:
        send_email("marachljll@gmail.com")
        logging.info("Function executed successfully.")
    except Exception as e:
        logging.error(f"Error during function execution: {e}")
    """
    
