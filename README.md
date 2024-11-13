# Comedy Movies Data Analysis Project

This project analyzes trends in comedy movies, focusing on aspects such as revenue, budget, profitability, and number of films produced over the last centure. Using data from popular online movie databases, we explore metrics like average ratings, decade-wise performance, and other trends in the comedy genre.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Analysis Goals](#analysis-goals)
4. [Methodology](#methodology)
5. [Requirements](#requirements)
6. [Results and Findings](#results-and-findings)
7. [How to Run](#how-to-run)
8. [Acknowledgments](#acknowledgments)

## Project Overview

The purpose of this project is to uncover patterns and insights within the comedy movie genre. By examining data on revenue, budget, release dates, and user ratings, we can better understand the profitability of comedy movies and how this genre has evolved over the years.

## Dataset

This project uses data from the following sources:

1. **IMDb**: Information about movies, such as genres, release dates, and user ratings.
2. **IMDb and TMDb Movie Metadata**: Financial information, including box office revenue and budget details, provided by Kaggle.

> **Original Data Sources**:  
> - [IMDb Dataset](https://www.imdb.com/interfaces/)
> - [IMDb and TMDb Movie Metadata on Kaggle](https://www.kaggle.com/datasets/shubhamchandra235/imdb-and-tmdb-movie-metadata-big-dataset-1m/code)

**Note:** The file name of the Kaggle dataset might vary when downloaded (e.g., `IMDB TMDB Movie Metadata Big Dataset (1M).csv`). Please check the downloaded file name and update the code accordingly if it does not match the name used in this project.

Note: The data was filtered to include only comedy movies and merged to ensure accurate financial and rating information.

## Analysis Goals

The primary goals of the analysis are:

1. Identify trends in revenue, budget, and profit over different decades.
2. Analyze the average ratings for comedy movies over time.
3. Determine the profitability trends within the comedy genre.
4. Visualize key metrics to better understand the genre’s success and patterns.
5. understand if their is truely a decline in the number of comedy movies produced and if so why that may be.

**Note:** A third analysis of just the last 30 years (1990 - 2020) may give better insights to the trend in comedy movies in their current era.

## Methodology

1. **Data Cleaning**: 
   - Filtered data to include only comedy movies.
   - Removed records with missing or zero values in key fields like `revenue` and `budget`.
   - Converted dates into appropriate formats and extracted relevant parts (e.g., year and decade).

2. **Data Analysis**:
   - Calculated decade-wise averages for revenue, budget, and profitability.
   - Aggregated ratings data to find average ratings per decade.
   - Created visualizations to highlight the findings.

3. **Visualization**:
   - Used `matplotlib` and `seaborn` to create bar charts and line plots that depict trends over time.

## Requirements

To run the analysis and generate the visualizations, you need the following Python packages:

- `pandas`
- `matplotlib`
- `seaborn`

You can install these using `requirements.txt`:

```bash
pip install -r requirements.txt
