import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from DTabs import tabs
"""
This file initializes the application and formats 
how the application gets displayed.
"""

# create application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = html.Div([


    # title
    html.Div([

        html.A(
            html.Img(src="assets/images/rosslab_logo.png", id="logo"),
            href="http://www.rosslabcsu.com/"
        ),

        html.H1("Neutron Scattering", id="title"),
        html.A(
            html.P("View on Github", id="github-text"),
            href="https://github.com/Jim-Shaddix/Neutron-Scattering-Dashboard",
            id="github-link"
        ),
        html.Div(className="clr")
    ], id="banner"),

    html.Div(className="clr"),

    # All Content
    dbc.Container([
        dbc.Row([

            # tabs
            dbc.Col([
                tabs
            ], width="auto", lg=6, xl=4),

            # plots
            dbc.Col([
                dbc.Row([
                    # heat map
                    dbc.Col([

                        # heat-map
                        dcc.Graph(
                            id="graph-heatmap"
                        ),

                        # slider
                        html.Div([

                            dcc.Slider(
                                id="slider-heatmap",
                                value=1,
                                updatemode="drag"
                            )

                        ], id="div-slider")

                    ], md=6, lg=12, xl=6),

                    # cross section
                    dbc.Col([
                        dcc.Graph(id="graph-cross-section")
                    ], md=6, lg=12, xl=6)

                ])
            ], width="auto", lg=6)
        ]),
    ], fluid=True)

])


if __name__ == '__main__':
    app.run_server(debug=True)
