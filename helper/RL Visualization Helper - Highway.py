import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

# Read in the file
path = "/home/maria-visinescu/iPLAN/results/sacred/5/results.csv"
df = pd.read_csv(path)

# Get the columns from the df
x = df["Time_step"]
reward = df["Average reward"]
length = df["Average Episode Length"]
win = df["Average Win Num"]

# Calculate the linear trend
z = np.polyfit(x, reward, 1)
p = np.poly1d(z)
trend = p(x)

# Plot the reward and the linear trend
plt.figure(figsize=(10,6))
plt.plot(x, reward, label="Raw Reward")
plt.plot(x, trend, color="red", label="Linear Trend")
plt.xlabel("Timesteps")
plt.ylabel("Average Reward")
plt.title("Episodic Reward")
plt.legend()
plt.grid()
plt.show()