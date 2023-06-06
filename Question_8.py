import matplotlib.pyplot as plt

# Replace ... with the extracted episode data
episodes = [
    {
        "name": "Episode 1",
        "season": 1,
        "average_rating": 8.2,
        "airdate": "2019-01-15",
        "summary": "Summary of Episode 1"
    },
    {
        "name": "Episode 2",
        "season": 1,
        "average_rating": 9.1,
        "airdate": "2019-01-22",
        "summary": "Summary of Episode 2"
    },
    {
        "name": "Episode 1",
        "season": 2,
        "average_rating": 8.5,
        "airdate": "2020-02-10",
        "summary": "Summary of Episode 1"
    },
    {
        "name": "Episode 2",
        "season": 2,
        "average_rating": 8.8,
        "airdate": "2020-02-17",
        "summary": "Summary of Episode 2"
    },
    # Add more episodes for each season
    # ...
]

# Get all the overall ratings for each season and compare the ratings using plots
season_numbers = []
season_ratings = []
for episode in episodes:
    season_numbers.append(episode["season"])
    season_ratings.append(episode["average_rating"])

plt.bar(season_numbers, season_ratings)
plt.xlabel("Season")
plt.ylabel("Average Rating")
plt.title("Overall Ratings for Each Season")
plt.show()

# Get all the episode names whose average rating is more than 8 for every season
high_rated_episodes = []
for episode in episodes:
    if episode["average_rating"] > 8:
        high_rated_episodes.append(episode["name"])

print("Highly Rated Episodes:")
for episode_name in high_rated_episodes:
    print(episode_name)

# Get all the episode names that aired before May 2019
early_episodes = []
for episode in episodes:
    if episode["airdate"] < "2019-05-01":
        early_episodes.append(episode["name"])

print("Episodes Aired Before May 2019:")
for episode_name in early_episodes:
    print(episode_name)

# Get the episode name from each season with the highest and lowest rating
highest_rated_episodes = []
lowest_rated_episodes = []
for season in set(season_numbers):
    season_episodes = [episode for episode in episodes if episode["season"] == season]
    highest_rated = max(season_episodes, key=lambda episode: episode["average_rating"])
    lowest_rated = min(season_episodes, key=lambda episode: episode["average_rating"])
    highest_rated_episodes.append(highest_rated["name"])
    lowest_rated_episodes.append(lowest_rated["name"])

print("Episodes with Highest Ratings:")
for episode_name in highest_rated_episodes:
    print(episode_name)

print("Episodes with Lowest Ratings:")
for episode_name in lowest_rated_episodes:
    print(episode_name)

# Get the summary for the most popular (highest rated) episode in every season
popular_summaries = []
for season in set(season_numbers):
    season_episodes = [episode for episode in episodes if episode["season"] == season]
    highest_rated = max(season_episodes, key=lambda episode: episode["average_rating"])
    popular_summaries.append(highest_rated["summary"])

print("Summaries of Most Popular Episodes:")
for summary in popular_summaries:
    print(summary)