import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import random
import basic_music_stats
import medium_music_stats
import color_stuff


"""
DONE faceted bar graph for top n artists & top n respective songs of the year

TODO line graph for number of songs each month and number of new songs each month

TODO top 10 songs in a list with number of plays

TODO earworms (10 songs that are in earworms that arent in any of the other parts)
"""



def top_n_top_5(df, year, num_artists, num_artist_songs):
    artists = [pair[0] for pair in basic_music_stats.top_artists_year(df, year, num_artists)]
    titles = []
    for artist in artists:
        minutes = basic_music_stats.artist_minutes(df, artist)
        titles.append(artist + ' - ' + str(minutes) + ' minutes total')
    fig = make_subplots(rows=num_artists, cols=1, subplot_titles=(titles))
    for i, artist in enumerate(artists):
        xs, ys = [], []
        data = basic_music_stats.top_artist_songs_year(df, year, artist, num_artist_songs)
        plays = sum([pair[1] for pair in data])
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
        ), row=i+1, col=1)
        fig.update_yaxes(title="Total Plays: " + str(plays), row=i+1, col=1)
    fig.update_layout(showlegend=False, bargap=0.15)
    fig.update_layout(height=275*num_artists, width=150*num_artist_songs,
                  title_text="Top " + str(num_artists) + " Artists and Top " + str(num_artist_songs) + " Songs for each Artist in " + str(year))
    fig.update_layout(font=dict(
        family="Courier New, monospace",
        size=12
    ))
    fig.update_xaxes(title_font=dict(size=4))
    return fig


def line_graph(df, year):
    df = medium_music_stats.get_line_graph_data(df, year)
    fig = go.Figure()
    rgb = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
    color = 'rgb(' + str(rgb[0]) + ', ' + str(rgb[1]) + ', ' + str(rgb[2]) + ')'
    fig.add_trace(go.Scatter(x=df['month'], y=df['plays_per_month'], name='Total Plays a Month', line=dict(color=color, width=2)))
    rgb = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
    color = 'rgb(' + str(rgb[0]) + ', ' + str(rgb[1]) + ', ' + str(rgb[2]) + ')'
    fig.add_trace(go.Scatter(x=df['month'], y=df['unique_plays_per_month'], name='Unique Plays a Month', line=dict(color=color, width=2)))
    fig.update_yaxes(title='Play Counts')
    fig.update_xaxes(title='Month')
    fig.update_layout(title_text='Plays Per Month in ' + str(year))
    return fig


def top_ten_songs(df, year):
    out_str = ""
    data = basic_music_stats.top_songs_year(df, year, 10)
    for song in data:
        out_str += song[0] + ': ' + str(song[1]) + '\n'
    return out_str






df = pd.read_csv(r"cleaned_apple_data.csv")
year = 2020
num_artists = 3
num_artist_songs = 5


top_ten_songs(df, year)
