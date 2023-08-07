import smtplib

gmail_user = '6278callefuego@gmail.com'
gmail_password = 'walris65'

sent_from = gmail_user
to = ['detmar@peterke.com', "8583952295@tmomail.net"]
subject = 'subj'
body = "a text"

email_text = """\
From: %s
To: %s
%s
%s
""" % (sent_from, ", ".join(to), subject, body)

print(email_text)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(1)
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')