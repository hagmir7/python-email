import smtplib
from email.message import EmailMessage
import pywhatkit

def email_message(obj, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = obj
    msg['to'] = to
    username = 'hagmir7@gmail.com'
    msg['from'] = username
    password = 'jfpgqzkxetgyjbvo'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()

# if __name__ == '__main__':
#     email_message('hellow Hassan', 'l9lwa you', 'hagmir6@gmail.com')
pywhatkit.sendwhatmsg('+212648382674', 'good morning', 2, 10)