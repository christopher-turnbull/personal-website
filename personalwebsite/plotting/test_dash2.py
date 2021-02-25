# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# from dash.dependencies import Input, Output
#
# ###################
# # APPLICATION DASH
# ###################
# #
# # https://thinkinfi.com/integrate-plotly-dash-in-django/
#
# a = pd.read_csv('test_data.csv')
# b = pd.read_csv('test_data.csv')
#
# app = dash.Dash()
# app.layout = html.Div(children=[
#     html.H1(children='APP NAME', style={'textAlign': 'center'
#                                         }),
#
#     html.Div([
#         dcc.DatePickerRange(
#             id='my-date',
#             min_date_allowed=dt(2015, 8, 5),
#             max_date_allowed=dt(2021, 9, 19),
#             initial_visible_month=dt(2019, 8, 5),
#             start_date=str(dt(2019, 8, 25)),
#             end_date=str(dt(2019, 12, 25))),
#
#         html.Div(id='Text', style={'font-size': '26px'}),
#         dcc.Graph(id='totalsales'),
#     ])
#
#     @ app.callback(
#         [dash.dependencies.Output('totalsales', 'figure'),
#          dash.dependencies.Output('Text', 'children')],
#         [dash.dependencies.Input('my-date', 'start_date'),
#          dash.dependencies.Input('my-date', 'end_date')]
#     )
#
#
# def update_output(start_date, end_date):
#     sales2 = a[(a['transDate_mev'] > start_date) & (a['transDate_mev'] < end_date)]
#     forecast2 = b[(b['Date'] > start_date) & (b['Date'] < end_date)]
#
#     prefix = 'Sales in the period: '
#     totals = str(int(round(sales2['sales'].sum())))
#
#     fig_totalsales = go.Figure()
#     fig_totalsales.add_trace(go.Scatter(x=sales2['transDate_mev'], y=sales2['sales'], visible=True, name='Sales'))
#     fig_totalsales.add_trace(go.Scatter(x=forecast2['Date'], y=forecast2['forecast'], visible=True, name='Forecast'))
#     fig_totalsales.update_layout(title='Daily Sales', width=1350, height=450)
#
#     return fig_totalsales, prefix + totals + '$'
#
#
# app.run_server(debug=True, use_reloader=False)