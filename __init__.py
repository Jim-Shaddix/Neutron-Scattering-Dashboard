import pandas as pd
import numpy as np

# read in data
df = pd.read_csv("data/1K0Slice_Integratedpm0p1.csv", names=["x", "y", "z"])
x_unique = df.x.unique()
y_unique = df.y.unique()

# create z coordinate to use
# - adding a minimum value
new_z = df.z.copy()
new_z.loc[new_z < 0] = 0

# - adding a maximum value (0.057 tends to work (eliminates 3-actual values))
#  - here I am going to put a much smaller thresold value
max_z_val = 0.025
new_z.loc[new_z > max_z_val] = max_z_val


intensity = np.array(new_z).reshape(-1, (len(df.x.unique())))

# Tick marks for the x-coordinate of the heatmap
heatmap_x_tickvals = np.linspace(0,len(x_unique) - 1, 5)
heatmap_x_ticktext = [f"{x:.2f}" for x in np.linspace(df.x.min(), df.x.max(), 5)]

# Tick marks for the x-coordinate of the heatmap
heatmap_y_tickvals = np.linspace(0,len(y_unique) - 1, 5)
heatmap_y_ticktext = [f"{y:.2f}" for y in np.linspace(df.y.min(), df.y.max(), 5)]

heatmap_hovertemplate = \
    '<b>Intensity</b>: %{z}'+ \
    '<br><i>x-index</i>: %{x}<br>' + \
    '<i>y-index</i> %{y} <extra></extra>'