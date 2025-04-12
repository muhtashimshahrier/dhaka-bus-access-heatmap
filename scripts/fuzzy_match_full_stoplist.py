import pandas as pd
import numpy as np
from fuzzywuzzy import process
import argparse

parser = argparse.ArgumentParser(description="Fuzzy match geocoded coordinates to full bus stop list.")
parser.add_argument("--geocoded", required=True, help="Path to geocoded unique stops CSV.")
parser.add_argument("--full", required=True, help="Path to full stop list (Excel or CSV).")
parser.add_argument("--output", required=True, help="Path to save the enriched stop list with lat/lon.")
parser.add_argument("--threshold", type=int, default=90, help="Fuzzy match score threshold (default: 90)")
args = parser.parse_args()

# Load files
geo_df = pd.read_csv(args.geocoded)
main_df = pd.read_excel(args.full) if args.full.endswith('.xlsx') else pd.read_csv(args.full)

# Clean stop names
geo_df['Stop Name'] = geo_df['Stop Name'].astype(str).str.strip()
main_df['Stop Name'] = main_df['Stop Name'].astype(str).str.strip()

# Add lat/lon columns if missing
main_df['latitude'] = np.nan
main_df['longitude'] = np.nan

# Fuzzy match
geo_names = geo_df['Stop Name'].tolist()

for i, row in main_df.iterrows():
    stop = row['Stop Name']
    best_match, score = process.extractOne(stop, geo_names)
    
    if score >= args.threshold:
        matched_row = geo_df[geo_df['Stop Name'] == best_match].iloc[0]
        main_df.at[i, 'latitude'] = matched_row['latitude']
        main_df.at[i, 'longitude'] = matched_row['longitude']

print("Fuzzy matching complete.")
main_df.to_csv(args.output, index=False)
print(f"Output saved to {args.output}")
