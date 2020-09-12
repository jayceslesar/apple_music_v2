import pandas as pd


cols_to_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month', 'content']

df = pd.read_csv(r"cleaned_apple_data.csv")


# finds all songs considered "earworms" - songs that pick up very quick and stay up top
def earworms(df) -> list:
    earworms = []
    return earworms
