import pandas as pd
import basic_music_stats


"""
mostly combinations of other functions in basic_music_stats as well as other less trivial functions
"""


cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content']

df = pd.read_csv(r"cleaned_apple_data.csv")


def occurs(a: list, item, threshold: int):
    """helper function for songs_played_once()"""
    return a.count(item) <= threshold


def songs_played_once(df) -> list:
    """Returns all songs that were only ever played once and calcs a metric of proportion of total songs that are bad songs"""
    songs_played_once_data = {}
    songs_played_once = []
    songs = df['content'].to_list()
    songs_set = set(songs)
    for song in songs_set:
        if occurs(songs, song, 1):
            songs_played_once.append(song)
    songs_played_once_data['songs_played_once'] = songs_played_once
    songs_played_once_data['ratio'] = len(songs_played_once)/len(df)
    return songs_played_once_data


