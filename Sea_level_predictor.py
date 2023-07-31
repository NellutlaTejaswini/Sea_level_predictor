import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Use Pandas to import the data from "epa-sea-level.csv"
# Replace 'epa-sea-level.csv' with the actual filename or path to your dataset
df = pd.read_csv('epa-sea-level.csv')

# Use matplotlib to create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level Data', color='blue', marker='o')

# Use the linregress function to get the slope and y-intercept of the line of best fit
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit over the top of the scatter plot
plt.plot(df['Year'], slope * df['Year'] + intercept, label='Best Fit Line', color='red')

# Plot a new line of best fit using data from year 2000 to the most recent year
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
plt.plot(df['Year'], slope_recent * df['Year'] + intercept_recent, label='Best Fit Line (since 2000)', color='green')

# Set the x and y labels and the title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Set the legend
plt.legend()

# Plot the line going through year 2050
plt.axvline(x=2050, linestyle='--', color='black', label='2050 Prediction')

# Save the image and return the plot
plt.savefig('sea_level_plot.png')
plt.show()
