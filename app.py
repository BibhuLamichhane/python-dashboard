import pandas as pd
from dash import Dash, Input, Output, dcc, html

data = (
    pd.read_csv("avocado.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
regions = data["region"].sort_values().unique()
avocado_types = data["type"].sort_values().unique()

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Total Volume"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Avocados Sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Total Volume"],
                                    "y": data["AveragePrice"],
                                    "mode": "markers",
                                    "hovertemplate": (
                                        "$%{y:.2f} for %{x:,.0f} avocados<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Price vs. Volume",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {
                                    "title": "Total Volume",
                                    "type": "log",
                                    "fixedrange": True,
                                },
                                "yaxis": {
                                    "title": "Average Price",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="histogram-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["AveragePrice"],
                                    "nbinsx": 30,
                                    "marker": {"color": "#E12D39"},
                                    "hovertemplate": "$%{x:.2f}<extra></extra>",
                                    "type": "histogram",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Price Distribution",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="heatmap-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "z": data["AveragePrice"],
                                    "x": data["Date"],
                                    "y": data["Total Volume"],
                                    "type": "heatmap",
                                    "colorscale": "Viridis",
                                    "hovertemplate": "$%{z:.2f}<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Price Intensity",
                                    "x": 0.5,
                                    "xanchor": "center",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="boxplot-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "y": data["AveragePrice"],
                                    "type": "box",
                                    "marker": {"color": "#17b897"},
                                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Price Summary",
                                    "x": 0.5,
                                    "xanchor": "center",
                                },
                                "yaxis": {"title": "Average Price", "fixedrange": True},
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="violin-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "y": data["AveragePrice"],
                                    "type": "violin",
                                    "line": {"color": "#E12D39"},
                                    "hoveron": "points",
                                    "hoverinfo": "y",
                                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Price Distribution",
                                    "x": 0.5,
                                    "xanchor": "center",
                                },
                                "yaxis": {"title": "Average Price", "fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="bar-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "bar",
                                    "hovertemplate": "$%{y:.2f}<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.5,
                                    "xanchor": "center",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                
                html.Div(
                    children=dcc.Graph(
                        id="pie-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "labels": ["A", "B", "C", "D"],
                                    "values": [1, 2, 3, 4],
                                    "type": "pie",
                                    "hoverinfo": "label+percent",
                                    "textinfo": "value",
                                    "textposition": "inside",
                                    "marker": {"colors": ["#E12D39", "#17b897", "#F3D8E2", "#F1B0C4"]},
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Pie Chart",
                                    "x": 0.5,
                                    "xanchor": "center",
                                },
                                "colorway": ["#E12D39", "#17b897", "#F3D8E2", "#F1B0C4"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
