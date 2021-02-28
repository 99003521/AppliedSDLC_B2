# import random
# for i in range(25):
#   print(random.randint(40,100))

import plotly.graph_objects as go
import pandas as pd
import numpy as np
import csv
import os

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
