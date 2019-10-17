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

from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from __init__ import x_unique, y_unique, df
from layout import layout_heatmap, layout_cross, trace_heatmap

# update axis drop down
@app.callback([Output('slider-heatmap', 'min'),
               Output('slider-heatmap', 'max'),
               Output('slider-heatmap', 'value'),
               Output('slider-heatmap', 'marks')],
              [Input('dropdown-axis', 'value')])
def update_axis_dropdown(value):

    if value == "x":
        max_val = len(x_unique)-1
    else:
        max_val = len(y_unique)-1

    marks = [10]
    while (marks[-1] + 10) < max_val:
        marks.append(marks[-1] + 10)

    marks = dict(zip(marks, [str(i) for i in marks]))

    return 1, max_val, 1, marks


@app.callback([Output('graph-heatmap', 'figure'),
               Output('graph-cross-section', 'figure'),
               Output('input-axis-value', 'value')],
              [Input('slider-heatmap', 'value')],
              [State('dropdown-axis', 'value')])
def update_slider(slider_value, dropdown_value):

    # red line plot values
    if dropdown_value == "x":
        x = [slider_value] * 2
        y = [0, len(y_unique)-1]
    else:
        x = [0, len(x_unique)-1]
        y = [slider_value] * 2

    # Find cross section plot parameters
    if dropdown_value == "x":
        new_df = df[df.x == x_unique[slider_value]]
        y_cross = new_df.z
        x_cross = new_df.y
    else:
        print("slider value =", slider_value)
        print("number of unique y values = ", len(y_unique))
        new_df = df[df.y == y_unique[slider_value]]
        y_cross = new_df.z
        x_cross = new_df.x

    # heatmap figure
    figure_heatmap=go.Figure(
        data=[trace_heatmap, go.Scatter(x=x, y=y, marker={"color": "green"})],
        layout=layout_heatmap
    )

    # cross-section figure
    figure_cross=go.Figure(
        data=[go.Scatter(x=x_cross, y=y_cross)],
        layout=layout_cross
    )

    return figure_heatmap, figure_cross, slider_value


if __name__ == '__main__':
    app.run_server(debug=True)
