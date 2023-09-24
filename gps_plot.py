"""
Utility for creating gps graph based on the data

Todo: Add RSSI, SNR markers to the html instead of editing HTML directly
"""

import folium
import pandas as pd

FOLDER_PATH = "Using_E22900M30S_with_Wisgate2"
csv_file_path = f"{Using_E22900M30S_with_Wisgate2}/location.csv"

# Load your CSV data using the correct file path
data = pd.read_csv(csv_file_path)

# Create map object
m = folium.Map(location=[0, 0], zoom_start=5)

# Add markers for each data point
for index, row in data.iterrows():
    latitude = row[' Latitude']
    longitude = row[' Longitude']

    # Check if the latitude and longitude are not NaN (missing values)
    if not pd.isna(latitude) and not pd.isna(longitude):
        folium.Marker([latitude, longitude]).add_to(m)

# Save to HTML
m.save(f'{Using_E22900M30S_with_Wisgate2}/gps_plot.html')

