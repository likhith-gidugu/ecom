import smtplib
from email.message import EmailMessage  
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('likhithgidugu036@gmail.com','sjrs btex ydhx zxcx')
    msg=EmailMessage()
    msg['FROM']='likhithgidugu036@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
