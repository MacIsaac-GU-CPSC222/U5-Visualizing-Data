import pandas as pd

# DATA VIS NOTES
# EDA: exploratory data analysis
# getting familiar with your data
# exploring data, visualizing data, mining data

# goals of data visualization
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing understanding
# 3. label units and points of interest

# some jargon
# chart: a 2D visualization
# plot: a chart of data points (e.g., scatter plot)
# graph: a chart of a math function (e.g., sine)

# we will use the matplotlib library for charting
# 3 ways to use matplotlib
# 1. using the pyplot submodule
import matplotlib.pyplot as plt


def main():
    # TODO: Follow along with our demo starting here
    pass
    
main()



# TASK 1: TOP 5 SCORERS
# Create a horizontal bar chart showing the five players
# with the most total points.
# - Sort the DataFrame by PTS.
# - Display only the top five players.
# - BONUS: Make the highest-scoring player's bar a
#   different color.
#
# TASK 2: MINUTES VS. POINTS
# Create a scatter plot investigating the relationship
# between minutes played (MIN) and points scored (PTS).
# - X-axis: Minutes played
# - Y-axis: Total points scored
# - Customize the marker size, color, or style.
# - QUESTION: Do players who play more minutes generally
#   score more points? Are there any outliers?
# - BONUS: Annotate the player with the most points.
#
# TASK 3: POINTS BY CLASS
# Create a bar chart showing the total points scored
# by each class (Fr, So, Jr, Sr, Gr).
# - Use groupby() and sum() to calculate totals.
# - BONUS: Create a second chart showing the average
#   points per player in each class.
# - QUESTION: Does the class with the most total points
#   also have the highest average points per player?
