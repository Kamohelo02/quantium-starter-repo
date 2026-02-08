import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd


# Load and prepare data
def load_data(filepath):
    df = pd.read_csv(filepath)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df


# Create layout with title, radio buttons, and graph
def create_layout():
    return html.Div([
        html.H1("Pink Morsel Sales Visualizer", style={
            'textAlign': 'center',
            'color': 'darkblue',
            'fontFamily': 'Arial'
        }),

        html.Div([
            html.Label("Select Region:", style={'fontSize': '18px', 'marginRight': '10px'}),
            dcc.RadioItems(
                id='region-radio',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all',
                inline=True,
                style={'fontSize': '16px', 'marginBottom': '20px'}
            )
        ], style={'textAlign': 'center', 'marginBottom': '30px'}),

        dcc.Graph(id='sales-chart')
    ], style={'padding': '20px', 'backgroundColor': '#f9f9f9'})


# Create chart based on selected region
def create_chart(df, region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    fig = px.line(filtered_df, x='date', y='sales',
                  title=f'Sales in {region.capitalize()} Region')
    fig.update_xaxes(title='Date')
    fig.update_yaxes(title='Sales ($)')
    fig.update_layout(plot_bgcolor='white', title_font_size=20)
    return fig


# Callback to update chart when region changes
def register_callback(app, df):
    @app.callback(
        Output('sales-chart', 'figure'),
        Input('region-radio', 'value')
    )
    def update_chart(selected_region):
        return create_chart(df, selected_region)


# Main function to run app
def main():
    df = load_data("final_sales.csv")

    app = dash.Dash(__name__)
    app.layout = create_layout()
    register_callback(app, df)

    app.run(debug=True)


if __name__ == '__main__':
    main()