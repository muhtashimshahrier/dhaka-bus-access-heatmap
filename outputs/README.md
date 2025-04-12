# QGIS Visualization & Spatial Analysis

This folder contains the core visual output and spatial analysis created using QGIS for the **Bus Route Access Heatmap in Dhaka** project.

---

## Main Visualization

**`heatmap_dhaka_bus_access.png`**  
A heatmap visualizing the intensity of bus service access across Dhaka. The brighter areas indicate clusters served by more unique buses. 

Created using clustered bus stop centroids, weighted by `service_count`.

---

## QGIS Workflow Summary

### 1. Imported clustered bus stop centroids
- Used `clustered_stops.csv` as input
- Imported as a delimited text layer (EPSG:4326 - WGS 84)
- Columns included:
  - `latitude`
  - `longitude`
  - `service_count` (number of unique buses in cluster)

---

### 2. Exported and reprojected
- Exported points to shapefile for styling
- Reprojected to **EPSG:32646 (UTM Zone 46N)** for metric accuracy (required for heatmap radius)

---

### 3. Created a heatmap layer
- Applied heatmap symbology to `service_count`
- Parameters:
  - Radius: **500 meters**
  - Weight: `service_count`
  - Color ramp: Yellow → Orange → Red
  - Blending mode: Overlay
  - Opacity: 70%

---

### 4. Added basemap
- Used **QuickMapServices** plugin
- Added **OpenStreetMap Standard** for context

---

### 5. Population raster (WorldPop)
- Downloaded `bgd_pd_2020_1km_UNadj.tif`
- Added raster to QGIS
- Created **3 km buffer** around clusters as a mask
- Used **Clip Raster by Mask Layer** to extract Dhaka

---

### 6. 1 km × 1 km grid creation
- Used **Create Grid** tool:
  - Extent: Clipped raster area
  - CRS: EPSG:32646
  - Cell size: 1000m × 1000m
- Clipped grid using buffered polygon

---

### 7. Zonal statistics on population
- Used **Zonal Statistics** tool:
  - Statistic: **Sum** of population (`pop_sum`) in each cell

---

### 8. Styled the grid
- Applied graduated symbology to `pop_sum`
- Used **Natural Breaks (Jenks)** for color classification

---

### 9. Transit access by grid
- Used **Join Attributes by Location (Summary)**:
  - Counted number of clusters per grid cell
  - Output field: `cluster_id_count`

---

### 🔹 10. Identified underserved zones
- Filtered grid cells using expressions like:
  ```sql
  "pop_sum" > 100000 AND "cluster_id_count" = 0


## Notes
- QGIS Version: 3.40.5
- Basemap: OpenStreetMap Standard
- Heatmap generated using cluster data from data/clustered_stops.csv
