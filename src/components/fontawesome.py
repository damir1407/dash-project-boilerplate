import dash
from dash import dcc, html


def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=className)
