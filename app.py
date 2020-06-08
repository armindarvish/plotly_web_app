#Import plotly and csv
import plotly.graph_objects as go
import csv
from datetime import datetime

sales={'x':[], 'y':[]}
with open('salesdata.csv') as file:
    csvdata = csv.DictReader(file)
    for row in csvdata:
        sales['x'].append(datetime.strptime(row['x'], '%Y-%m-%d'))
        sales['y'].append(float(row['y']))

# print(sales[0])
#Initialize the plot
fig_totalsales=go.Figure()
#Add the lines
fig_totalsales.add_trace(go.Scatter(x=sales['x'], y=sales['y'], visible=True, name='Sales'))
# fig_totalsales.add_trace(go.Scatter(x=fore['Date'],y=fore[fore.columns[0]],visible=True, name='Forecast'))
#Add title/set graph size
fig_totalsales.update_layout(title = 'Daily Sales', width=850, height=400)
fig_totalsales.show()


#Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
#Create the app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig_totalsales)
])

app.run_server(debug=True, use_reloader=False)
