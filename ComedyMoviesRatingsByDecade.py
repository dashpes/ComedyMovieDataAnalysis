import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
comedy_movies = pd.read_csv("data/comedy_movies.csv")

# Ensure startYear is numeric, and handle errors by setting invalid values to NaN
comedy_movies["startYear"] = pd.to_numeric(comedy_movies["startYear"], errors="coerce")

# Drop rows with NaN values in startYear
comedy_movies = comedy_movies.dropna(subset=["startYear"])

# Convert startYear to integer (after dropping NaN rows)
comedy_movies["startYear"] = comedy_movies["startYear"].astype(int)

# Create a new column for the decade
comedy_movies["Decade"] = (comedy_movies["startYear"] // 10) * 10

# Calculate the average rating per decade
average_ratings_per_decade = comedy_movies.groupby('Decade')['averageRating'].mean().reset_index()

# Line plot of average ratings per decade
plt.figure(figsize=(10, 6))
plt.plot(average_ratings_per_decade['Decade'], average_ratings_per_decade['averageRating'], marker='o', linestyle='-')
plt.xlabel('Decade')
plt.ylabel('Average Rating')
plt.title('Average Rating of Comedy Movies per Decade - Line Chart')
plt.ylim(1, 10)
plt.grid(True)
plt.show()

# Bar chart of average ratings per decade (in a separate window)
plt.figure(figsize=(10, 6))
plt.bar(average_ratings_per_decade['Decade'], average_ratings_per_decade['averageRating'], color='skyblue')
plt.xlabel('Decade')
plt.ylabel('Average Rating')
plt.title('Average Rating of Comedy Movies per Decade - Bar Chart')
plt.ylim(1, 10)
plt.grid(axis='y')
plt.show()