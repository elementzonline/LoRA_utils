import folium
import pandas as pd
import geopy.distance
import matplotlib.pyplot as plt

# Load your CSV data using the correct file path
csv_file_path = "/home/dhanish/Documents/brinto/gps/location.csv"
data = pd.read_csv(csv_file_path)

# Central antenna coordinates (you should replace these with your actual coordinates)
central_antenna_coords = (8.512643333, 76.947217833)

# Calculate distances and store them in a new column 'Distance' in the DataFrame
data['Distance'] = data.apply(lambda row: geopy.distance.distance(central_antenna_coords, (row[' Latitude'], row[' Longitude'])).m, axis=1)

# Create a scatter plot of RSSI against Distance
plt.figure(figsize=(10, 6))
plt.scatter(data['Distance'], data[' SNR'], alpha=0.5)
plt.xlabel('Distance (m)')
plt.ylabel('SNR')
plt.title('SNR vs. Distance')
plt.grid(True)

# Save the plot to a file (if needed)
plt.savefig('snr_vs_distance.png')

# Display the plot
plt.show()
