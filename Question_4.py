import pandas as pd
import requests

# Define the URL to download the JSON data from
url = 'https://data.nasa.gov/resource/y77d-th95.json'

# Send a GET request to the URL and retrieve the JSON data
response = requests.get(url)
data = response.json()

# Create empty lists to store the extracted data
names = []
ids = []
name_types = []
recclasses = []
masses = []
years = []
reclats = []
reclongs = []
point_coordinates = []

# Iterate over each meteorite entry in the JSON data
for meteorite in data:
    # Extract the required attributes and append them to the respective lists
    names.append(meteorite['name'])
    ids.append(meteorite['id'])
    name_types.append(meteorite['nametype'])
    recclasses.append(meteorite['recclass'])
    masses.append(float(meteorite['mass']) if 'mass' in meteorite else None)
    year = meteorite.get('year')
    try:
        years.append(pd.to_datetime(year, format='%Y-%m-%dT%H:%M:%S.%f') if year and 'nanosecond' not in year else pd.NaT)
    except pd.errors.OutOfBoundsDatetime:
        years.append(pd.NaT)
    reclats.append(float(meteorite['reclat']) if 'reclat' in meteorite else None)
    reclongs.append(float(meteorite['reclong']) if 'reclong' in meteorite else None)
    point_coordinates.append(meteorite['geolocation']['coordinates'] if 'geolocation' in meteorite else [])

# Create a dictionary to hold the extracted data
meteorite_data = {
    'Name of Earth Meteorite': names,
    'ID of Earth Meteorite': ids,
    'Name Type': name_types,
    'Recclass': recclasses,
    'Mass (g)': masses,
    'Year': years,
    'Latitude': reclats,
    'Longitude': reclongs,
    'Point Coordinates': point_coordinates
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(meteorite_data)

# Export the DataFrame to a CSV file
output_file = 'meteorite_data.csv'
df.to_csv(output_file, index=False)

print("Data has been exported to", output_file)