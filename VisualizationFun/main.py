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

def line_chart_example(x, y, y2, filename):
    plt.figure(layout="constrained")

    plt.plot(x, y, label="PTS", c="red", lw=5, ls="--")
    plt.plot(x,y2, label="MIN", c="blue")

    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.title("24-25 Men's Basketball Season Totals")
    plt.xlabel("Player")
    plt.ylabel("Season Totals")

    plt.grid()
    plt.show()
    # plt.savefig(filename)

def scatter_chart_ex(x,y, filename):
    plt.figure(layout="constrained")

    plt.scatter(x,y, s=200, marker="^")

    plt.savefig(filename)


def bar_chart_ex(x, y, filename):

    plt.figure(layout="constrained")
    plt.bar(x, y)
    plt.savefig(filename)

def pie_chart_ex(labels, y, filename):
    plt.figure()
    plt.pie(y, labels = labels, autopct="%1.1f%%")
    plt.savefig(filename)

def histogram_ex(x, filename):
    plt.figure()
    plt.hist(x, bins = 5, edgecolor="black")
    plt.savefig(filename)

def main():
    df = pd.read_csv("bball.csv", index_col = 0)
    new_row_df = pd.DataFrame([["F",3,10,0]], columns=df.columns, index = ["Noah Haaland"])
    new_row_df.index.name = df.index.name
    df = pd.concat([df,new_row_df])
    print(df.tail())

    df["CLASS"] = ["Sr", "So", "So", "So", "Sr", "Fr", "Fr", "Jr", "Jr", "Gr", "Sr", "Sr", "Sr","Jr"]
    print(df["CLASS"])

    class_counts_ser = df["CLASS"].value_counts()
    print(class_counts_ser)
    grouped_by_class = df.groupby("CLASS")
    means_pts_ser = grouped_by_class["PTS"].mean()
    print(means_pts_ser)

    line_chart_example(df.index, df["PTS"], df["MIN"], "line_example.png")

    scatter_chart_ex(df.index, df["PTS"], "scatter_chart.png")

    bar_chart_ex(class_counts_ser.index, class_counts_ser, "bar.png")

    pie_chart_ex(class_counts_ser.index, class_counts_ser, "pie.png")

    histogram_ex(df["PTS"], "histogram.png")
main()