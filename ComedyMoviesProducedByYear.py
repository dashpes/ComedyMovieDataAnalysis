import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
comedy_movies = pd.read_csv("data/comedy_movies.csv")

# Display the first few rows to verify data loading
print(comedy_movies.head())

# Group by startYear and count the number of movies for each year
movies_per_year = comedy_movies.groupby("startYear").size()

# Reset index to turn it into a DataFrame
movies_per_year = movies_per_year.reset_index(name="count")


# Line chart for movies produced per year
plt.figure(figsize=(18,6))
sns.lineplot(data=movies_per_year, x="startYear", y="count")
plt.title("Number of Comedy Movies Produced Per Year (Line Chart)")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(rotation=90, fontsize=6)  # Set fontsize to make labels smaller

# Bar chart for movies produced per year
plt.figure(figsize=(18,6))
sns.barplot(data=movies_per_year, x="startYear", y="count", color="skyblue")
plt.title("Number of Comedy Movies Produced Per Year (Bar Chart)")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(rotation=90, fontsize=6)  # Set fontsize to make labels smaller

# Show both charts side-by-side
plt.tight_layout()
plt.show()