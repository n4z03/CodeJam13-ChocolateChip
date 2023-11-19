import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def update_email_html(contact):
    from app import app
    with app.app_context():
        from flask import session
        fobj = open("templates/email-template.html", "r")
        html_str = ""
        for i in fobj:
            html_str += i
        html_tokenized = html_str.split("|")
        for i in range(len(html_tokenized)):
            if html_tokenized[i] == "UserName":
                html_tokenized[i] = session['name'] #user session.name
            elif html_tokenized[i] == "ChipName":
                html_tokenized[i] = contact.name #contact.name
            elif html_tokenized[i] == "Type":
                html_tokenized[i] = contact.type #contact.type
            elif html_tokenized[i] == "Email":
                html_tokenized[i] = contact.email #contact
        html_str = ""
        for i in html_tokenized:
            html_str += i
        print(html_str)
        fobj.close
        fobj = open("templates/email-to-send.html", "w")
        fobj.write(html_str)
        fobj.close
    
        
def update_email_html_quick(contact):

    fobj = open("templates/email-template.html", "r")
    html_str = ""
    for i in fobj:
        html_str += i
    html_tokenized = html_str.split("|")
    for i in range(len(html_tokenized)):
        if html_tokenized[i] == "UserName":
            html_tokenized[i] = "hackingheat" #user session.name
        elif html_tokenized[i] == "ChipName":
            html_tokenized[i] = "recruiterx" #contact.name
        elif html_tokenized[i] == "Type":
            html_tokenized[i] = "professional" #contact.type
        elif html_tokenized[i] == "Email":
            html_tokenized[i] = "companyname@gmailcom" #contact
        elif html_tokenized[i] == "Social Media":
            html_tokenized[i] = "recruiter name" #contact
        elif html_tokenized[i] == "":
            html_tokenized[i] = "companyname@gmailcom" #contact
        
    html_str = ""
    for i in html_tokenized:
        html_str += i
    print(html_str)
    fobj.close
    fobj = open("templates/email-to-send.html", "w")
    fobj.write(html_str)
    fobj.close
    

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
    with open("templates/email-to-send.html", "r") as file:
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
    
    send_email("marachljll@gmail.com")
    send_email("luis.limgenco@mail.mcgill.com")
    
    
