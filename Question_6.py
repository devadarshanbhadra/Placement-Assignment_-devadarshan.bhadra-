import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
data = pd.read_excel('pokedex.xlsx')

# Question 1: Get all Pokemons whose spawn rate is less than 5%
spawn_rate_threshold = 5
low_spawn_rate_pokemon = data[data['spawn_chance'] < spawn_rate_threshold]
print("Pokemons with spawn rate less than", spawn_rate_threshold, "percent:")
print(low_spawn_rate_pokemon[['num', 'name', 'spawn_chance']])
print()

# Question 2: Get all Pokemons that have less than 4 weaknesses
weakness_threshold = 4
pokemon_with_few_weaknesses = data[data['weaknesses'].str.count(',') < weakness_threshold]
print("Pokemons with less than", weakness_threshold, "weaknesses:")
print(pokemon_with_few_weaknesses[['num', 'name', 'weaknesses']])
print()

# Question 3: Get all Pokemons that have no multipliers at all
no_multipliers_pokemon = data[data['multipliers'] == '']
print("Pokemons with no multipliers:")
print(no_multipliers_pokemon[['num', 'name']])
print()

# Question 4: Get all Pokemons that do not have more than 2 evolutions
evolution_threshold = 2
pokemon_with_few_evolutions = data[data['next_evolution'].str.count(',') <= evolution_threshold]
print("Pokemons with", evolution_threshold, "or fewer evolutions:")
print(pokemon_with_few_evolutions[['num', 'name', 'next_evolution']])
print()

# Question 5: Get all Pokemons whose spawn time is less than 300 seconds
spawn_time_threshold = 300
# Convert spawn time to seconds for comparison
data['spawn_time'] = pd.to_datetime(data['spawn_time'], format='%M:%S').dt.second
short_spawn_time_pokemon = data[data['spawn_time'] < spawn_time_threshold]
print("Pokemons with spawn time less than", spawn_time_threshold, "seconds:")
print(short_spawn_time_pokemon[['num', 'name', 'spawn_time']])
print()

# Question 6: Get all Pokemon who have more than two types of capabilities
multiple_types_pokemon = data[data['type'].str.count(',') > 1]
print("Pokemons with more than two types of capabilities:")
print(multiple_types_pokemon[['num', 'name', 'type']])
print()

# Plotting for better visualizations

# Plot for Question 1: Spawn Rate Distribution
plt.figure(figsize=(10, 6))
plt.hist(data['spawn_chance'], bins=20, edgecolor='black')
plt.xlabel('Spawn Rate (%)')
plt.ylabel('Count')
plt.title('Spawn Rate Distribution')
plt.show()

# Plot for Question 2: Weakness Count Distribution
plt.figure(figsize=(10, 6))
data['Weakness Count'] = data['weaknesses'].str.count(',') + 1
plt.hist(data['Weakness Count'], bins=range(1, 8), edgecolor='black', align='left')
plt.xlabel('Number of Weaknesses')
plt.ylabel('Count')
plt.title('Weakness Count Distribution')
plt.xticks(range(1, 8))
plt.show()