import pandas as pd
import os
import argparse

def get_bus_routes_from_html(url: str) -> list:
    """
    Extracts bus route data from a given URL using pandas.read_html().
    Returns a list of dictionaries in long format (one stop per row).
    """
    long_format_data = []
    tables = pd.read_html(url)

    for table in tables:
        for _, row in table.iterrows():
            bus_raw = str(row[0]).strip()
            route_raw = str(row[1]).strip()

            if pd.isna(bus_raw) or pd.isna(route_raw):
                continue

            if '(' in bus_raw:
                bus_name = bus_raw.split('(')[0].replace('Bus Route', '').strip()
            else:
                bus_name = bus_raw.replace('Bus Route', '').strip()

            route_cleaned = route_raw.replace("–", "⇄").replace("\xa0", " ")
            stops = [stop.strip() for stop in route_cleaned.split("⇄") if stop.strip()]

            for idx, stop in enumerate(stops, start=1):
                long_format_data.append({
                    "Bus Name": bus_name,
                    "Stop Order": idx,
                    "Stop Name": stop
                })

    return long_format_data

def save_csv(data: list, filename: str):
    df = pd.DataFrame(data)
    path = os.path.join(os.getcwd(), filename)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Dhaka bus routes and save as CSV.")
    parser.add_argument('--url', type=str, default="https://busroutebd.com/dhaka-local-bus-routes/", help="URL to scrape from")
    parser.add_argument('--output', type=str, default="data/dhaka_bus_routes.csv", help="Output CSV filename")
    args = parser.parse_args()

    data = get_bus_routes_from_html(args.url)
    save_csv(data, args.output)
    print(f"Bus route data saved to: {args.output}")
