#! /mnt/data/Events/TATA Crucible/PhotoBioReactor/env python3

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from add_paths import vedant
from app import app
from apps import dashboard, analytics

app.layout = html.Div([
    dcc.Location(id='url', refresh=False, pathname='/apps/dashboard'),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/dashboard':
        return dashboard.layout
    elif pathname == '/apps/analytics':
        return analytics.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=False)
