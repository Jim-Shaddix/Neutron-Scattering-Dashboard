import pandas as pd
import numpy as np

# read in data
df = pd.read_csv("data/Data_From_1K0Slice_Integratedpm0p1.csv", names=["x", "y", "z"])
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
