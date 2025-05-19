import requests
import json
import pandas as pd

api_url = "https://ucdpapi.pcr.uu.se/api/gedevents/24.1"
target_folder = "F:/Full Stack/Projects/Conflict Asia/Data/"
page_size = 1000
xlsx_path = r"F:\Full Stack\Projects\Conflict Asia\Data\G&W Codes - Asia.xlsx"  # Replace with your actual file path
df = pd.read_excel(xlsx_path, usecols=["Country", "Code"])
dict_from_df = df.set_index('Country')['Code'].to_dict()

def total_pages(page_size, country):
    params = {
            "country": country,
            "pagesize": page_size
        }
    
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error fetching data for region : {response.status_code}")
    Total_pages = data.get("TotalPages", 1)
    print(f"Total pages: {Total_pages}")
    return Total_pages

def fetch_all_data(country_dict, page_size):
    all_data = []

    for country_name, country_code in country_dict.items():
        print(f"\nFetching data for {country_name} (Code: {country_code})...")
        try:
            total = total_pages(page_size, country_code)
            for i in range(1, total + 1):
                params = {
                    "page": i,
                    "country": country_code,  # Using numeric code here
                    "pagesize": page_size
                }
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    results = data.get("Result", [])
                    if not results:
                        print(f"No more results on page {i} for {country_name}.")
                        break
                    all_data.extend(results)
                    print(f"Page {i}/{total} for {country_name} fetched. Records: {len(results)}")
                else:
                    print(f"Error {response.status_code} on page {i} for {country_name}")
                    break
        except Exception as e:
            print(f"Error processing {country_name}: {e}")

    return all_data

# Fetch all countries' data
all_conflict_data = fetch_all_data(dict_from_df, page_size)

countries_table = all_conflict_data["country_id", "country", "region"]
countries_table.head()

# Save to DataFrame
#df_all = pd.DataFrame(all_conflict_data)
#df_all.to_csv(target_folder + "conflict_data_asia.csv", index=False)