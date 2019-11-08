import plotly.graph_objects as go
from __init__ import intensity


def xaxis_title(title):
    xaxis = go.layout.xaxis.Title(
        text=title
    )
    return xaxis


def yaxis_title(title):
    yaxis = go.layout.yaxis.Title(
        text=title
    )
    return yaxis

layout_heatmap = go.Layout(
    title=go.layout.Title(text="Intensity", xref="paper", x=0.5),
    width=450,
    height=350,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=go.layout.XAxis(showgrid=False, zeroline=False,
                          title=xaxis_title("X axis")),
    yaxis=go.layout.YAxis(showgrid=False, zeroline=False,
                          title=yaxis_title("Yaxis")),
    margin=go.layout.Margin(
        l=50,
        r=0,
        b=0,
        t=70,
        pad=0
    )
)

layout_cross = go.Layout(
    title=go.layout.Title(text="Cross Section", xref="paper", x=0.5),
    width=380,
    height=350,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=go.layout.XAxis(
        showline=True, linewidth=2, linecolor='black', mirror=True,
        showgrid=True, gridwidth=1, gridcolor='LightGrey',
        zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey',
        title=xaxis_title("X axis")
    ),
    yaxis=go.layout.YAxis(
        showline=True, linewidth=2, linecolor='black', mirror=True,
        showgrid=True, gridwidth=1, gridcolor='LightGrey',
        zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey',
        title=yaxis_title("Y axis")
    ),
    margin=go.layout.Margin(
        l=50,
        r=20,
        b=0,
        t=65,
        pad=0
    )
)

# Data for the Heat Map
trace_heatmap = go.Heatmap(
    z=intensity,
    showscale=True,
    colorscale=[
        [0, 'rgb(0, 0, 0)'],  # black
        [0.1, 'rgb(153, 51, 255)'],  # purple
        [0.2, 'rgb(51, 51, 255)'],  # blue
        [0.3, 'rgb(51, 153, 255)'],  # light blue
        [0.4, 'rgb(51, 255, 255)'],  # teal
        [0.5, 'rgb(51, 255, 153)'],  # light green
        [0.6, 'rgb(51, 255, 51)'],  # green
        [0.7, 'rgb(153, 255, 51)'],  # yellow green
        [0.8, 'rgb(255, 255, 51)'],  # yellow
        [0.9, 'rgb(255, 153, 51)'],  # orange
        [1, 'rgb(255, 51, 51)']  # red
    ],
)
