import pandas as pd
import re

# Load your CSV file
csv_path = r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_asia.csv"
df = pd.read_csv(csv_path)

# Select and deduplicate relevant columns
war_participants_table = df[["id", "country_id", "dyad_name"]].drop_duplicates()

# Save cleaned wars table to UTF-8 CSV
war_participants_table.to_csv(r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_war_participants.csv", index=False, encoding="utf-8")
