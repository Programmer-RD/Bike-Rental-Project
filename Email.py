import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def m(sub, bod):
    msg = MIMEMultipart()
    msg['From'] = "go2testcode@gmail.com@gmail.com"
    msg['To'] = "ranugagamage@gmail.com"
    msg['subject'] = sub
    msg.attach(MIMEText(bod))
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login("go2testcode@gmail.com", "Ranuga2008")
        try:
            server.sendmail("go2testcode@gmail.com", "ranugagamage@gmail.com", msg.as_string())
        except:
            server.sendmail("go2testcode@gmail.com", "ranugagamage@gmail.com", msg.as_bytes())
        server.close()
        return True
    except Exception as e:
        print(" > Something went wrong.... \n > The error is " + str(e))
        return False
