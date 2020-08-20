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
                    html.Div([

                        html.Div([
                            dcc.Textarea(
                                id="complaintText",
                                # value="This is some random complaint",
                                placeholder="Write your complaint here..."
                            ),
                        ], className='row'),
                        html.Div([
                            html.Button([
                                "Submit",
                            ],
                                id='btnSubmitComplaint',
                            ),
                        ], className='row justify-content-end')
                    ], className="container divInput"),

                ],
                    className="divDisplay")
            ],
                className="col container"
            ),
            html.Div([
                html.Div([
                    html.Div([
                        # Title
                        html.Div([
                            html.H3(
                                'Predicted Department',
                                id="predictionTitle",
                            ),
                        ], className="row justify-content-center"),

                        # Prediction Box
                        html.Div([
                            html.Div([
                                html.H4(
                                    'Department',
                                    id='predictionDeptText'
                                )
                            ],
                                id='predictionDept',
                                className='d-flex justify-content-center align-items-center'
                            )
                        ], className='row justify-content-center')
                    ], className='container justify-content-center'),
                ],
                    className="divDisplay")
            ],
                className="col container"
            ),
        ], className="row"),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        # Title
                        html.Div([
                            html.H3(
                                'Keywords',
                                id="keywordsTitle",
                            ),
                        ], className="row justify-content-center"),

                        # Keywords List
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.H4(
                                        'Keyword',
                                        className='keywordText'
                                    ),
                                    html.H4(
                                        'Keyword',
                                        className='keywordText'
                                    ),
                                    html.H4(
                                        'Keyword',
                                        className='keywordText'
                                    ),
                                    html.H4(
                                        'Keyword',
                                        className='keywordText'
                                    ),
                                    html.H4(
                                        'Keyword',
                                        className='keywordText'
                                    )
                                ])
                            ],
                                id='keywordsDiv',
                                className='container d-flex justify-content-center align-items-center'
                            )
                        ], className='row justify-content-center')
                    ], className='container')
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


@ app.callback(
    [Output('predictionDeptText', 'children'), ],
    [Input('btnSubmitComplaint', 'n_clicks')],
    [State('complaintText', 'value')],
)
def update_nutrients_graph(n_clicks, value):
    print("Button Clicked")
    print(value)
    return "D",


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
