import pandas as pd

#loads the file into a dataframe
revenue_df = pd.read_csv("Data/IMDBTMDBMovieMetadataBigDataset.csv", sep=",", low_memory=False)

#display the first few rows to understand the data
print(revenue_df.head())

#filter down to only comedy movies
comedy_revenue_df = revenue_df[revenue_df['genres_list'].str.contains('Comedy', na=False)]

#select all the columns we need
comedy_revenue_df = comedy_revenue_df[['release_date', 'revenue', 'budget']]

# Remove rows where either 'revenue' or 'budget' is zero
comedy_revenue_df = comedy_revenue_df[(comedy_revenue_df['revenue'] != 0) & (comedy_revenue_df['budget'] != 0)]

# Remove rows where 'release_date' is NaN
comedy_revenue_df = comedy_revenue_df.dropna(subset=['release_date'])

# Create a new column 'profitloss' by subtracting 'budget' from 'revenue'
comedy_revenue_df['profit_loss'] = comedy_revenue_df['revenue'] - comedy_revenue_df['budget']

# Ensure 'release_date' is in datetime format
comedy_revenue_df['release_date'] = pd.to_datetime(comedy_revenue_df['release_date'], errors='coerce')

# Extract the year from 'release_date'
comedy_revenue_df['year'] = comedy_revenue_df['release_date'].dt.year

# Fill NaN values with a specific value, if needed (e.g., filling NaN years with 0)
comedy_revenue_df['year'] = comedy_revenue_df['year'].fillna(0).astype(int)

#print the first few lines to make sure the correct data has been filtered and cleaned
print(comedy_revenue_df.head())

#export to a csv
comedy_revenue_df.to_csv("Comedy_Movies_Revenue.csv", index=False)