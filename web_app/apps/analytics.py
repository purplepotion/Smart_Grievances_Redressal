# import sys
# sys.path.append(r'F:\vedant_data\Smart_Grievances_Redressal\web_app\apps\helpers')
from web_app.apps.helpers import sqlquery
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from apps.helpers.graph_helpers import frequency_graph

from app import app

DEPARTMENTS = ['Garbage (SWM)', 'Drainage', 'Electrical', 'Health Kitak', 'Noise Pollution', 'Tree Authority', 'Road', 'Water Supply', 'Road Project(H.O)', 'Bhavan Rachana Department']
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
                        value = DEPARTMENTS[0],
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
                    dcc.Graph(
                    id="frequency_graph",
                    style={
                        'width': '100%',
                        'height': '100%',
                    },
                    figure=frequency_graph(DEPARTMENTS[0])
                )
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
                                     html.Button(
                                         'Keyword',
                                         id='keywordBtn01',
                                         className='keywordBtn'
                                     ),
                                     html.Button(
                                         'Keyword',
                                         id='keywordBtn02',
                                         className='keywordBtn'
                                     ),
                                     html.Button(
                                         'Keyword',
                                         id='keywordBtn03',
                                         className='keywordBtn'
                                     ),
                                     html.Button(
                                         'Keyword',
                                         id='keywordBtn04',
                                         className='keywordBtn'
                                     ),
                                     html.Button(
                                         'Keyword',
                                         id='keywordBtn05',
                                         className='keywordBtn'
                                     ),
                                 ])
                             ],
                                 id='keywordsBtnDiv',
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
                    html.Div(
                    	id = 'keyword_tweet')
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

@ app.callback(
    [Output('keywordBtn01', 'children'),
     Output('keywordBtn02', 'children'), 
     Output('keywordBtn03', 'children'), 
     Output('keywordBtn04', 'children'), 
     Output('keywordBtn05', 'children')],
    [Input('selectDepartment', 'value')],
)
def update_keywords(value):
    keywords_list = sqlquery.top_by_dept(value)
    keywords = [val1 for val1, val2 in keywords_list][:5]
    # print(keywords)
    return keywords

@ app.callback(
    [Output('frequency_graph', 'figure')],
    [Input('selectDepartment', 'value')],
)
def update_frequency_graph(value):
	return frequency_graph(value) #mark

@ app.callback(
    [Output('keyword_tweet', 'children')],
    [Input('keywordBtn01', 'n_clicks')],
    [State('keywordBtn01', 'children')]
)
def update_tweets(n_clicks, value):
	print(n_clicks, value)
	tweets = sqlquery.top_tweets(value)
	# print(tweets)
	children = []
	for tweet in tweets:
		children.append(html.P(tweet[0]))

	return [html.Div(children)]

@ app.callback(
    [Output('keyword_tweet', 'children')],
    [Input('keywordBtn01', 'n_clicks')],
    [State('keywordBtn01', 'children')]
)
def update_tweets(n_clicks, value):
	print(n_clicks, value)
	tweets = sqlquery.top_tweets(value)
	# print(tweets)
	children = []
	for tweet in tweets:
		children.append(html.P(tweet[0]))

	return [html.Div(children)]

@ app.callback(
    [Output('keyword_tweet', 'children')],
    [Input('keywordBtn02', 'n_clicks')],
    [State('keywordBtn02', 'children')]
)
def update_tweets(n_clicks, value):
	print(n_clicks, value)
	tweets = sqlquery.top_tweets(value)
	# print(tweets)
	children = []
	for tweet in tweets:
		children.append(html.P(tweet[0]))

	return [html.Div(children)]

@ app.callback(
    [Output('keyword_tweet', 'children')],
    [Input('keywordBtn03', 'n_clicks')],
    [State('keywordBtn03', 'children')]
)
def update_tweets(n_clicks, value):
	print(n_clicks, value)
	tweets = sqlquery.top_tweets(value)
	# print(tweets)
	children = []
	for tweet in tweets:
		children.append(html.P(tweet[0]))

	return [html.Div(children)]

@ app.callback(
    [Output('keyword_tweet', 'children')],
    [Input('keywordBtn04', 'n_clicks')],
    [State('keywordBtn04', 'children')]
)
def update_tweets(n_clicks, value):
	print(n_clicks, value)
	tweets = sqlquery.top_tweets(value)
	# print(tweets)
	children = []
	for tweet in tweets:
		children.append(html.P(tweet[0]))

	return [html.Div(children)]

@ app.callback(
    [Output('keyword_tweet', 'children')],
    [Input('keywordBtn05', 'n_clicks')],
    [State('keywordBtn05', 'children')]
)
def update_tweets(n_clicks, value):
	print(n_clicks, value)
	tweets = sqlquery.top_tweets(value)
	print(tweets)
	children = []
	for tweet in tweets:
		children.append(html.P(tweet[0]))

	return [html.Div(children)]



