import re
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os.path
import email

from dotenv import load_dotenv, find_dotenv
from os import listdir
from os.path import isfile, join


def sending_email():
    os.environ['sender_password'] = 'enter_yours'
    os.environ['sender_email'] = 'enter_yours'

    # For this function to work you need to unable the settings here: https://myaccount.google.com/lesssecureapps
    if 'sender_password' not in os.environ:
        raise ValueError('You must enter a password')
    elif 'sender_email' not in os.environ:
        raise ValueError('You must enter an email')

    #mypath = '../data/results/'
    #files = [f for f in listdir(mypath) if isfile(join(mypath, f))]


    #For the next 2 lines of code to work you need to create those two variables in os.environ
    sender_email = os.environ['sender_email']
    sender_password = os.environ['sender_password']

    receiver = input('Who do you want to send this mail? ').strip()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()  # So the message will be encripted
        server.ehlo()
        server.login(sender_email, sender_password)

    except:
        print('Connection not working, try again later')

    while not re.match(r"[^@]+@[^@]+\.[^@]+", receiver):
        print("The email you just entered it's not correct")
        receiver = input('Please try again: ')
    print(f'Sending email to {receiver}')

    img_data = open('../data/results/results.png', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Results from billionaires in 2018'
    msg['From'] = sender_email
    msg['To'] = receiver

    text = MIMEText('Below you have your desired results from the analysis of the most billionaires in 2018!')
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('results.png'))
    msg.attach(image)

    server.sendmail(msg['From'], msg['To'] , msg.as_string())

    print('Go check your email inbox, there you have it!')

    server.close()
