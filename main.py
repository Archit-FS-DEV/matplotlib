# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# ------------------------- Line Plot Example ------------------------- #
# Example data for line plot
a = [0, 1, 2, 3, 5, 6, 3, 6]
b = [2, 3, 4, 5, 6, 7, 8, 5]

# Create figure with custom size and resolution
plt.figure(figsize=(6, 3), dpi=120)

# Add title and labels to the plot
plt.title("Our First Graph", fontdict={"fontsize": 20})
plt.xlabel("X Axis", fontdict={"fontsize": 20})
plt.ylabel("Y Axis", fontdict={"fontsize": 20})

# Customize x-axis and y-axis ticks
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Plot the data with customizations
plt.plot(a, b, label="2x", color="#1f77b4", linewidth=2, linestyle='--',
         marker='.', markersize=16, markeredgecolor='red')

# Add a second line plot with partial data
x2 = np.arange(0, 4, 0.3)
plt.plot(x2[:6], x2[:6] ** 2, color='red', label="x2 (partial)")
plt.plot(x2[5:], x2[5:] ** 2, 'r.--', label="x2 (rest)")

# Add legend and save the figure
plt.legend()
plt.savefig("my_plot.png", dpi=300)  # Save the plot as a PNG image
plt.show()

# ------------------------- Fuel Prices Dataset ------------------------- #
# Load the dataset
gas = pd.read_csv("/path/to/your/fuel_prices.csv")

# ------------------------- Line Plot for USA and Canada ------------------------- #
plt.figure(figsize=(9, 7))  # Set figure size

# Plot fuel prices for USA and Canada
plt.plot(gas["Year"], gas["USA"], 'r.-', label="USA")
plt.plot(gas["Year"], gas["Canada"], 'b.-', label="Canada")

# Customize the plot
plt.title("USA vs Canada Gas Prices", fontdict={"fontsize": 20})
plt.xlabel("Year")
plt.ylabel("Dollar/Gallon")
plt.xticks(np.arange(2000, 2022, 2))  # Set x-axis ticks
plt.legend()
plt.show()

# ------------------------- Bar Plot for Fuel Prices in 2020 ------------------------- #
# Filter the data for the year 2020
gas_2020 = gas[gas["Year"] == 2020]

plt.figure(figsize=(10, 6))

# Create a bar plot for fuel prices in 2020
plt.bar(gas_2020.columns[1:-2], gas_2020.iloc[0, 1:-2], color='skyblue')

# Add labels, title, and rotate x-axis labels for readability
plt.title("Fuel Prices in 2020 (USD per Gallon)")
plt.xlabel("Countries")
plt.ylabel("Fuel Price (USD)")
plt.xticks(rotation=45)
plt.show()

# ------------------------- Line Plot for Multiple Countries ------------------------- #
plt.figure(figsize=(12, 8))

# Plot fuel prices for selected countries
plt.plot(gas["Year"], gas["USA"], 'r.-', label="USA")
plt.plot(gas["Year"], gas["China"], 'b.-', label="China")
plt.plot(gas["Year"], gas["India"], 'g.-', label="India")

# Add labels, grid, and legend
plt.title("Fuel Price Trends (2000–2020)")
plt.xlabel("Year")
plt.ylabel("Fuel Price (USD per Gallon)")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------- Stacked Bar Chart ------------------------- #
# Define data for the stacked bar chart
years = gas["Year"]
usa = gas["USA"]
china = gas["China"]
india = gas["India"]

plt.figure(figsize=(10, 6))

# Create stacked bar chart
plt.bar(years, usa, color='red', label='USA')
plt.bar(years, china, bottom=usa, color='blue', label='China')
plt.bar(years, india, bottom=usa + china, color='green', label='India')

# Add labels, title, and legend
plt.title("Cumulative Fuel Prices Over Time")
plt.xlabel("Year")
plt.ylabel("Fuel Price (USD per Gallon)")
plt.legend()
plt.show()

# ------------------------- Pie Chart ------------------------- #
# Filter fuel prices for 2020
fuel_2020 = gas[gas["Year"] == 2020]
fuel_prices = fuel_2020.iloc[0, 1:-2]
countries = fuel_2020.columns[1:-2]

plt.figure(figsize=(8, 8))

# Create a pie chart
plt.pie(fuel_prices, labels=countries, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)

# Add title
plt.title("Fuel Price Share by Country in 2020")
plt.show()

# ------------------------- 3D Scatter Plot ------------------------- #
# Create a 3D scatter plot for USA, India, and Canada
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with transparency and color
ax.scatter(gas["USA"], gas["India"], gas["Canada"], color='purple', alpha=0.7)

# Add labels and title for the 3D plot
ax.set_title("Fuel Prices: USA, India, and Canada (3D)")
ax.set_xlabel("USA (USD)")
ax.set_ylabel("India (USD)")
ax.set_zlabel("Canada (USD)")

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.show()

# ------------------------- FIFA Data Visualizations ------------------------- #
# Load the FIFA dataset
fifa = pd.read_csv("/path/to/your/fifa_data.csv")

# ------------------------- Histogram for Player Ratings ------------------------- #
plt.figure(figsize=(10, 6), dpi=120)
plt.hist(fifa['Overall'], bins=20, color='skyblue', edgecolor='black', alpha=1)

# Add title and labels
plt.title("Distribution of FIFA Player Ratings", fontsize=16)
plt.xlabel("Player Overall Rating", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=1)

# Display the histogram
plt.show()

# ------------------------- Pie Chart for Preferred Foot ------------------------- #
foot_counts = fifa['Preferred Foot'].value_counts()

# List of start angles you want to test
angles = [0, 90, 180, 270]

# Create a pie chart for each angle and display it
for angle in angles:
    plt.figure(figsize=(6, 6))  # Set the figure size for each plot
    plt.pie(foot_counts, labels=foot_counts.index, autopct='%1.1f%%', startangle=angle, colors=['lightblue', 'lightgreen'])
    plt.title(f"Distribution of Preferred Foot (Start Angle = {angle}°)")
    plt.show()

# ------------------------- Pie Chart for Player Weight Distribution ------------------------- #
# Convert Weight to integers (strip 'lbs')
fifa['Weight'] = fifa['Weight'].apply(lambda x: int(x.strip('lbs')) if isinstance(x, str) else x)

# Calculate counts for each weight category
light = fifa[fifa['Weight'] < 125].shape[0]
light_medium = fifa[(fifa['Weight'] >= 125) & (fifa['Weight'] < 150)].shape[0]
medium = fifa[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].shape[0]
medium_heavy = fifa[(fifa['Weight'] >= 175) & (fifa['Weight'] < 190)].shape[0]
heavy = fifa[fifa['Weight'] >= 190].shape[0]

# Labels and counts
labels = ['Light (<125lbs)', 'Light-Medium (125–149lbs)', 'Medium (150–174lbs)',
          'Medium-Heavy (175–189lbs)', 'Heavy (>=190lbs)']
counts = [light, light_medium, medium, medium_heavy, heavy]
explode = (.1, .1, 0, 0, .1)

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=labels, autopct='%0.2f%%', startangle=0, pctdistance=0.85, explode=explode)
plt.title("Player Weight Distribution")
plt.show()

# ------------------------- Box Plot for Comparison of Clubs ------------------------- #
fc = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
man_city = fifa.loc[fifa.Club == 'Manchester City']['Overall']

# Create a boxplot
plt.boxplot([fc, madrid, man_city], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='purple'))

# Add labels and title
plt.xticks([1, 2, 3], ['FC Barcelona', 'Real Madrid', 'Manchester City'])
plt.ylabel('Overall Rating')
plt.title('Comparison of Overall Ratings of Players from Three Clubs')

# Show the plot
plt.show()
