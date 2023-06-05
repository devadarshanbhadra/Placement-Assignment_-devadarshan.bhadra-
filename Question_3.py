import requests
import pandas as pd
import json

def download_and_convert_data(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Extract relevant attributes from the data
    attributes = ['id', 'num', 'name', 'img', 'type', 'height', 'weight', 'candy', 'candy_count',
                  'egg', 'spawn_chance', 'avg_spawns', 'spawn_time', 'multipliers', 'weaknesses',
                  'next_evolution', 'prev_evolution']

    pokemon_data = []
    for pokemon in data['pokemon']:
        pokemon_info = {attr: pokemon.get(attr) for attr in attributes}
        pokemon_data.append(pokemon_info)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(pokemon_data)

    # Save the DataFrame to Excel format
    df.to_excel(output_file, index=False)

    print("Data conversion completed. Output file:", output_file)

# Provide the URL of the data file to download
url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

# Provide the desired output file path (including the .xlsx extension)
output_file = 'pokedex.xlsx'

# Call the function to download and convert the data
download_and_convert_data(url, output_file)
    



