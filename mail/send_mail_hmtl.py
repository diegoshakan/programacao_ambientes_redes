# encoding: utf-8

import os
import smtplib
import imghdr
from email.message import EmailMessage

email_address = 'dih.pokemaster@gmail.com'
email_password = ''

msg = EmailMessage()
msg['Subject'] = 'Email com HTML'
msg['From'] = email_address
msg['To'] = 'givanaldoifrn@hotmail.com'

msg.set_content('Nosso IFRN')

msg.add_alternative("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        <p>Nosso IFRN Parnamirim</p>
        <img src="https://i.ytimg.com/vi/_Xjtv5gW7VU/hqdefault.jpg">
        <p>Diego Silva de Araujo</p>
        <p>Graduando em Sistemas Para Internet - IFRN/Par</p>
        <img src="https://fr-br-school.ifrn.edu.br/wp-content/themes/WPSchool/assets/images/ifrnlogo.png" width="300" height="150">
    </body>
</html>""", subtype='html')



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)