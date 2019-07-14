import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# Generating Plots:

# data for scatter plot
trace_scatter = go.Scatter3d(x=df.x, y=df.y, z=df.z,
                             mode="markers",
                             marker=dict(
                                 color='#FFBAD2',
                                 line=dict(width = 0.01)
                             )
                             )

# Data For Surface Plot
X, Y = np.meshgrid(x_unique, y_unique)
Z = np.array(df.z).reshape((len(y_unique), len(x_unique)))
trace_surface = go.Surface(x=X, y=Y, z=Z)


# --- deleted elements ---
############################


# Footer
html.Div([
    html.H2("Footer"),
    html.P("blah kah saw maw daw. " * 20)
], id="footer", className="box")



# First Row
dbc.Row([

    # Column Left
    dbc.Col([
        dcc.Graph(
            figure=go.Figure(
                data=[trace_scatter],
                layout=go.Layout(
                    title='Scatter Plot',
                    #autosize=True,
                    #width=700,
                    #height=700,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
            ),
        )],
        width=4
    ),

    # column middle
    dbc.Col([
        html.Div([
            html.H2("Description"),
            html.P("lorem blah kabba man sup bro hello. " * 10)
        ],
            className="box",
            id="description"
        )

    ], width=4),

    # Column Right
    dbc.Col([
        dcc.Graph(
            figure=go.Figure(
                data=[trace_surface],
                layout=go.Layout(
                    title='Surface Plot',
                    #autosize=True,
                    #width=700,
                    #height=700,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
            ),
        )],
        width=4
    ),

]),
