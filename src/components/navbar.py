import dash
from dash import html
import dash_bootstrap_components as dbc
from services.utils import component


@component
def Navbar(vertical=False, **kwargs):
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=vertical,
            pills=True,
            className="nav bg-dark navbar-dark",
        ),
        **kwargs,
    )
