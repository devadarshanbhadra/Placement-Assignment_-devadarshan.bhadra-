import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data_url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(data_url)

# Check if 'Clean Alternative Fuel Vehicle (CAFV)' column exists
if 'Clean Alternative Fuel Vehicle (CAFV)' in df.columns:
    # Get all the cars and their types that do not qualify for clean alternative fuel vehicle
    non_clean_cars = df[df['Clean Alternative Fuel Vehicle (CAFV)'] == 'No']
    non_clean_cars = non_clean_cars[['Make', 'Model']]
    print("Cars that do not qualify for clean alternative fuel vehicle:")
    print(non_clean_cars)
else:
    print("Column 'Clean Alternative Fuel Vehicle (CAFV)' not found.")

# Check if 'Make' and 'City' columns exist
if 'Make' in df.columns and 'City' in df.columns:
    # Get all TESLA cars with the model year and city
    tesla_cars = df[(df['Make'] == 'TESLA') & (df['City'] == 'BOTHELL')]
    if not tesla_cars.empty:
        tesla_cars = tesla_cars[['Model Year', 'Make', 'City']]
        print("TESLA cars made in Bothell City:")
        print(tesla_cars)
    else:
        print("No TESLA cars found in Bothell City.")
else:
    print("Columns 'Make' and/or 'City' not found.")

# Check if 'Electric Range' and 'Model Year' columns exist
if 'Electric Range' in df.columns and 'Model Year' in df.columns:
    # Get all the cars that have an electric range of more than 100, and were made after 2015
    electric_cars = df[(df['Electric Range'] > 100) & (df['Model Year'] > 2015)]
    if not electric_cars.empty:
        electric_cars = electric_cars[['Make', 'Model', 'Electric Range']]
        print("Cars with an electric range of more than 100, made after 2015:")
        print(electric_cars)
    else:
        print("No cars found with an electric range of more than 100, made after 2015.")
else:
    print("Columns 'Electric Range' and/or 'Model Year' not found.")

# Draw plots to show the distribution between city and electric vehicle type
if 'City' in df.columns and 'Electric Vehicle Type' in df.columns:
    city_counts = df['City'].value_counts()
    city_counts.plot(kind='bar')
    plt.xlabel("City")
    plt.ylabel("Count")
    plt.title("Distribution of Electric Vehicles by City")
    plt.show()

    electric_type_counts = df['Electric Vehicle Type'].value_counts()
    electric_type_counts.plot(kind='bar')
    plt.xlabel("Electric Vehicle Type")
    plt.ylabel("Count")
    plt.title("Distribution of Electric Vehicles by Type")
    plt.show()
else:
    print("Columns 'City' and/or 'Electric Vehicle Type' not found.")