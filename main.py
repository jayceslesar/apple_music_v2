import pandas as pd
import os
from pathlib import Path
import initial_clean
import basic_music_stats
import medium_music_stats
import advanced_music_stats


df = pd.read_csv(r"cleaned_apple_data.csv")


print(basic_music_stats.month_minutes(df, 2020, 3))

years = set(df['year'].to_list())
months = set(df['month'].to_list())


