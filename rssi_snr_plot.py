"""
Plot the following
- distance vs SNR 
- distance vs RSSI
"""


import pandas as pd
import geopy.distance
import matplotlib.pyplot as plt

FOLDER_PATH = 'Using_E22900M30S_with_Wisgate2'

# Load your CSV data using the correct file path
csv_file_path = f"{FOLDER_PATH}/location.csv"
df = pd.read_csv(csv_file_path)

# Central antenna coordinates (you should replace these with your actual coordinates)
# central_antenna_coords = (8.512643333, 76.947217833)
central_antenna_coords = (8.5126123,76.946934)

# Calculate distance for each coordinate
df['Distance'] = df.apply(lambda row: geopy.distance.distance(central_antenna_coords, (row['Latitude'], row['Longitude'])).m, axis=1)

# Plotting
plt.figure(figsize=(10,6))
# Plot RSSI
plt.plot(df['Distance'], df['RSSI'], '-o', label='RSSI', color='blue')

# Plot SNR
plt.plot(df['Distance'], df['SNR'], '-o', label='SNR', color='red')

plt.title('Distance vs RSSI and SNR')
plt.xlabel('Distance (m)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Save the plot to a file (if needed)
plt.savefig(f'{FOLDER_PATH}/rssi_vs_distance.png')

# Display the plot
plt.show()
