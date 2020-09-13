import pandas as pd
import numpy as np
import datetime
import basic_music_stats

cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content', 'day']

df = pd.read_csv(r"cleaned_apple_data.csv")



def remove_dupes_inplace(lst):
    """helper function for earworm"""
    for i in range(len(lst)-1,0,-1):
        if lst[i] == lst[i-1]:
            del lst[i]
    return lst



def earworm(df, song: str) -> bool:
    """
    returns true if a song is considered an earworm or not

    song must be the format of the column 'content' in the dataframe
    """
    # get a dataframe of just the content in question for analysis
    df = df[df['content'] == song]
    # build frequency by looping thru and building frequency list from datetimes
    dates = []
    for index, row in df.iterrows():
        date = str(row['year']) + ', ' + str(row['month']) + ', ' + str(row['day'])
        dates.append(date)
    # get rid of dupes inplace as to keep order
    dates = remove_dupes_inplace(dates)
    # get all dates assuming that there are days the song wasn't played in the dates list
    # TODO:: bro clean this up
    start = dates[0].replace(', ', '-')
    end = dates[-1].replace(', ', '-')
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
    dates_generated = [start_date + datetime.timedelta(days=x) for x in range(0, (end_date-start_date).days)]
    all_dates_generated = []
    for d in dates_generated:
        cleaned = str(d.strftime('%Y-%m-%d')).split('-') # .replace('-', ', ')
        cleaned[1] = str(int(cleaned[1]))
        cleaned = cleaned[0] + ', ' + cleaned[1] + ', ' + cleaned[2]
        all_dates_generated.append(cleaned)

    frequency = []
    # find frequency
    for d in all_dates_generated:
        if d not in dates:
            plays = 0
            frequency.append(plays)
        else:
            d = d.split(',')
            df_date = df[(df['year'] == int(d[0])) & (df['month'] == int(d[1])) & (df['day'] == int(d[2]))]
            plays = len(df_date)
            frequency.append(plays)
    # now the frequency list matches the index of date, the date doesn't matter now that the frequency list exists
    earworms = []
    return earworms


def longest_streak(df):
    """finds the song with the longest n-day streak"""
    pass



earworm(df, 'memphis, ag club')
