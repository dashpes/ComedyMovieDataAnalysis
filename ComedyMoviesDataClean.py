import pandas as pd

# Load title.basics.tsv and title.ratings.tsv
basics_df = pd.read_csv("Data/title.basics.tsv", sep="\t", low_memory=False)
ratings_df = pd.read_csv("Data/title.ratings.tsv", sep="\t", low_memory=False)

# Display the first few rows to understand the data structure
print(basics_df.head())
print(ratings_df.head())

# Filter basics_df to keep only movies
movies_df = basics_df[basics_df['titleType'] == 'movie']

# Filter to keep only comedy movies
comedy_movies_df = movies_df[movies_df['genres'].str.contains('Comedy', na=False)]

# Merge comedy movies with their ratings
comedy_movies_with_ratings_df = comedy_movies_df.merge(ratings_df, on='tconst', how='inner')

# Select only the columns we need for analysis
comedy_movies_final = comedy_movies_with_ratings_df[['primaryTitle', 'startYear', 'genres', 'averageRating', 'numVotes']]

# Save to a CSV file
comedy_movies_final.to_csv("comedy_movies.csv", index=False)