import dash
import dash_core_components as dcc
import dash_html_components as html
import graphs
import pandas as pd


YEAR = 2019
df = pd.read_csv(r"cleaned_apple_data.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

sever = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options



app.layout = html.Div(children=[
    html.H1(children='Apple Music Dashboard'),

    html.Div(children='''
        My Solution to Apple not Having a Rewind.
    '''),

    dcc.Graph(
        id='Top 3 Artists in 2020 and the Top 5 Songs Played',
        figure=graphs.top_n_top_5(df, YEAR, 3, 5)
    ),
    dcc.Graph(
        id='Lines',
        figure=graphs.line_graph(df, YEAR)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)