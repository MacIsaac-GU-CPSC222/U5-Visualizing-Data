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
    plt.figure(layout="constrained")
    df = df.sort_values("Date")
    x = df["Date"]
    print(x)
    y = df["PTS"]
    y2 = df["MP"]
    plt.plot(x, y, label="Points", c="red",lw=2, ls="--", marker="o")

    plt.plot(x, y2, label="Minutes", c="blue", lw=2, marker="o")

    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.title("Graham Ike: Points and Minutes by Game (2024–25)")
    plt.xlabel("Game Date")
    plt.ylabel("Mins/Pts")

    plt.grid()
    # plt.show()
    plt.savefig(filename)

def scatter_chart_ex(df, filename):
    # SCATTER PLOT
    # Best for: Exploring relationships between two numerical variables.
    # Benefits:
    # - Helps identify correlations (positive, negative, or none).
    # - Makes it easy to spot clusters and outliers.
    # - Shows how individual observations are distributed.
    # Example: Minutes played vs. points scored for each player.
    # NOTE: Correlation does not necessarily imply causation.
    plt.figure(layout="constrained")

    x = df["MIN"]
    y = df["PTS"]

    plt.scatter(x, y, s=100, marker="^", c="blue")

    plt.title("Playing Time vs. Points Scored")
    plt.xlabel("Total Minutes Played")
    plt.ylabel("Total Points Scored")
    plt.grid(alpha=0.3)

    plt.savefig(filename)


def bar_chart_ex(ser, filename):
    # BAR CHART
    # Best for: Comparing values across different categories.
    # Benefits:
    # - Makes it easy to compare quantities and identify rankings.
    # - Works well with categorical data.
    # - Horizontal bars are especially useful for long category names.
    # Example: Total points scored by each player or class.
    # NOTE: Bar charts should generally start their value axis at zero.
    x = ser.index
    y = ser
    plt.figure(layout="constrained")
    plt.bar(x, y, color=["red", "blue", "yellow"])
    plt.savefig(filename)

def points_per_min_chart(df, filename):
    plt.figure(layout="constrained")

    df = df[df["MIN"] > 0].copy()
    df["PTS PER MIN"] = df["PTS"] / df["MIN"]

    df_sorted = df.sort_values("PTS PER MIN")

    plt.barh(df_sorted.index, df_sorted["PTS PER MIN"])

    plt.title("Scoring Efficiency by Player")
    plt.xlabel("Points Per Minute")
    plt.ylabel("Player")

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
    plt.figure()
    labels = ser.index
    y = ser
    plt.pie(y, labels = labels, autopct="%1.1f%%")
    plt.savefig(filename)

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
    plt.figure()
    plt.hist(x, bins=5, edgecolor="black")
    plt.title("Distribution of Player Points Scored")
    plt.xlabel("Total Season Points Scored")
    plt.ylabel("Number of Players")
    plt.savefig(filename)

def task1(df):
    top_5 = df.sort_values("PTS", ascending=False).head(5)

    colors = ["red", "blue", "blue", "blue", "blue"]

    plt.figure(layout="constrained")
    plt.barh(top_5.index, top_5["PTS"], color=colors)
    plt.gca().invert_yaxis() # to invert order
    plt.title("Top 5 Scorers")
    plt.xlabel("Total Points")
    plt.ylabel("Player")
    plt.savefig("figures/task1")
def task2(df):
    fga = df["FGA"]
    pts = df["PTS"]
    plt.figure(layout="constrained")
    plt.scatter(fga, pts)
    plt.title("Field Goal Attempts vs. Points Scored")
    plt.xlabel("Field Goal Attempts")
    plt.ylabel("Points Scored")

    # extras:
    top_game = df.loc[df["PTS"].idxmax()]
    plt.annotate(top_game["Opp"],
                (top_game["FGA"], top_game["PTS"]),
                xytext=(10, 0), textcoords="offset points")
    plt.grid()
    plt.savefig("figures/task2.png")

def task3(df):
    sum_per_class = df.groupby("CLASS")["PTS"].sum()
    sum_per_class = sum_per_class.loc[["Fr", "So", "Jr","Sr","Gr"]]
    plt.figure(layout="constrained")
    plt.bar(sum_per_class.index, sum_per_class)
    plt.title("Total Points by Class")
    plt.xlabel("Class")
    plt.ylabel("Total Points")
  
    plt.savefig("figures/task3.png")

def main():
    # data source: https://www.sports-reference.com/cbb/players/graham-ike-1/gamelog/2025
    df_ike = pd.read_csv("ike_game_stats.csv",)
    df_ike["Date"] = pd.to_datetime(df_ike["Date"], format="%Y-%m-%d")
    line_chart_example(df_ike, "figures/line_example.png")
    
    
    df = pd.read_csv("bball.csv", index_col = 0)
    scatter_chart_ex(df, "figures/scatter_chart.png")
    
    class_counts_ser = df["CLASS"].value_counts()
    print(class_counts_ser)

    grouped_by_class = df.groupby("CLASS")
    means_pts_ser = grouped_by_class["PTS"].mean()
    print(means_pts_ser)

    bar_chart_ex(class_counts_ser, "figures/bar.png")
    bar_chart_ex(means_pts_ser, "figures/average_pts_by_class.png")
    points_per_min_chart(df, "figures/scoring_efficiency.png")
    pie_chart_ex(class_counts_ser, "figures/pie.png")
    histogram_ex(df["PTS"], "figures/histogram.png")

    task1(df)
    task2(df_ike)
    task3(df)

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

