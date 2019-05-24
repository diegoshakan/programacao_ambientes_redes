# encoding: utf-8

import os
import smtplib
import imghdr
from email.message import EmailMessage

email_address = 'dih.pokemaster@gmail.com'
email_password = 'pokemon29'

msg = EmailMessage()
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address, email_password)

    subject = 'Vamos testar'
    body = 'Email de teste'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email_address, 'dih.historia@gmail.com', msg)


############################3

# import smtplib
# smtp = smtplib.SMTP('smtp.live.com', 25)
# smtp.starttls()
# smtp.login('diego_shakan@hotmail.com', 'dka292530')
# de = 'diego_shakan@hotmail.com'
# para = ['dih.historia@gmail.com']
# msg = (f'''Olá! Fazendo um teste
# From: {de}
# To: {para}
# Subject: SempreUpdate
# Email de teste do SempreUpdate.''')
# (de, ','.join(para))
# smtp.sendmail(de, para, msg)
# smtp.quit()

# import simplemail
# simplemail.Email(
#     smtp_server = "smtp.gmail.com:587",
#     smtp_user = "dihpokemaster@gmail.com",
#     smtp_password = "pokemon29",
#     from_address = "dihpokemaster@gmail.com",
#     to_address = "dih.historia@gmail.com",
#     subject = u"This is the subject with umlauts (ÖÄÜß)",
#     message = u"This is the short message body with umlauts (ÖÄÜß)."
# ).send()

# def send(to,subject,message=""):
#     e=simplemail.Email(
#         smtp_server='smtp.gmail.com:587',
#         smtp_user='dihpokemaster@gmail.com',
#         smtp_password='pokemon29',
#         use_tls=True,
#         from_address='dihpokemaster@gmail.com',
#         to_address=to,
#         subject=subject,
#         message=message).send()

# send('dih.historia@gmail.com', 'Teste de Email chegado', 'espero que tenha dado certo.')