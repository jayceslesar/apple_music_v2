import pandas as pd
import basic_music_stats

df = pd.read_csv(r"cleaned_apple_data.csv")


years = set(df['year'].to_list())
months = set(df['month'].to_list())

