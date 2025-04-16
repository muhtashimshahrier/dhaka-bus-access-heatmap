# Bus Route Access Heatmap in Dhaka

This project analyzes and visualizes the spatial intensity of bus service access in Dhaka using scraped route data, geocoded stop locations, spatial clustering, and GIS-based heatmap generation. The goal is to identify areas with dense transit coverage as well as potential service gaps, using both visual and population-based comparisons.

## Objective

To identify clusters of bus stops served by multiple unique routes and map the spatial distribution of transit accessibility across Dhaka. The project also integrates population data to highlight underserved but densely populated areas.

## Repository Structure
.
├── data/             # Cleaned and processed datasets
├── scripts/          # Python scripts for scraping, geocoding, matching, clustering
├── outputs/          # Final heatmap and QGIS analysis notes
├── requirements.txt  # Python dependencies
└── README.md         # Project overview and usage instructions


## Methodology

### 1. Data Collection and Preparation

- Scraped route data from https://dhakabusroute.com/.
- Extracted all stops for each bus route and saved in long format.
- Cleaned and deduplicated stop names.

### 2. Geocoding

- Geocoded unique stop names using the Nominatim API (OpenStreetMap).
- Applied fuzzy matching to assign coordinates to all stops in the full dataset.
- Final output: `stop_routes_full.csv` with lat/lon for each stop.

### 3. Clustering

- Applied DBSCAN clustering (500-meter radius) using Haversine distance.
- Aggregated cluster centroids and calculated `service_count` (number of unique buses serving each cluster).
- Output: `clustered_stops.csv` with latitude, longitude, and service intensity.

### 4. Visualization in QGIS

- Imported clustered stops and applied heatmap styling to visualize intensity.
- Reprojected to UTM Zone 46N for accurate distance scaling.
- Added OpenStreetMap basemap for spatial context.

### 5. Population-Based Access Comparison

- Loaded WorldPop 1 km raster for Bangladesh.
- Created a 1 km × 1 km grid clipped to Dhaka.
- Computed zonal statistics to estimate population per cell.
- Performed spatial join to count number of clusters per cell.
- Identified high-population zones with low or zero bus access.

## Scripts

All scripts are located in the `scripts/` folder and can be run independently.

## Outputs
Final visualizations and spatial analysis details are available in the outputs/ folder



