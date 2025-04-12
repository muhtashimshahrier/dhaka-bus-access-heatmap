# Data Folder

This folder contains the cleaned and processed datasets used in the **Bus Route Access Heatmap in Dhaka** project. Each file is in CSV format and supports different stages of the analysis.

---

## File Descriptions

### `geocoded_unique_stops.csv`
A deduplicated list of bus stops scraped from multiple routes, with latitude and longitude obtained via OpenCage geocoding and fuzzy matching. This dataset represents unique stop locations across the city.

**Columns:**
- `Stop Name`: Cleaned stop name
- `latitude`: Geocoded latitude
- `longitude`: Geocoded longitude

---

### `stop_routes_full.csv`
The full list of bus stops along with their respective operators and coordinates. This dataset captures how frequently each stop appears across different routes.

**Columns:**
- `Operator`: Bus operator name (e.g., Active Paribahan)
- `Stop No`: Stop index in route
- `Stop Name`: Raw stop name
- `latitude`: Geocoded latitude
- `longitude`: Geocoded longitude

---

### `clustered_stops.csv`
Output from DBSCAN clustering applied to `geocoded_unique_stops.csv`. Each row corresponds to a cluster centroid and its associated service intensity (number of stops within a 500m radius).

**Columns:**
- `cluster_id`: Cluster identifier
- `latitude`: Cluster centroid latitude
- `longitude`: Cluster centroid longitude
- `service_count`: Number of stops within the cluster (i.e., service intensity)

---



