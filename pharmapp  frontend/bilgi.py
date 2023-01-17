from email.message import EmailMessage
import ssl
import smtplib
def bilgilendir(drug):
    email_sender = "hasanyazgu@gmail.com"
    email_password = "lsvr xyhf ozmr mvhh"
    email_receiver = "mmcaldag1@gmail.com"
    drug=drug.capitalize()
    subject = "Ani İlaç Satımı Artışı"
    body= f"{drug} Satımında Ani artış olmuştur"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    ctx = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ctx) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())