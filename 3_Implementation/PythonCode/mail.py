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