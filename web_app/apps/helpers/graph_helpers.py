import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

from web_app.app import app
from web_app.add_paths import path

df = pd.read_csv(path + "/web_app/apps/data/data.csv")

dates = list(df['Date'].unique())

COLORS = {
    'background': '#1e1e2a',
    'text': '#77d1d6',
}


def pH_graph(date=dates[0]):
    X = df[df['Date'] == date]['DateTime'].apply(pd.to_datetime)
    Y = 'pH'
    return {
        'data': [
            {
                'x': X,
                'y': df[df['Date'] == date][Y],
                'name': 'pH',
                'marker': {
                    'color': '#ff9d76',
                    # 'size': 10,
                }
            },
        ],
        'layout': {
            'title': 'pH During the Day',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 14]
            },
        }
    }


def nutrients_graph(date=dates[0]):
    X = df[df['Date'] == date]['DateTime'].apply(pd.to_datetime)
    Y = df[df['Date'] == date]
    return {
        'data': [
            {
                'x': X,
                'y': Y['Protein.AF'],
                'name': 'Protein',
                'mode':'lines',
                'marker': {
                    'color': '#ff9d76',
                    # 'size': 0,
                }
            },
            {
                'x': X,
                'y': Y['FAME.Lipids.AF'],
                'name': 'Lipids',
                'mode':'lines',
                'marker': {
                    'color': '#a3f7bf',
                    # 'size': 0,
                }
            },
            {
                'x': X,
                'y': Y['Carbohydrates.AF'],
                'name': 'Carbohydrates',
                'mode':'lines',
                'marker': {
                    'color': '#05dfd7',
                    # 'size': 0,
                }
            }
        ],
        'layout': {
            'title': 'Nutrients during the Day',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 75]
            },
        }
    }


def light_energy_graph(date=dates[0]):
    X = df[df['Date'] == date]['DateTime'].apply(pd.to_datetime)
    Y = df[df['Date'] == date]
    return {
        'data': [
            {
                'x': X,
                'y': Y['GlobalLightEnergy(W.m2)'],
                'name': 'Global Light Energy',
                'mode':'lines',
                'marker': {
                    'color': '#ff9d76',
                    # 'size': 10,
                }
            },
        ],
        'layout': {
            'title': 'Global Light Energy (W.m2)',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 700]
            },
        }
    }


def temp_graph(date=dates[0]):
    X = df[df['Date'] == date]['DateTime'].apply(pd.to_datetime)
    Y = df[df['Date'] == date]
    df['Temp(C)'] = df['Temp(C)'].apply(lambda x: x + 2.45)
    return {
        'data': [
            {
                'x': X,
                'y': Y['Temp(C)'],
                'name': 'Temperature',
                'mode':'lines',
                'marker': {
                    'color': '#ff9d76',
                    # 'size': 10,
                }
            },
        ],
        'layout': {
            'title': 'Temperature (C)',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 50]
            },
        }
    }


def afdw_graph(date=dates[0]):
    X = df[df['Date'] == date]['DateTime'].apply(pd.to_datetime)
    Y = df[df['Date'] == date]
    return {
        'data': [
            {
                'x': X,
                'y': Y['AFDW (g/L)'],
                'name': 'AFDW',
                'mode':'lines',
                'marker': {
                    'color': '#ff9d76',
                    # 'size': 10,
                }
            },
        ],
        'layout': {
            'title': 'AFDW (g/L)',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 1]
            },
        }
    }


def do_graph(date=dates[0]):
    X = df[df['Date'] == date]['DateTime'].apply(pd.to_datetime)
    Y = df[df['Date'] == date]
    return {
        'data': [
            {
                'x': X,
                'y': Y['DO (mg.L)'],
                'name': 'DO',
                'mode':'lines',
                # 'type':'bar',
                'marker': {
                    'color': '#ff9d76',
                    # 'size': 10,
                }
            },
        ],
        'layout': {
            'title': 'DO (mg.L)',
            'showlegend': False,
            'colorscale': 'balance',
            'legend': {
                'x': 0,
                'y': 1.0
            },
            'plot_bgcolor': COLORS['background'],
            'paper_bgcolor': COLORS['background'],
            'font': {
                'color': COLORS['text']
            },
            'transition': {
                'duration': 1500
            },
            'yaxis': {
                'range': [0, 35]
            },
        }
    }
