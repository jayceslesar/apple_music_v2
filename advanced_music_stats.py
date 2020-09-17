import pandas as pd
import numpy as np
import itertools
import operator
import datetime
import basic_music_stats


cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content', 'day']

df = pd.read_csv(r"cleaned_apple_data.csv")


def remove_dupes_inplace(lst):
    """helper function for earworm, helps keep dates sorted"""
    for i in range(len(lst)-1,0,-1):
        if lst[i] == lst[i-1]:
            del lst[i]
    return lst


def frequencies(df) -> list:
    """returns frequency list of the first time to the last time a criteria (song/artist) was played    """
    # build frequency by looping thru and building frequency list from datetimes
    dates = []
    for index, row in df.iterrows():
        date = str(row['year']) + ', ' + str(row['month']) + ', ' + str(row['day'])
        dates.append(date)
    # get rid of dupes inplace as to keep order
    dates = remove_dupes_inplace(dates)
    # generate all dates assuming that there are days the song wasn't played in the dates list
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
        cleaned[2] = str(int(cleaned[2]))
        cleaned = cleaned[0] + ', ' + cleaned[1] + ', ' + cleaned[2]
        all_dates_generated.append(cleaned)
    frequency = []
    # find frequency
    for d in all_dates_generated:
        if d not in dates:
            # if there is a date that it isn't played, add the date and 0 plays
            plays = 0
            frequency.append(plays)
        else:
            # add the plays to date, where plays is the size of the dataset on that day
            d = d.split(',')
            df_date = df[(df['year'] == int(d[0])) & (df['month'] == int(d[1])) & (df['day'] == int(d[2]))]
            plays = len(df_date)
            frequency.append(plays)
    # now the frequency list matches the index of date, the date doesn't matter now that the frequency list exists
    return frequency


def determine_avg_streak(df):
    """gets streak statistics for an entire dataframe to use as a metric"""
    all_streaks = []
    for song in list(set(df['content'].to_list())):
        df_content = df[df['content'] == song]
        fs = frequencies(df_content)
        streaks = [list(g) for k, g in itertools.groupby(fs, key=lambda x:x!=0) if k]
        for streak in streaks:
            if len(streak) > 3:
                all_streaks.append(len(streak))
    return (np.mean(all_streaks), np.std(all_streaks))


def earworm(df, song: str, avg_freq: float, std_freq: float) -> bool:
    """will determine if a song is an earworm or not by how fast it picks up and stays there from frequency list"""
    df_song = df[df['content'] == song]
    fs = frequencies(df_song)
    streaks = [list(g) for k, g in itertools.groupby(fs, key=lambda x:x!=0) if k]
    all_streaks = []
    for streak in streaks:
        if len(streak) > 3:
            all_streaks.append(len(streak))
    mean_streak = np.mean(all_streaks)
    # if a streak exists
    if len(streaks) > 0:
        # if the mean streak of this song is greater than the user average streak - x*frequency standard deviation
        if mean_streak > avg_freq - 0.5*std_freq:
            # if the number of plays in the first week is greater than x times the length of the streak
            return True


def longest_song_streak(df, song: str) -> int:
    """finds the specified song with the longest n-day streak"""
    df = df[df['content'] == song]
    fs = frequencies(df)
    streaks = [list(g) for k, g in itertools.groupby(fs, key=lambda x:x!=0) if k]
    streak_lens = [len(i) for i in streaks]
    return max(streak_lens)


def longest_artist_streak(df, artist: str) -> int:
    """finds the specified artist with the longest n-day streak"""
    df = df[df['Artist Name'] == artist]
    fs = frequencies(df)
    streaks = [list(g) for k, g in itertools.groupby(fs, key=lambda x:x!=0) if k]
    streak_lens = [len(i) for i in streaks]
    return max(streak_lens)


df = df[df['year'] == 2020]
freq_stats = determine_avg_streak(df)
avg_freq = freq_stats[0]
std_freq = freq_stats[1]
for song in list(set(df['content'].to_list())):
    if earworm(df, song, avg_freq, std_freq):
        print(song)