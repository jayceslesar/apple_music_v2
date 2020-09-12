import pandas as pd
import basic_music_stats


# mostly combinations of other functions in basic_music_stats


cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content']

df = pd.read_csv(r"cleaned_apple_data.csv")


# gets the top songs played and minutes for a given range of top
def top_artist_stats(df, count):
    artist_data = {}
    for artist in basic_music_stats.top_artists(df, count):
        artist = artist[0]
        artist_data[artist] = {}
        data = basic_music_stats.artist_stats(df, artist)
        artist_data[artist]['top_songs'] = data['top_songs']
        artist_data[artist]['artist_minutes'] = data['artist_minutes']
    return artist_data


# helper function for songs_played_once()
def occurs_once(a, item):
    return a.count(item) == 1


# finds all songs that were only ever played once and calcs a metric of proportion of total songs that are bad songs
def songs_played_once(df) -> list:
    songs_played_once_data = {}
    songs_played_once = []
    songs = df['content'].to_list()
    songs_set = set(songs)
    for song in songs_set:
        if occurs_once(songs, song):
            songs_played_once.append(song)
    songs_played_once_data['songs_played_once'] = songs_played_once
    songs_played_once_data['ratio'] = len(songs_played_once)/len(df)
    return songs_played_once_data
