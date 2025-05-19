import pandas as pd
import re

# Load your CSV file
csv_path = r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_asia.csv"
df = pd.read_csv(csv_path)

# Extract relevant columns
geolocation_table = df[["id", "latitude", "longitude"]]

# Create 'location' column in POINT format "(x,y)" = (longitude, latitude)
geolocation_table["location"] = "(" + geolocation_table["longitude"].astype(str) + "," + geolocation_table["latitude"].astype(str) + ")"

# Keep only event_id and location
geolocation_table = geolocation_table.rename(columns={"id": "event_id"})[["event_id", "location"]]

# Export to CSV
geolocation_table.to_csv(r"F:\Full Stack\Projects\Conflict Asia\Data\conflict_data_geolocation.csv", index=False, encoding="utf-8")
