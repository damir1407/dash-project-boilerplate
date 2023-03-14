import dash
from dash import dcc, html
from services.utils import component
from .fontawesome import fa
from core.settings import BaseConfig as settings


@component
def Brand(**kwargs):
    return html.Header(
        className="brand",
        children=dcc.Link(
            href="/",
            children=html.H1([fa("fa-solid fa-chart-column"), settings().TITLE]),
        ),
        **kwargs,
    )
