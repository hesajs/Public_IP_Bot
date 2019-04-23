import smtplib, requests
import datetime as dt
from email.mime.text import MIMEText

def send_email():
    pub_ip = requests.get('https://api.ipify.org').text
    from_addr = 'sender@gmail.com'
    to_addr = 'receiver@gmail.com'
    msg = MIMEText(pub_ip)
    msg['Subject'] = 'Public IP'
    msg['From'] = from_addr
    msg['To'] = to_addr
    print ("Email send to {}".format(to_addr))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(from_addr,'passwordGoesHere')
    server.sendmail(from_addr,to_addr, msg.as_string())
    server.quit()

pub_ip = requests.get('https://api.ipify.org').text
k=['', '']

k[0]=pub_ip
current_time = dt.datetime.now().hour

send_email()

while True:
    check_time = dt.datetime.now().hour
    if (check_time-current_time == 1) or (current_time-check_time== 23):
        k[1] = requests.get('https://api.ipify.org').text

        if(k[0] != k[1]):
            k[0] = k[1]
            send_email()
            
        current_time = check_time