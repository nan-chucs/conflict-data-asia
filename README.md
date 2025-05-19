# Conflict Data Analysis – UCDP GED (Asia)

This project focuses on building a simple, functional data pipeline using conflict data from the UCDP GED API. The scope was to track conflicts in Asia, store them in a structured database, and visualize key metrics in Power BI.

It’s not perfect — some files are missing or weren’t saved, and the final dataset was too large to upload here. But it works, and it taught me a lot.

---

## Tools Used

- Python (requests, pandas)
- PostgreSQL (pgAdmin 4)
- Power BI (for visuals)
- Git + GitHub (first time putting a full project here)

---

## What This Project Does

- Connects to the UCDP GED public API and pulls conflict event data
- Filters for countries in Asia using a manually prepared country code list
- Cleans and transforms the data with Python (handled missing values, cleaned text)
- Builds normalized SQL tables for:
  - Countries
  - Wars
  - Events
  - Geolocation
- Extracts latitude and longitude from POINT types for compatibility with Power BI
- Summarizes fatalities and event counts for analysis
- Visualizes the results in Power BI

---

## Project Folder Overview

Some parts of the original project weren’t saved, but here’s what remains:

- `data/`: Cleaned datasets (some large CSVs not included)
- `sql/`: SQL scripts to create and populate tables
- `visuals/`: One screenshot from the Power BI report
- `README.md`: This file

> Note: `conflict_data_asia.csv` was too large for GitHub, so it’s not included here.

---

## Screenshot

![Power BI Report](visuals/report_screenshot.png)

This is just a static summary — most of the interactivity is in Power BI.

---

## Final Notes

- `event_id` was used as the primary key throughout the project
- Foreign keys were initially set but later dropped in some places for flexibility
- The pipeline isn’t fully automated yet — the API connection and database parts are manual
- UCDP data includes all types of fatalities (civilian + combatant), but it doesn’t distinguish between them

---

## What's Missing

- A few original scripts
- The large source CSV used to populate the tables
- A proper way to reproduce this from scratch

I’ll eventually come back to restructure and clean up the repo. For now, this stands as a working draft of my first proper data pipeline.

---

## Contact

If you want the report file or want to ask something about this project, feel free to reach out.
