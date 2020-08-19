import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from web_app.app import app

DEPARTMENTS = ["Water", "Air", "Fire", "Earth", "Space"]
dropdownOptions = [{'label': dept, 'value': dept} for dept in DEPARTMENTS]

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H1(
                    children="ANALYTICS",
                    id="dashboard_title",
                ),
            ], className="col"),

            html.Div([
                html.Div([
                    dcc.Dropdown(
                        options=dropdownOptions,
                        id="selectDepartment",
                        style={
                            'width': '100%',
                        }
                    ),
                ],
                    className="container deptDropdown",
                )
            ], className="col")
        ], className="row"),

        html.Div([
            html.Div([
                html.Div([
                    "Frequency of Complaints"
                ],
                    className="divDisplay")
            ],
                className="col container"
            ),
            html.Div([
                html.Div([
                    "Frequency of Keywords"
                ],
                    className="divDisplay")
            ],
                className="col container"
            ),
        ], className="row"),

        html.Div([
            html.Div([
                html.Div([
                    "Keywords"
                ],
                    className="divDisplay")
            ],
                className="col-4 container"
            ),
            html.Div([
                html.Div([
                    "Tweets related to those specific keywords"
                ],
                    className="divDisplay")
            ],
                className="col-8 container"
            ),
        ], className="row"),

        html.Div([
            html.Button([
                dcc.Link('DASHBOARD', href='/apps/dashboard')
            ],
                id='btnPageChange',
            ),
        ], className='row justify-content-start')
    ], className="container justify-content-center")
])
