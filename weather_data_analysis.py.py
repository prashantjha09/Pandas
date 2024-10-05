# Here we will be working on the CSV file which is a weather report:
import pandas as pd

# Reading the CSV file containing weather data
weather_data = pd.read_csv("C:\\Users\\Prashant Jha\\Desktop\\weather_data.csv")

# Printing the complete data
print(weather_data)

# Printing selected columns (temperature and windspeed)
print(weather_data[["temperature", "windspeed"]])

# Printing the type of the data
print(type(weather_data))

# Printing the shape of the data (number of rows and columns)
print(weather_data.shape)

# Adding a new column 'index' and setting it as the index
weather_data["index"] = range(1, weather_data.shape[0] + 1)
weather_data.set_index("index", inplace=True)
print(weather_data)

# Printing maximum, mean, minimum, and standard deviation of temperature
print("Maximum temperature is " + str(weather_data["temperature"].max()))
print("Mean temperature is " + str(weather_data["temperature"].mean()))
print("Minimum temperature is " + str(weather_data["temperature"].min()))
print("Std temperature is " + str(weather_data["temperature"].std()))

# Describing statistics of the data
print(weather_data.describe())

# Printing data based on certain conditions
print(weather_data[weather_data["temperature"] > 30])  # Where temperature is above 30
print(weather_data[(weather_data["temperature"] > 30) & (weather_data["temperature"] < 33)])  # Temperature between 30 and 33
print(weather_data[(weather_data.temperature > 32) | (weather_data.temperature < 25)])  # Temperature above 32 or below 25

# Creating a DataFrame using a Python list of tuples
data = [("Jan", 23, 7), ("Feb", 24, 8), ("Mar", 30, 6), ("April", 32, 8), ("May", 34, 9), ("Jun", 35, 9)]
pd_data = pd.DataFrame(data, columns=["Months", "Temperature", "WindSpeed"])

# Printing the new DataFrame
print(pd_data)
