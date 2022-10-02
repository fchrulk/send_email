from email.message import EmailMessage
import mimetypes
import smtplib

def send_email(sender, sender_pass, recipients, subject, content, attachments=[]):
    """
    Send email using Gmail via Python

    :param sender: string
        sender's email
    :param sender_pass: string
        sender's password
    :param recipients: list of string
        list of recipients email
    :param subject: string
        email's subject
    :param content: string
        email's body
    :param attachments: list of string
        list of file names. e.g: ['C:/Desktop/attachments_1.pdf', 'attachments_2.xlsx']
    :return: None"""

    message = EmailMessage()
    message['From'] = 'Personal Notification <{}>'.format(sender)
    message['To'] = ', '.join(recipients)
    message['Subject'] = subject
    message.set_content(content)

    for att in attachments:
        mime_type, _ = mimetypes.guess_type(att)
        mime_type, mime_subtype = mime_type.split('/')
        with open(att, 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=att)

    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.login(sender, sender_pass)
    mail_server.send_message(message)
    mail_server.quit()
    print('Email sent to {}!'.format(recipients))