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

# there is always a "current" figure
# https://matplotlib.org/stable/api/pyplot_summary.html
# 2. using the OOP interface
# 3. a mix of the two

def line_chart_example(df,filename):
    plt.figure(layout="constrained")
    x = df.index
    y = df["PTS"]
    y2 = df["MIN"]
    plt.plot(x, y, label="PTS", c="red", lw=5, ls="--")
    plt.plot(x,y2, label="MIN", c="blue")

    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.title("24-25 Men's Basketball Season Totals")
    plt.xlabel("Player")
    plt.ylabel("Season Totals")

    plt.grid()
    # plt.show()
    plt.savefig(filename)

def scatter_chart_ex(df, filename):
    plt.figure(layout="constrained")
    df_sorted_by_points = df.sort_values(by="PTS", ascending=False)
    x = df_sorted_by_points.index
    y = df_sorted_by_points["PTS"]

    plt.scatter(x,y, s=200, marker="^")
    plt.xticks(rotation=45, ha="right")
    plt.savefig(filename)

def scatter_chart_pts_per_min(df, filename):
    plt.figure(layout="constrained")
    df["PTS PER MIN"] = df["PTS"]/df["MIN"]
    df_sorted_by_points = df.sort_values(by="PTS PER MIN", ascending=False)
    x = df_sorted_by_points.index
    y = df_sorted_by_points["PTS PER MIN"]

    plt.scatter(x,y, s=200, marker="x")
    plt.xticks(rotation=45, ha="right")
    plt.savefig(filename)

def bar_chart_ex(ser, filename):
    x = ser.index
    y = ser
    plt.figure(layout="constrained")
    plt.bar(x, y)
    plt.savefig(filename)

def pie_chart_ex(ser, filename):
    plt.figure()
    labels = ser.index
    y = ser
    plt.pie(y, labels = labels, autopct="%1.1f%%")
    plt.savefig(filename)

def histogram_ex(x, filename):
    plt.figure()
    plt.hist(x, bins=5, edgecolor="black")
    plt.title("Distribution of Player Points Scored")
    plt.xlabel("Total Season Points Scored")
    plt.ylabel("Number of Players")
    plt.savefig(filename)

def main():
    df = pd.read_csv("bball.csv", index_col = 0)

    class_counts_ser = df["CLASS"].value_counts()
    print(class_counts_ser)

    grouped_by_class = df.groupby("CLASS")
    means_pts_ser = grouped_by_class["PTS"].mean()
    print(means_pts_ser)

    line_chart_example(df, "figures/line_example.png")
    scatter_chart_ex(df, "figures/scatter_chart.png")
    scatter_chart_pts_per_min(df, "figures/scatter_chart_pts_per_min.png")
    bar_chart_ex(class_counts_ser, "figures/bar.png")
    pie_chart_ex(class_counts_ser, "figures/pie.png")
    histogram_ex(df["PTS"], "figures/histogram.png")
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

