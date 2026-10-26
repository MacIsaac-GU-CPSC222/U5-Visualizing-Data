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

# ============================================================
# GENERAL DATA VISUALIZATION TIPS
# ============================================================
# 1. Choose a chart based on the question you want to answer.
# 2. Include descriptive titles and label axes with units.
# 3. Avoid misleading scales and unnecessary visual clutter.
# 4. Use colors and annotations to highlight important information.
# 5. Keep plots simple enough to understand at a glance.
# 6. Consider whether your chart accurately represents the data.
# 7. A good visualization should help reveal information that
#    might be difficult to recognize from a table of numbers.

# we will use the matplotlib library for charting
# there is always a "current" figure
import matplotlib.pyplot as plt


def line_chart_example(df,filename):
    # LINE CHART
    # Best for: Showing trends or changes over time or ordered data.
    # Benefits:
    # - Makes it easy to identify trends (increasing/decreasing).
    # - Useful for comparing how multiple variables change over time.
    # - Highlights patterns, peaks, and dips.
    # Example: Points scored by a basketball team across a season.
    # NOTE: Avoid connecting unrelated categories (e.g., player names)
    # because the lines imply continuity between observations.
    pass

def scatter_chart_ex(df, filename):
    # SCATTER PLOT
    # Best for: Exploring relationships between two numerical variables.
    # Benefits:
    # - Helps identify correlations (positive, negative, or none).
    # - Makes it easy to spot clusters and outliers.
    # - Shows how individual observations are distributed.
    # Example: Minutes played vs. points scored for each player.
    # NOTE: Correlation does not necessarily imply causation.
    pass


def bar_chart_ex(ser, filename):
    # BAR CHART
    # Best for: Comparing values across different categories.
    # Benefits:
    # - Makes it easy to compare quantities and identify rankings.
    # - Works well with categorical data.
    # - Horizontal bars are especially useful for long category names.
    # Example: Total points scored by each player or class.
    # NOTE: Bar charts should generally start their value axis at zero.
    pass

def points_per_min_chart(df, filename):
    pass

    plt.savefig(filename)

def pie_chart_ex(ser, filename):
    # PIE CHART
    # Best for: Showing how categories contribute to a whole.
    # Benefits:
    # - Makes proportions and percentages easy to visualize.
    # - Useful when there are only a few categories.
    # Example: Percentage of players in each class.
    # NOTE: All slices should represent parts of the same whole.
    # Bar charts are often better for comparing similar percentages.
    pass

def histogram_ex(x, filename):
    # HISTOGRAM
    # Best for: Showing the distribution of a numerical variable.
    # Benefits:
    # - Shows how frequently values occur within ranges (bins).
    # - Helps identify the shape, spread, and skew of data.
    # - Can reveal clusters, gaps, and possible outliers.
    # Example: Distribution of total points scored by players.
    # NOTE: Unlike bar charts, histograms group numerical values
    # into intervals rather than displaying separate categories.
    # The number of bins can significantly change the appearance.
    pass


def main():
    # data source: https://www.sports-reference.com/cbb/players/graham-ike-1/gamelog/2025
    pass

main()
# TASK 1: TOP 5 SCORERS (bball.csv)
# Create a horizontal bar chart showing the five players
# with the most total points scored.
# - Sort the DataFrame by PTS.
# - Display only the top five players.
# - Make the highest-scoring player's bar a different color.
# - use plt.barh() for horizontal bar
# QUESTION: How much more did the top scorer score than
# the fifth-highest scorer?


# TASK 2: SHOT ATTEMPTS VS. POINTS (ike_game_stats.csv)
# Investigate whether Ike scores more points in games
# where he attempts more field goals.
# - Create a scatter plot using FGA and PTS.
# - X-axis: Field Goal Attempts
# - Y-axis: Points Scored
# - Customize the appearance of the points.
#
# QUESTION: Is there a relationship between field goal
# attempts and points scored? Are there any outliers?
#
# BONUS: Annotate the highest-scoring game with
# the name of the opponent (Opp).


# TASK 3: POINTS BY CLASS (bball.csv)
# Investigate which class contributes the most scoring.
# - Use groupby() and sum() to calculate the total
#   points scored by each class.
# - Create an appropriate chart comparing the classes.
#
# QUESTION: Does the class with the most total points
# also have the highest average points per player?
# Why might these rankings be different?

