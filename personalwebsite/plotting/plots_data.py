#Import plotly
import plotly.graph_objects as go
import pandas as pd

#Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html


sales = pd.read_csv('test_data.csv')
fore = pd.read_csv('test_data.csv')
#Initialize the plot
fig_totalsales=go.Figure()
#Add the lines
fig_totalsales.add_trace(go.Scatter(x=sales[sales.columns[0]], y=sales[sales.columns[1]], visible=True, name='Sales'))
# fig_totalsales.add_trace(go.Scatter(x=fore['Date'],y=fore[fore.columns[0]],visible=True, name='Forecast'))
#Add title/set graph size
fig_totalsales.update_layout(title = 'Daily Sales', width=850, height=400)
fig_totalsales.show()


#Create the app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig_totalsales)
])

app.run_server(debug=True, use_reloader=False)