# import random
# for i in range(25):
#   print(random.randint(40,100))

import plotly.graph_objects as go
import pandas as pd
import numpy as np
import csv
import os

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders


def display(id,data):
  fig = go.Figure(data=go.Scatterpolar(
    r=data,
    theta=['Computer','Physics','Chemistry', 'Biology','Maths','Python'],
    fill='toself'
  ))
  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True
      ),
    ),
    showlegend=False
  )
  fig.write_image("results/SpiderChart/"+str(id)+".png")

def mergeMarks(subName):
  if i[0] in subName.values:
    temp_rows= [list(row) for row in subName.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subName.values[t][3])+",")
  else: 
    f.write("NA,")

def sendMailTO():
  sender_address = 'sdlcgen@gmail.com' #put ur mailid

  sender_pass = 'SDLCGEN1234' #ur mailpass
  # list of reciver email_id to the mail

  li = ['ragulperi@gmail.com','amanvkalaskar@gmail.com','gracej755@gmail.com']

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
  Regards, 
      Mark Analyser'''
      message.attach(MIMEText(mail_content, 'plain'))
      filename = 'results/studentMarks.csv'

      with open(filename, "rb") as attachment:
  # MIME attachment is a binary file for that content type "application/octet-stream" is used
          part = MIMEBase("application", "octet-stream")
          part.set_payload(attachment.read())
      encoders.encode_base64(part)

  

      part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

  

  # attach the instance 'part' to instance 'message'

      message.attach(part)

      s = smtplib.SMTP('smtp.gmail.com', 587)

      s.starttls()

      s.login(sender_address, sender_pass)

      text = message.as_string()

      s.sendmail(sender_address, reciver_mail, text)

      s.quit()

      print('Mail Sent')


#create a file for results
if not os.path.exists('results'):
    os.makedirs('results')
    os.mkdir('results/SpiderChart')


ComputerMarks = open('dataset/Computer.csv', 'r')

# Create a dataframe from csv
df = pd.read_csv('dataset/Computer.csv',)
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]
# print(df)
f = open("results/studentMarks.csv", "w")
f.write("studentID,studentNAME,studentEMAIL,Computer,Physics,Chemistry,Biology,Maths,Python,Average\n")
for i in list_of_rows:
  # print(i)
  for j in i:
    # print(j)
    f.write(str(j).strip()+",")

  subPhy = pd.read_csv('dataset/Physics.csv', delimiter=',')
  mergeMarks(subPhy)
  
  subChe = pd.read_csv('dataset/Chemistry.csv', delimiter=',')  
  mergeMarks(subChe)

  subBio = pd.read_csv('dataset/Biology.csv', delimiter=',')  
  mergeMarks(subBio)
  
  subMat = pd.read_csv('dataset/Maths.csv', delimiter=',')  
  mergeMarks(subMat)

  subPy = pd.read_csv('dataset/Python.csv', delimiter=',')  
  mergeMarks(subPy)
    
  f.write("\n")
f.close()

data = pd.read_csv('results/studentMarks.csv', index_col=False)
final = pd.DataFrame(data)

for i in range(final.shape[0]):
  display(final.iloc[i,0],final.iloc[i,3:9])

col = final.loc[: , "Computer":"Python"]
final['Average'] = col.mean(axis=1)
# final = final.sort_values(by = 'studentID')
print(final)

final.to_csv("results/studentMarks.csv")

teacher = {'Teacher_Name':['Badri', 'Prithvi', 'Bharat', 'Ajay','Abhishek','Vivek'],
           'Teacher_Email':['badri@ltts.com', 'prithvi@ltts.com', 'Bharat@ltts.com', 'ajay@ltts.com', 'abhishek@ltts.com','vivek@ltts.com'],
           'Subject':['Computer','Physics',  'Chemistry','Biology','Maths','Python']}

subStats = pd.DataFrame(teacher)


# print(final.loc[: , "Computer":"Maths"].mean())

subStats["Average"] = list(final.loc[: , "Computer":"Python"].mean())
subStats["Max"] = list(final.loc[: , "Computer":"Python"].max())
subStats["Min"] = list(final.loc[: , "Computer":"Python"].min())
subStats["Total"] = list(final.loc[: , "Computer":"Python"].sum())
# print(final.loc[final[['Computer']].idxmax()],"studentID")
# print(final.index[final["Computer"]])
print(subStats)
subStats.to_csv('results/SubjectStats.csv')
sendMailTO()