import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data for bar and line plot
data = {"x": [11, 2, 3, 4, 5, 16, 7], "y": [10, 11, 12, 13, 4, 15, 16]}
df = pd.DataFrame(data)

# Saving the data to a CSV file
df.to_csv("out1.csv", index=False)

# Loading the data from the CSV file
x, y = np.loadtxt("out1.csv", delimiter=",", skiprows=1, unpack=True)

# Bar plot
plt.bar(x, y, color='red')
plt.show()

# Line plot
plt.plot(x, y, color='b')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Data")
plt.legend()
plt.show()
