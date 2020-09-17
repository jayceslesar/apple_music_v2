import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import random
import basic_music_stats
import color_stuff





"""
DONE split bar graph for top 5 artists of the year

TODO line graph for number of songs each month and number of new songs each month

TODO top 10 songs in a list with number of plays

TODO top 10 words listened to

TODO earworms (10 songs that are in earworms that arent in any of the other parts)
"""


df = pd.read_csv(r"cleaned_apple_data.csv")
year = 2020
num_artists = 4
num_artist_songs = 5


def top_n_top_5(df, year, num_artists, num_artist_songs):
    artists = [pair[0] for pair in basic_music_stats.top_artists_year(df, year, num_artists)]
    # del artists[artists.index('idk')]
    fig = make_subplots(rows=num_artists, cols=1, subplot_titles=(artists))
    for i, artist in enumerate(artists):
        xs, ys = [], []
        data = basic_music_stats.top_artist_songs_year(df, year, artist, num_artist_songs)
        songs_to_color = [pair[0][:pair[0].rfind(', ')] for pair in data]
        fixed_songs = []
        for song in songs_to_color:
            if '(' in song:
                fixed_songs.append(song[:song.index('(') - 1])
            else:
                fixed_songs.append(song)
        xs = fixed_songs
        ys = [pair[1] for pair in data]
        colors = []
        for song in songs_to_color:
            try:
                rgb = random.choice(color_stuff.compute_top_image_colors(song + ' - ' + artist))
            except:
                rgb = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
            colors.append('rgb(' + str(rgb[0]) + ', ' + str(rgb[1]) + ', ' + str(rgb[2]) + ')')
        fig = fig.add_trace(go.Bar(
            x=xs,
            y=ys,
            name=artist,
            marker_color=colors
        ), row=i + 1, col=1)
    fig.update_layout(showlegend=False, bargap=0.15)
    fig.update_layout(height=225*num_artists, width=150*num_artist_songs,
                  title_text="Top " + str(num_artists) + " Artists and Top " + str(num_artist_songs) + " Songs for each Artist")
    fig.update_layout(font=dict(
        family="Courier New, monospace",
        size=12
    ))
    fig.update_xaxes(title_font=dict(size=4))
    fig.show()



top_n_top_5(df, year, num_artists, num_artist_songs)










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


