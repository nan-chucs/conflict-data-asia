import pandas as pd
import re

# Load your CSV file
csv_path = r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_asia.csv"
df = pd.read_csv(csv_path)

# Select and deduplicate relevant columns
events_table = df[["id", "conflict_new_id", "date_start", "country", "type_of_violence", "best", "source_article"]].drop_duplicates()

# Clean source_article: remove non-UTF-8-compatible characters, but KEEP commas
def clean_text(text):
    try:
        return re.sub(r'[^\x00-\x7F]+', '', str(text))  # Just strip bad characters
    except:
        return ''

events_table['source_article'] = events_table['source_article'].apply(clean_text)

# Save cleaned events table to UTF-8 CSV
events_table.to_csv(r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_events.csv", index=False, encoding="utf-8")
