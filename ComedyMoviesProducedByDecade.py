import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
comedy_movies = pd.read_csv("Data/comedy_movies.csv")

# Ensure startYear is numeric, and handle errors by setting invalid values to NaN
comedy_movies["startYear"] = pd.to_numeric(comedy_movies["startYear"], errors="coerce")

# Drop rows with NaN values in startYear
comedy_movies = comedy_movies.dropna(subset=["startYear"])

# Convert startYear to integer (after dropping NaN rows)
comedy_movies["startYear"] = comedy_movies["startYear"].astype(int)

# Create a new column for the decade
comedy_movies["decade"] = (comedy_movies["startYear"] // 10) * 10

# Group by decade to get the count of movies for each decade
movies_per_decade = comedy_movies.groupby("decade").size().reset_index(name="count")

# Plotting the number of movies produced each decade
plt.figure(figsize=(10, 6))
sns.barplot(data=movies_per_decade, x="decade", y="count", color="lightcoral")
plt.title("Number of Comedy Movies Produced Per Decade")
plt.xlabel("Decade")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)

plt.show()