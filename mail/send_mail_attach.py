# encoding: utf-8

import os
import smtplib
import imghdr
from email.message import EmailMessage

email_address = 'dih.pokemaster@gmail.com'
email_password = ''

msg = EmailMessage()
msg['Subject'] = 'Segue arquivo de teste anexo!'
msg['From'] = email_address
msg['To'] = 'givanaldoifrn@hotmail.com'
msg.set_content('Foto teste')

with open('brasil.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)