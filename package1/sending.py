import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os.path
import email
import glob


def sending_email():
    want_results = input('Do you want to receive your results by email? (Y/N) ').upper().strip()

    if want_results == 'Y':
        os.environ['sender_password'] = 'sender_password'
        os.environ['sender_email'] = 'sender_email'

        # For this function to work you need to unable the settings here: https://myaccount.google.com/lesssecureapps
        if 'sender_password' not in os.environ:
            raise ValueError('You must enter a password')
        elif 'sender_email' not in os.environ:
            raise ValueError('You must enter an email')


        #For the next 2 lines of code to work you need to create those two variables in os.environ
        sender_email = os.environ['sender_email']
        sender_password = os.environ['sender_password']

        receiver = input('Write your email: ').strip()
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

        image_path = ''.join(glob.glob('../data/results/*.jpg'))
        if os.path.exists(image_path):
            img_data1 = open(image_path, 'rb').read()
            image1 = MIMEImage(img_data1, name=os.path.basename(image_path))
            msg.attach(image1)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        print('Go check your email inbox, there you have it!')

        server.close()

    else:
        print('Thanks for participating!')
