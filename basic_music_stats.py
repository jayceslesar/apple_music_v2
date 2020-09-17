import pandas as pd
from collections import Counter
import datetime


cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content' , 'day']

df = pd.read_csv(r"cleaned_apple_data.csv")


def top_songs(df, n: int) -> Counter:
    """Returns the top n songs in a given library"""
    content = df['content'].to_list()
    most_common = Counter(content).most_common(n)
    return most_common


def top_songs_year(df, year: int, n: int) -> Counter:
    """Returns the top n songs for a library in a given year"""
    df = df[df['year'] == year]
    return top_songs(df, n)


def top_songs_month(df, year: int, n: int) -> Counter:
    """Returns the top n songs for a library in a given year and month"""
    df = df[(df['year'] == year) & (df['month'] == month)]
    return top_songs(df, n)


def top_artists(df, n: int) -> Counter:
    """Returns the top n artists in a given library"""
    content = df['Artist Name'].to_list()
    most_common = Counter(content).most_common(n)
    return most_common


def top_artists_year(df, year: int, n: int) -> Counter:
    """Returns the top n artists for a library in a given year"""
    df = df[df['year'] == year]
    return top_artists(df, n)


def top_artists_month(df, year: int, month: int, n: int) -> Counter:
    """Returns the top n artists for a library in a given year and month"""
    df = df[(df['year'] == year) & (df['month'] == month)]
    return top_artists(df, n)


def total_minutes(df) -> int:
    """Returns the total minutes of a library"""
    starts = df['Event Start Timestamp'].to_list()
    ends = df['Event End Timestamp'].to_list()
    seconds = 0
    for i in range(len(df)):
        start = starts[i].replace('t', ' ')[:18]
        end = ends[i].replace('t', ' ')[:18]
        date_time_start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        date_time_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        delta = date_time_end - date_time_start
        seconds += delta.total_seconds()
    # turn to minutes
    return int(seconds/60)


def year_minutes(df, year: int) -> int:
    """Returns total minutes in given year"""
    df = df[df['year'] == year]
    return total_minutes(df)


def month_minutes(df, year: int, month: int) -> int:
    """Returns total minutes in given month in year"""
    df = df[(df['year'] == year) & (df['month'] == month)]
    return total_minutes(df)


def artist_minutes(df, artist: str) -> int:
    """Returns total minutes for a specific artist"""
    df = df[df['Artist Name'] == artist]
    return total_minutes(df)


def artist_stats(df, artist: str) -> dict:
    """
    More general function for returning bulk stats
    Returns the top songs and minutes listened of an artist in your library
    """
    artist_stats = {}
    artist = artist.lower()
    df = df[df['Artist Name'] == artist]
    songs = set(df['Content Name'].to_list())
    top_songs = Counter(df['Content Name'].to_list()).most_common(len(songs))
    minutes = total_minutes(df)
    artist_stats['top_songs'] = top_songs
    artist_stats['artist_minutes'] = minutes
    return artist_stats

def top_artist_songs_year(df, year: int, artist: str, n: int):
    df = df[(df['year'] == year) & (df['Artist Name'] == artist)]
    return top_songs(df, n)
