import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('meteorite_data.csv')

# Convert the 'Year' column to datetime type
df['Year'] = pd.to_datetime(df['Year'])

# Get all the Earth meteorites that fell before the year 2000
earth_meteorites_before_2000 = df[df['Year'].dt.year < 2000]

# Get all the Earth meteorites' coordinates that fell before the year 1970
earth_meteorites_coordinates_before_1970 = df[df['Year'].dt.year < 1970][['Latitude', 'Longitude']]

# Get all Earth meteorites with mass greater than 10000 kg (assuming mass is in kg)
earth_meteorites_mass_gt_10000 = df[df['Mass (g)'] > 10000]

# Plotting the analysis

# Plot 1: Histogram of meteorites by year
plt.figure(figsize=(10, 6))
plt.hist(df['Year'], bins=30, edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Distribution of Meteorites by Year')
plt.show()

# Plot 2: Scatter plot of meteorite coordinates
plt.figure(figsize=(10, 6))
plt.scatter(df['Longitude'], df['Latitude'], s=10, alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Meteorite Coordinates')
plt.show()

# Plot 3: Bar plot of meteorites by mass range
mass_ranges = ['< 1000 kg', '1000-5000 kg', '5000-10000 kg', '> 10000 kg']
mass_counts = [
    len(df[df['Mass (g)'] < 1000]),
    len(df[(df['Mass (g)'] >= 1000) & (df['Mass (g)'] < 5000)]),
    len(df[(df['Mass (g)'] >= 5000) & (df['Mass (g)'] < 10000)]),
    len(df[df['Mass (g)'] >= 10000])
]

plt.figure(figsize=(10, 6))
plt.bar(mass_ranges, mass_counts)
plt.xlabel('Mass Range')
plt.ylabel('Count')
plt.title('Distribution of Meteorites by Mass Range')
plt.show()

# Print the analysis results
print("Number of Earth meteorites that fell before the year 2000:", len(earth_meteorites_before_2000))
print("Number of Earth meteorites' coordinates that fell before the year 1970:", len(earth_meteorites_coordinates_before_1970))
print("Number of Earth meteorites with mass greater than 10000 kg:", len(earth_meteorites_mass_gt_10000))