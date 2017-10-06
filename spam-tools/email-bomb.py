import smtplib
import random
import email.utils
from email.mime.text import MIMEText

# structure users
recipients = ['bchung1@luc.edu', 'afila@luc.edu']
author = 'stopspammingme517@gmail.com'

# structure message
# message body
msg = MIMEText('''
Hello,

On one or more of the afternoons listed below, an email from your email address was flagged as a spam message attempting to employ a phishing scam while impersonating the "System Administrator Management Team" or the "Office of Information Technology" of Loyola.

The email provided a link for Loyola users to "verify" their accounts, but directed them to a fake Outlook-style page (e.g. "http://outllookoffice793.weebly.com/").

The aforementioned dates include, but are not limited to:
July 26th, 2017
September 15th, 2017

Under the circumstances, a retaliation act was thought necessary. We apologize for the delay and any inconvenience this stream of emails is causing.

Enjoy.

In addendum, if you find yourself in the position where you did not send these messages please fill out the form here: 
''')
# define recipients
msg['To'] = email.utils.formataddr(('Recipient', recipients))
# define author
msg['From'] = email.utils.formataddr(('Author', author))
# define subject
msg['Subject'] = 'Request for Maintenance #%d' % random.randint(0, 1000)

# gmail credentials for temp acct
username = author
pwd = 'epsilon;'

# set up SSL secure server
server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# show communications with server
server_ssl.set_debuglevel(True)

# identify ourselves to SSL server to expose features
server_ssl.ehlo()

try:
    # check for TLS availability
    if server_ssl.has_extn('STARTTLS'):
        server_ssl.starttls()
        server_ssl.ehlo()
    else:
        print "TLS encryption unavailable on this server..."
    # login to temp acct
    server_ssl.login(username, pwd)
    for x in range(0,5):
        # send mail
        server_ssl.sendmail(author, recipients, msg.as_string())
        print "message #%d sent" % (x+1)
finally:
    server_ssl.quit()
