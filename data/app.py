import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
# load and prepare sales
def load_data(filepath):
    df = pd.read_csv(filepath)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df

# create line chart of sales over time
def create_sales_chart(df):
    fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Sales ($)")
    return fig

# build dash app layout
def build_layout(fig):
    return html.Div([
        html.H1("Pink Morsel Sales Visualizer"),
        dcc.Graph(figure = fig)
    ])

# main function to run the dash app
def main():
    df = load_data("final_sales.csv")
    fig = create_sales_chart(df)

    app = dash.Dash(__name__)
    app.layout = build_layout(fig)

    app.run(debug=True)


if __name__ == "__main__":
    main()