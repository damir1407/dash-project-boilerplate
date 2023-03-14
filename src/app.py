import flask
import dash
import dash_bootstrap_components as dbc
from typing import Any
from dash import html
from core import settings
from components.brand import Brand
from components.navbar import Navbar

external_stylesheets = [
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']

external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']


def create_app(config=settings.DevelopmentConfig()) -> Any:
    dash_app = dash.Dash(__name__,
                         use_pages=True,
                         title=config.TITLE,
                         external_stylesheets=external_stylesheets,
                         external_scripts=external_scripts,
                         server=server)
    return dash_app


# Server definition

server = flask.Flask(__name__)
app = create_app(settings.DevelopmentConfig())

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(Brand(), width="auto"),
                dbc.Col(Navbar(vertical=False), width="auto"),
            ],
            id="header",
            className="bg-dark justify-content-between align-items-center",
        ),
        dbc.Container(dbc.Row(dbc.Col(dash.page_container)), fluid=True),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=settings.DevelopmentConfig().DEBUG)
