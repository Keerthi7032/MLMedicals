import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff


labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

trace = go.Pie(labels=labels, values=values)

layout = go.Pie(labels=labels, values=values)
py.plot(layout, auto_open=False, output_type='div')