# import random
# for i in range(10):
#   print(random.randint(40,100))
import plotly.graph_objects as go

def display(data):
  fig = go.Figure(data=go.Scatterpolar(
    r=data,
    theta=['processing cost','mechanical properties','chemical stability', 'thermal stability',
            'device integration'],
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
  fig.write_image("temp.png")

data=[5,2,3,4,5]
display(data)






