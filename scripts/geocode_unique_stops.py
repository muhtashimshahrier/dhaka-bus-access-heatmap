import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import argparse

parser = argparse.ArgumentParser(description="Geocode unique bus stop names using Nominatim.")
parser.add_argument("--input", required=True, help="Path to Excel or CSV file containing full stop list.")
parser.add_argument("--output", required=True, help="Path to save the geocoded unique stops as CSV.")
args = parser.parse_args()

# Load and extract unique stop names
df = pd.read_excel(args.input) if args.input.endswith('.xlsx') else pd.read_csv(args.input)
unique_stops = df['Stop Name'].dropna().astype(str).str.strip().unique()
stops_df = pd.DataFrame(unique_stops, columns=["Stop Name"])

# Initialize geocoder
geolocator = Nominatim(user_agent="dhaka_bus_heatmap")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Apply geocoding
stops_df['location'] = stops_df['Stop Name'].apply(lambda x: geocode(f"{x}, Dhaka, Bangladesh"))
stops_df['latitude'] = stops_df['location'].apply(lambda loc: loc.latitude if loc else None)
stops_df['longitude'] = stops_df['location'].apply(lambda loc: loc.longitude if loc else None)

# Save to CSV
stops_df.drop(columns=['location']).to_csv(args.output, index=False)
print(f"Geocoding complete. Output saved to {args.output}")
