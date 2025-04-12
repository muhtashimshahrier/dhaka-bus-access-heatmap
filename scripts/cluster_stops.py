import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import haversine_distances
import argparse

parser = argparse.ArgumentParser(description="Cluster bus stops using DBSCAN with Haversine distance.")
parser.add_argument('--input', type=str, required=True, help="Path to the full stop list with lat/lon")
parser.add_argument('--output', type=str, required=True, help="Path to save clustered output CSV")
parser.add_argument('--eps', type=float, default=500, help="Clustering radius in meters (default: 500)")
args = parser.parse_args()

# Load and clean input
df = pd.read_excel(args.input) if args.input.endswith(".xlsx") else pd.read_csv(args.input)
df = df.dropna(subset=['latitude', 'longitude'])

# Prepare coordinates
coords = df[['latitude', 'longitude']].to_numpy()
coords_rad = np.radians(coords)

# Haversine distance matrix
distance_matrix = haversine_distances(coords_rad) * 6371000  # Earth radius in meters

# DBSCAN clustering
db = DBSCAN(eps=args.eps, min_samples=1, metric='precomputed')
labels = db.fit_predict(distance_matrix)
df['cluster_id'] = labels

# Deduplicate by (cluster_id, Bus Name)
deduped = df[['cluster_id', 'Bus Name', 'latitude', 'longitude']].drop_duplicates()

# Aggregate service intensity
clustered = deduped.groupby('cluster_id').agg({
    'latitude': 'mean',
    'longitude': 'mean',
    'Bus Name': 'count'
}).reset_index().rename(columns={'Bus Name': 'service_count'})

# Save output
clustered.to_csv(args.output, index=False)
print(f"Clustering complete. Saved to: {args.output}")
