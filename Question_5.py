import requests
import json
from bs4 import BeautifulSoup

def download_and_extract_data(url):
    # Download the data from the API link
    response = requests.get(url)
    data = response.json()

    # Extract the required data attributes
    show_id = data['id']
    show_url = data['url']
    show_name = data['name']
    episodes = data['_embedded']['episodes']
    
    episode_list = []
    for episode in episodes:
        episode_season = episode['season']
        episode_number = episode['number']
        episode_type = episode['type']
        episode_airdate = episode['airdate']
        episode_airtime = episode['airtime']
        episode_runtime = episode['runtime']
        episode_rating = episode['rating']['average']
        episode_summary = BeautifulSoup(episode['summary'], 'html.parser').get_text()
        episode_image_medium = episode['image']['medium']
        episode_image_original = episode['image']['original']
        
        episode_info = {
            'ID': show_id,
            'URL': show_url,
            'Name': show_name,
            'Season': episode_season,
            'Number': episode_number,
            'Type': episode_type,
            'Airdate': episode_airdate,
            'Airtime': episode_airtime,
            'Runtime': episode_runtime,
            'Rating': episode_rating,
            'Summary': episode_summary,
            'Medium Image': episode_image_medium,
            'Original Image': episode_image_original
        }
        episode_list.append(episode_info)

    # Print the extracted data attributes with proper formatting
    print("Show ID:", show_id)
    print("Show URL:", show_url)
    print("Show Name:", show_name)
    print("\nEpisodes:")
    for episode in episode_list:
        print("ID:", episode['ID'])
        print("URL:", episode['URL'])
        print("Name:", episode['Name'])
        print("Season:", episode['Season'])
        print("Number:", episode['Number'])
        print("Type:", episode['Type'])
        print("Airdate:", episode['Airdate'])
        print("Airtime:", episode['Airtime'])
        print("Runtime:", episode['Runtime'])
        print("Rating:", episode['Rating'])
        print("Summary:", episode['Summary'])
        print("Medium Image:", episode['Medium Image'])
        print("Original Image:", episode['Original Image'])
        print()

# Provide the API link to download the data
url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'

# Call the function to download and extract the data attributes
download_and_extract_data(url)




