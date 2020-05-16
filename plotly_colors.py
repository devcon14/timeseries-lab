import plotly.graph_objs as go

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [2500, 1053,  3125, 930] 
# colors = ['aliceblue',  'aqua', 'aquamarine', 'darkturquoise']
# colors = ['DarkRed', 'PaleGreen', 'RebeccaPurple', 'MediumPurple']
colors = ['DarkRed', 'PaleGreen', 'AquaMarine', 'MediumPurple']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(colors=colors, 
                           line=dict(color='rgb(100,100,100)', 
                                     width=1)
                          )
              )

fw=go.FigureWidget(data=[trace])
fw.show()