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

# lets start with a simple line chart
def line_chart_example(x, y, y2, filename):
    plt.figure()
    # assume that x and y are parallel sequences
    # lists, tuples, series, numpy arrays, etc.
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
    plt.plot(x, y, label="PTS", c="red", lw=5, ls="--")
    plt.plot(x, y2, label="MIN")

    # lets beautify the plot!
    plt.xticks(rotation=45, ha="right")

    plt.xlabel("Player")
    plt.ylabel("Season Totals")
    plt.title("24-25 Men's Basketball Season Totals")
    plt.grid()
    plt.legend()

    plt.tight_layout() # right before showing or saving the chart

    # 3 ways to show the chart
    # 1. plt.show() shows an interactive desktop window
    # plt.show()
    # 2. plt.savefig()
    plt.savefig(filename)
    # 3. show the chart inline in a jupyter notebook

def scatter_chart_example(x, y, filename):
    plt.figure() # a new "current" figure
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter
    plt.scatter(x, y, s=200, marker="x")
    plt.savefig(filename)

def bar_chart_example(x, y, filename):
    plt.figure() # a new "current" figure
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar
    plt.bar(x, y)
    plt.savefig(filename)

def pie_chart_example(labels, y, filename):
    plt.figure() # a new "current" figure
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie
    plt.pie(y, labels=labels, autopct="%1.1f%%")
    plt.savefig(filename)

def histogram_chart_example(x, filename):
    plt.figure() # a new "current" figure
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
    plt.hist(x, bins=5, edgecolor="black")
    plt.savefig(filename)

def main():
    df = pd.read_csv("bball.csv", index_col=0)
    new_row_df = pd.DataFrame([["F",3,10,0]], columns=df.columns, index=["Noah Haaland"])
    new_row_df.index.name = df.index.name
    df = pd.concat([df, new_row_df])
    df["CLASS"] = ["Sr", "So", "So", "So", "Sr", "Fr", "Fr", "Jr", "Jr", "Gr", "Sr", "Sr", "Sr", "Jr"]
    print(df)

    class_counts_ser = df["CLASS"].value_counts()
    print(class_counts_ser)

    grouped_by_class = df.groupby("CLASS")
    mean_pts_ser = grouped_by_class["PTS"].mean()
    print(mean_pts_ser)

    # challenge!
    ppg_ser = df["PTS"] / df["GP"]
    print(ppg_ser)
    print(ppg_ser[ppg_ser == ppg_ser.max()])
    # another way
    print(ppg_ser.index[ppg_ser.argmax()], ppg_ser.iloc[ppg_ser.argmax()])
    # another way
    ppg_ser = ppg_ser.sort_values(ascending=False)
    print(ppg_ser.index[0], ppg_ser.iloc[0])

    # game plan
    # 1. line chart (check!)
    # simple charting examples for demonstration purposes only
    # (not the best way to visualize some of the data)
    line_chart_example(df.index, df["PTS"], df["MIN"], "line_example.png")
    # 2. scatter chart
    scatter_chart_example(df.index, df["PTS"], "scatter_example.png")
    # 3. bar chart
    bar_chart_example(class_counts_ser.index, class_counts_ser, "bar_example.png")
    # 4. pie chart
    pie_chart_example(class_counts_ser.index, class_counts_ser, "pie_example.png")
    # 5. histogram chart
    histogram_chart_example(df["PTS"], "hist_example.png")
    # 6. boxplot (later)

main()