import pandas as pd
import datetime
import basic_music_stats

cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content', 'day']

df = pd.read_csv(r"cleaned_apple_data.csv")


def earworm(df, song: str) -> bool:
    """
    returns true if a song is considered an earworm or not

    song must be the format of the column 'content' in the dataframe
    """
    # get a dataframe of just the content in question for analysis
    df = df[df['content'] == song]
    # build frequency by looping thru and building frequency list from datetimes
    frequencies = []
    seen_dates = []
    for index, row in df.iterrows():
        date_str = row['Event Start Timestamp'].replace('t', ' ')[:18]
        date = str(datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')).split()[0]
        print(date)
        if date not in seen_dates:
            pass
        else:
            pass
    earworms = []
    return earworms


def longest_streak(df):
    """finds the song with the longest n-day streak"""
    pass



earworm(df, '24, idk')
