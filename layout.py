import plotly.graph_objects as go
from __init__ import intensity

layout_heatmap = go.Layout(
            title='Intensity',
            width=450,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=go.layout.XAxis(showgrid=False, zeroline=False),
            yaxis=go.layout.YAxis(showgrid=False, zeroline=False),
            margin=go.layout.Margin(
                l=50,
                r=0,
                b=0,
                t=70,
                pad=0
            )
        )

layout_cross = go.Layout(
            title="Cross Section",
            width=350,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=go.layout.XAxis(
                showline=True, linewidth=2, linecolor='black', mirror=True,
                showgrid=True, gridwidth=1, gridcolor='LightGrey',
                zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey',
            ),
            yaxis=go.layout.YAxis(
                showline=True, linewidth=2, linecolor='black', mirror=True,
                showgrid=True, gridwidth=1, gridcolor='LightGrey',
                zeroline=True, zerolinewidth=2, zerolinecolor='LightGrey',
            ),
            margin=go.layout.Margin(
                l=50,
                r=20,
                b=25,
                t=65,
                pad=0
            )
        )

# Data for the Heat Map
trace_heatmap = go.Heatmap(
    z=intensity,
    showscale=True,
    colorscale=[
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
