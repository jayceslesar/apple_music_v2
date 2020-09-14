import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random
import basic_music_stats
import color_stuff


df = pd.read_csv(r"cleaned_apple_data.csv")
year = 2020
n = 10

def px_top_artist_year(df, year, n):
    colors = []
    x = []
    y = []
    for artist in basic_music_stats.top_artists_year(df, year, n)[::-1]:
        try:
            rgb = random.choice(color_stuff.compute_top_image_colors(artist[0]))
        except:
            rgb = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
        colors.append('rgb(' + str(rgb[0]) + ', ' + str(rgb[1]) + ', ' + str(rgb[2]) + ')')
        x.append(artist[0])
        y.append(artist[1])
    fig = go.Figure(data=[go.Bar(
        x=y,
        y=x,
        orientation='h',
        text=y,
        marker=dict(color=colors)
    )])

    fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    fig.update_layout(
    title="Play Counts for Top 10 Artists in 2020",
    xaxis_title="Plays in 2020",
    yaxis_title="Artist",
    font=dict(
        family="Courier New, monospace",
        size=18
    ))
    fig.update_traces(textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.show()


px_top_artist_year(df, year, n)