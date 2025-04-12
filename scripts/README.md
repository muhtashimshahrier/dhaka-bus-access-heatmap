# Script Descriptions

This folder contains Python scripts for scraping, processing, geocoding, and clustering bus stop data in Dhaka.

---

### `scrape_dhaka_routes.py`
Scrapes Dhaka bus route tables from [busroutebd.com](https://busroutebd.com) and returns stop-wise long-format data.

**Usage:**
```bash
python scripts/scrape_dhaka_routes.py --url <URL> --output data/dhaka_bus_routes.csv
```
### `geocode_unique_stops.py`
Extracts unique stop names and geocodes them using OpenStreetMap (Nominatim).

**Usage:**
```bash
python scripts/geocode_unique_stops.py --input data/stop_routes_full.csv --output data/geocoded_unique_stops.csv
```

### `fuzzy_match_full_stoplist.py`
Uses fuzzy matching to assign geocoded lat/lon to all stops from the full list.

**Usage:**
```bash
python scripts/fuzzy_match_full_stoplist.py \
  --geocoded data/geocoded_unique_stops.csv \
  --full data/stop_routes_full.xlsx \
  --output data/stop_routes_full.csv \
  --threshold 90
```

### `cluster_stops.py`
Clusters stop coordinates using DBSCAN with Haversine distance. Outputs average lat/lon and service count per cluster.

**Usage:**
```bash
python scripts/cluster_stops.py \
  --input data/stop_routes_full.csv \
  --output data/clustered_stops.csv \
  --eps 500
```

All scripts are modular and can be run independently. Coordinate matching and clustering rely on outputs from earlier steps.











