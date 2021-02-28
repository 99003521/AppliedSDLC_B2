import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders
#The mail addresses and  password

sender_address = 'sdlcgen@gmail.com' #put ur mailid

sender_pass = 'SDLCGEN1234' #ur mailpass
# list of reciver email_id to the mail

li = ['ragulperi@gmail.com','amanvkalaskar@gmail.com']

#[item for item in input("Enter Receiver Mail Address :- ").split()] this is used to take user input of receiver mail id
# getting length of list

length = len(li)
# Iterating the index
# same as 'for i in range(len(list))'
# Here we iterate the loop and send msg one by one to the reciver

for i in range(length):

    X = li[i]
    reciver_mail = X
 print(reciver_mail)
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] =  reciver_mail             #  Pass Reciver Mail Address
    message['Subject'] =  'Mail using python' #The subject line
    mail_content = '''Hi,

    I am your mark analyser. This mail contains the final marksheet and analysed data of the subject modules. PFA
