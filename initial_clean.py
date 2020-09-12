import pandas as pd


df = pd.read_csv(r"C:\Users\teamj\Documents\GitHub\apple_music_v2\Apple Music Play Activity.csv")

cols_i_care_about = ['Artist Name', 'Content Name', 'Event Start Timestamp', 'Event End Timestamp', 'year', 'month']
"""
artist = Artist Name
song = Content Name
start time = Event Start Timestamp
end time = Event End Timestamp
"""
# create year and month variables for easy access later
year = []
month = []
for index, row in df.iterrows():
    timestamp = str(row['Event Start Timestamp']).split('-')
    if 'nan' in timestamp:
        year.append('')
        month.append('')
        continue
    year.append(timestamp[0])
    month.append(timestamp[1])
df['year'] = year
df['month'] = month

# get rid of columns we dont want to look at
for col in df.columns:
    if col not in cols_i_care_about:
        del df[col]
df.to_csv('cleaned_apple_data.csv')

# drop na's
df = pd.read_csv(r"cleaned_apple_data.csv")
df = df.dropna()

# create a content row to get rid of duplicate song names with different artists (possible)
combined_content = []
for index, row in df.iterrows():
    curr_content = row['Content Name'] + ', ' + row['Artist Name']
    combined_content.append(curr_content)
df['content'] = combined_content
df = df.sort_values(by='Event Start Timestamp')
df = df.applymap(lambda s:s.lower() if type(s) == str else s)
df.to_csv(r"cleaned_apple_data.csv")
