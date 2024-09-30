import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Categories for the radar chart
categories = ['Innovation', 'Cost Efficiency', 'Independence from Network', 'Scalability', 'Data Security']

# Number of categories
N = len(categories)

# Values for each competitor and your company (adjusted scalability)
dronetech_values =      [7, 8, 1, 9, 5]   # Dronetech's qualities
# use of ai + cloud computing + 5g ; unknown but should be low since they are a service provider
# verdy dependent on 5G network ; connection to multiple devices through 5G; all data through 5G
# https://enterprise.dji.com/de/matrice-300/specs
# https://enterprise.dji.com/de/matrice-30
dji_values =            [9, 4, 7, 6, 8]   # DJI's qualities:
# modern system, fast, high-precision, fast-charging; very expensive (18.000€+);
# 2 km without external systems + extra relais-tower available (make it slightly dependent; work together DJI RC Plus + Mavic 3M; wifi, bluetooth
ageagle_values =        [8, 2, 9, 3, 9]   # AgEagle's qualities
# lightweight, fast; expensive just for mapping 12000€+
# no network needed ; no scale options, drone upgradeable; radio encrypted AES 254
your_company_values =   [7, 9, 9, 6, 9]   # Our company's qualities
# mid innovative; low price
# closed local network; extra stations needed; local transmission

# Creating the angle for the plot
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Function to plot values
def add_to_radar(values, label, color):
    values += values[:1]
    ax.fill(angles, values, color, alpha=0.2)  # Softened fill color for better visibility
    ax.plot(angles, values, color, linewidth=2, linestyle='solid', label=label)

# Plot each competitor's values and your company's values
add_to_radar(dronetech_values, 'Dronetech', 'blue')
add_to_radar(dji_values, 'DJI', 'orange')
add_to_radar(ageagle_values, 'AgEagle', 'green')
add_to_radar(your_company_values, 'Our Company', 'red')

# Adding labels to each axis, with padding to avoid overlap
plt.xticks(angles[:-1], categories, size=10, horizontalalignment='center')
ax.tick_params(pad=15)  # Add padding to move the labels outside of the plot

# Adjust the legend position to avoid overlap with the chart and ensure full visibility
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=9, frameon=False)

# Title of the chart
plt.title("Comparison of Strengths and Weaknesses with Competitors", pad=40)

# Increase padding between axis labels and plot to avoid overlap
ax.set_rlabel_position(30)

# Show the radar chart
plt.tight_layout()
plt.show()
