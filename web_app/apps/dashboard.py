import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

from app import app

layout = html.Div([
    html.Div([
        html.Div([
            html.H1(
                children="DASHBOARD",
                id="dashboard_title",
                className="col"
            ),
        ], className="row"),

        html.Div([
            html.Div([
                html.Div([
                    "TextBox"
                ],
                    className="divDisplay")
            ],
                className="col container"
            ),
            html.Div([
                html.Div([
                    "Department"
                ],
                    className="divDisplay")
            ],
                className="col container"
            ),
        ], className="row"),

        html.Div([
            html.Div([
                html.Div([
                    "Keywords found in the given complaint"
                ],
                    className="divDisplay")
            ],
                className="col-4 container"
            ),
            html.Div([
                html.Div([
                    "Bar graph of probability of departments."
                ],
                    className="divDisplay")
            ],
                className="col-8 container"
            ),
        ], className="row"),

        html.Div([
            html.Button([
                dcc.Link('ANALYTICS', href='/apps/analytics')
            ],
                id='btnPageChange',
            ),
        ], className='row justify-content-end')
    ], className="container justify-content-center")
])

# @ app.callback(
#     [Output('nutrients_graph', 'figure'), ],
#     [Input('dateDropdown', 'value')],
# )
# def update_nutrients_graph(value):
#     if not value:
#         value = dates[0]
#     return nutrients_graph(value),


# @ app.callback(
#     [Output('light_energy_graph', 'figure'), ],
#     [Input('dateDropdown', 'value')],
# )
# def update_light_energy_graph(value):
#     if not value:
#         value = dates[0]
#     return light_energy_graph(value),


# @ app.callback(
#     [Output('temp_graph', 'figure'), ],
#     [Input('dateDropdown', 'value')],
# )
# def update_temp_graph(value):
#     if not value:
#         value = dates[0]
#     return temp_graph(value),


# @ app.callback(
#     [Output('afdw_graph', 'figure'), ],
#     [Input('dateDropdown', 'value')],
# )
# def update_afdw_graph(value):
#     if not value:
#         value = dates[0]
#     return afdw_graph(value),


# @ app.callback(
#     [Output('do_graph', 'figure'), ],
#     [Input('dateDropdown', 'value')],
# )
# def update_do_graph(value):
#     if not value:
#         value = dates[0]
#     return do_graph(value),
