import pandas as pd
import initial_clean
import basic_music_stats
import medium_music_stats
import advanced_music_stats

df = pd.read_csv(r"cleaned_apple_data.csv")


years = set(df['year'].to_list())
months = set(df['month'].to_list())


