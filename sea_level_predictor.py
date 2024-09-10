import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )

    years_to_2050 = pd.Series(range(df["Year"].min(), 2051))
    sea_level_predict = intercept + slope * years_to_2050

    # Plotting the first line of best fit
    # Entire dataset
    ax.plot(
        years_to_2050,
        sea_level_predict,
        color="red",
        label="Best fit line (All data)",
    )

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    years_to_2050_from_2000 = pd.Series(range(2000, 2051))
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df2["Year"], df2["CSIRO Adjusted Sea Level"]
    )
    sea_level_predict2 = intercept2 + slope2 * years_to_2050_from_2000

    # Plotting the second line of best fit
    ax.plot(
        years_to_2050_from_2000,
        sea_level_predict2,
        color="green",
        label="Best fit line (2000 onwards)",
    )

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig("sea_level_plot.png")
    return ax
