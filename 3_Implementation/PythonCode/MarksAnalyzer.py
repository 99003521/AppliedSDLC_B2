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
  fig.write_image("results/"+str(id)+".png")

#create a file for results
if not os.path.exists('results'):
    os.makedirs('results')


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
  if i[0] in subPhy.values:
    temp_rows= [list(row) for row in subPhy.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subPhy.values[t][3])+",")
  else: 
    f.write("NA,")

  subChe = pd.read_csv('dataset/Chemistry.csv', delimiter=',')  
  if i[0] in subChe.values:
    temp_rows= [list(row) for row in subChe.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subChe.values[t][3])+",")
  else:
    f.write("NA,")

  subBio = pd.read_csv('dataset/Biology.csv', delimiter=',')  
  if i[0] in subBio.values:
    temp_rows= [list(row) for row in subBio.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subBio.values[t][3])+",")
  else:
    f.write("NA,")
  
  subMat = pd.read_csv('dataset/Maths.csv', delimiter=',')  
  if i[0] in subMat.values:
    temp_rows= [list(row) for row in subMat.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subMat.values[t][3])+",")
  else:
    f.write("NA,")


  subPy = pd.read_csv('dataset/Python.csv', delimiter=',')  
  if i[0] in subPy.values:
    temp_rows= [list(row) for row in subPy.values]
    for row in temp_rows:
      if i[0] in row:
        t=temp_rows.index(row)
        break
    f.write(str(subPy.values[t][3])+",")
  else:
    f.write("NA,")
    
  f.write("\n")
f.close()


data = pd.read_csv('results/studentMarks.csv', index_col=False)
final = pd.DataFrame(data)
print(final)

# print(final["Physics"].mean())
print(final.iloc[0,3:7].mean())
print(final.iloc[0,0])
# print(final.shape[0])
# display(final.iloc[0,0],final.iloc[0,3:8])
for i in range(final.shape[0]):
  display(final.iloc[i,0],final.iloc[i,3:8])
  
# df["Average"] = final.iloc[0,3:final.shape[1]].mean()
# print(df)
col = final.loc[: , "Computer":"Python"]
final['Average'] = col.mean(axis=1)
print(final)
final.to_csv("results/studentMarks.csv")

