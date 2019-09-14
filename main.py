import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from DTabs import tabs

# read in data
df = pd.read_csv("data/Data_From_1K0Slice_Integratedpm0p1.csv", names=["x", "y", "z"])
x_unique = df.x.unique()
y_unique = df.y.unique()

# create z coordinate to use
# - adding a minimum value
new_z = df.z.copy()
new_z.loc[new_z < 0] = 0

# - adding a maximum value (0.057 tends to work (eliminates 3-actual values))
#  - here I am going to put a much smaller thresold value
max_val = 0.025
new_z.loc[new_z > max_val] = max_val

# Data for the Heat Map
trace_heatmap = go.Heatmap(
                    z=np.array(new_z).reshape(-1, (len(df.x.unique()))),
                    showscale=False,
                    colorscale = [
                        [0, 'rgb(0, 0, 0)'],         # black
                        [0.1, 'rgb(153, 51, 255)'],  # purple
                        [0.2, 'rgb(51, 51, 255)'],   # blue
                        [0.3, 'rgb(51, 153, 255)'],  # light blue
                        [0.4, 'rgb(51, 255, 255)'],  # teal
                        [0.5, 'rgb(51, 255, 153)'],  # light green
                        [0.6, 'rgb(51, 255, 51)'],   # green
                        [0.7, 'rgb(153, 255, 51)'],  # yellow green
                        [0.8, 'rgb(255, 255, 51)'],  # yellow
                        [0.9, 'rgb(255, 153, 51)'],  # orange
                        [1, 'rgb(255, 51, 51)']      # red
                    ],
                )

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

    tabs,

    # Heat Map Row
    dbc.Row([

        # left col
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

            ], id="slider-stuff")

        ], width=6),

        # right col
        dbc.Col([
            dcc.Graph(id="graph-cross-section")
        ], width=6)
    ])

])


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


# update slider
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
        x_label = "Y-Values"
    else:
        print("slider value =", slider_value)
        print("number of unique y values = ", len(y_unique))
        new_df = df[df.y == y_unique[slider_value]]
        y_cross = new_df.z
        x_cross = new_df.x
        x_label = "X-Values"

    # heatmap figure
    figure=go.Figure(
        data=[trace_heatmap, go.Scatter(x=x, y=y, marker={"color": "red"})],
        layout=go.Layout(
            title='Intensity',
            #autosize=True,
            #width=700,
            #height=700,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
    )

    return figure, {'data': [go.Scatter(x=x_cross, y=y_cross)],
                    'layout':{
                        'title':'Cross Section',
                        #autosize=True,
                        #width=700,
                        #height=700,
                        'paper_bgcolor':'rgba(0,0,0,0)',
                        'plot_bgcolor':'rgba(0,0,0,0)'
                    }}, slider_value


if __name__ == '__main__':
    app.run_server(debug=True)

## Wondering how this gets updated