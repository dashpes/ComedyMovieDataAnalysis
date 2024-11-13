import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load in the Revenue CSV
revenue = pd.read_csv("Data/Comedy_Movies_Revenue.csv")

#create a decade column
revenue["decade"] = (revenue["year"] // 10) * 10

#calculates the average revenue, budget, and profit/loss per decade
average_revenue_per_decade = revenue.groupby('decade')['revenue'].mean().reset_index()
average_budget_per_decade = revenue.groupby('decade')['budget'].mean().reset_index()
average_profitloss_per_decade = revenue.groupby('decade')['profit_loss'].mean().reset_index()

# First figure for Revenue and Budget side by side
fig1, axes1 = plt.subplots(1, 2, figsize=(15, 6))

# Plot average revenue per decade in the first subplot
sns.barplot(data=average_revenue_per_decade, x='decade', y='revenue', ax=axes1[0], palette='Blues')
axes1[0].set_title('Average Revenue per Decade')
axes1[0].set_ylabel('Average Revenue')
axes1[0].set_xlabel('Decade')

# Plot average budget per decade in the second subplot
sns.barplot(data=average_budget_per_decade, x='decade', y='budget', ax=axes1[1], palette='Greens')
axes1[1].set_title('Average Budget per Decade')
axes1[1].set_ylabel('Average Budget')
axes1[1].set_xlabel('Decade')

# Adjust layout for better spacing
plt.tight_layout()

# Second figure for Profit/Loss
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Plot average profit/loss per decade in a separate figure
sns.barplot(data=average_profitloss_per_decade, x='decade', y='profit_loss', ax=ax2, palette='Reds')
ax2.set_title('Average Profit/Loss per Decade')
ax2.set_ylabel('Average Profit/Loss')
ax2.set_xlabel('Decade')

# Show both figures
plt.show()