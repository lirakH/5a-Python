"""

Data Visualization with Matplotlib,
Seaborn and Plotly


Types of visualization:

- Bar Charts: Display data using rectangular bars,
  where the length or height of bars corresponds
  to the values they represent. Bar charts are
  effective for comparing discrete categories of
  data. 

- Line Charts: Show data points connected by
  straight lines, making them ideal for showing
  trends or changes over time. Line Charts are
  useful for visualizing continuous data series. 

- Scatter Plots: Represent individual data points
  on a two-dimensional graph, where each axis
  represents a different variable. Scatter Plots
  are useful for showing relationships between
  pairs of variables. 

- Pie Charts: Display data as slices of a circular
  pie, representing parts of a whole. Pie Charts
  are useful for illustrating how parts relate to
  the whole, such as market share or percentages. 

"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("avgIQpercountry.csv")


filtered_df = df[df["Average IQ"] >= 100]

filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

print(filtered_df)

plt.figure(figsize=(14,8))

bars = plt.bar(filtered_df["Country"], filtered_df["Average IQ"], color="red")

plt.title("Average IQ by Country (IQ >= 100)", fontsize=16)

plt.xlabel("Country", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

plt.grid(axis="y", linestyle="--", alpha=0.8)

plt.bar_label(bars, fmt="%.2f", fontsize=10, color="black")

plt.xticks(rotation=90, fontsize=10)

plt.show()          



