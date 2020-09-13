import pandas as pd
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
    dates = remove_dupes_inplace(dates)
    frequency = []
    for d in dates:
        d = d.split(',')
        df_date = df[(df['year'] == int(d[0])) & (df['month'] == int(d[1])) & (df['day'] == int(d[2]))]
        plays = len(df_date)
        print(d, plays)
    earworms = []
    return earworms


def longest_streak(df):
    """finds the song with the longest n-day streak"""
    pass



earworm(df, 'memphis, ag club')
