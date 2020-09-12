import pandas as pd
from collections import Counter
import datetime


cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content']

df = pd.read_csv(r"cleaned_apple_data.csv")


# top songs of all time
def top_songs(df, count: int) -> Counter:
    content = df['content'].to_list()
    most_common = Counter(content).most_common(count)
    return most_common


# gets the top count songs for a given year
def top_songs_year(df, year: int, count: int) -> Counter:
    df = df[df['year'] == year]
    return top_songs(df, count)


# top artists of all time
def top_artists(df, count: int) -> Counter:
    content = df['Artist Name'].to_list()
    most_common = Counter(content).most_common(count)
    return most_common


# gets the top count artists for a given year
def top_artists_year(df, year: int, count: int) -> Counter:
    df = df[df['year'] == year]
    return top_artists(df, count)


# split df into dict of dfs by year
def split_years(df) -> dict:
    years = set(df['year'].to_list())
    dfs = {}
    for year in years:
        dfs[year] = df[df['year'] == year]
    return dfs


# get the total minutes of a dataframe (useful in other functions)
def total_minutes(df) -> int:
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


# get total minutes in given year
def year_minutes(df, year: int) -> int:
    df = df[df['year'] == year]
    return total_minutes(df)


# get total minutes in given month in year
def month_minutes(df, year: int, month: int) -> int:
    df = df[df['year'] == year]
    df = df[df['month'] == month]
    return total_minutes(df)


# return the top songs and minutes listened of an artist in your library
def artist_stats(df, artist: str) -> dict:
    artist_stats = {}
    artist = artist.lower()
    df = df[df['Artist Name'] == artist]
    songs = set(df['Content Name'].to_list())
    top_songs = Counter(df['Content Name'].to_list()).most_common(len(songs))
    minutes = total_minutes(df)
    artist_stats['top_songs'] = top_songs
    artist_stats['artist_minutes'] = minutes
    return artist_stats
