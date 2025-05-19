import pandas as pd
import re

csv_path = r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_asia.csv"
df = pd.read_csv(csv_path)

wars_table = df[["conflict_new_id", "country", "date_start", "date_end", "type_of_violence", "source_office"]].drop_duplicates()

def clean_text(text):
    try:
        return re.sub(r'[^\x00-\x7F]+', '', str(text))
    except:
        return ''

wars_table['source_office'] = wars_table['source_office'].apply(clean_text)
wars_table = wars_table.rename(columns={"conflict_new_id": "war_id"})

wars_table.to_csv(r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_wars.csv", index=False, encoding="utf-8")
