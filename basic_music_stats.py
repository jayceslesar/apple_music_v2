import pandas as pd
from collections import Counter
import datetime


cols_i_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content']

df = pd.read_csv(r"cleaned_apple_data.csv")


# gets the top count songs for a given year
def top_songs_year(df, year, count):
    df_year = df[df['year'] == year]
    content = df_year['content'].to_list()
    most_common = Counter(content).most_common(count)
    return most_common


# gets the top count artists for a given year
def top_artists_year(df, year, count):
    df_year = df[df['year'] == year]
    content = df_year['Artist Name'].to_list()
    most_common = Counter(content).most_common(count)
    return most_common


# split df into dict of dfs by year
def split_years(df):
    years = set(df['year'].to_list())
    dfs = {}
    for year in years:
        dfs[year] = df[df['year'] == year]
    return dfs


# get total minutes in given year
def minutes(df, year):
    df_year = df[df['year'] == year]
    starts = df['Event Start Timestamp'].to_list()
    ends = df['Event End Timestamp'].to_list()
    seconds = 0
    for i in range(len(df_year)):
        start = starts[i].replace('T', ' ')[:18]
        end = ends[i].replace('T', ' ')[:18]
        date_time_start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        date_time_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        delta = date_time_end - date_time_start
        seconds += delta.total_seconds()
    # turn to minutes
    return int(seconds/60)
