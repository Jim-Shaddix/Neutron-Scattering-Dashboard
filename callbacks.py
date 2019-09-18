from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from __init__ import x_unique, y_unique, df
from layout import layout_heatmap, layout_cross, trace_heatmap
from app import app

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
