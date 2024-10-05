import pandas as pd

# Reading weather data CSV and parsing the "day" column as date type
weather_report = pd.read_csv("C:\\Users\\Prashant Jha\\Desktop\\weather_data.csv", parse_dates=["day"])
weather_report.set_index("day", inplace=True)

# Forward filling: Filling missing values (NaN) with the previous day's data
ffill = weather_report.fillna(method="ffill")
# print(ffill)

# Backward filling: Filling missing values (NaN) with the next day's data
bfill = weather_report.fillna(method="bfill")
# print(bfill)

# Filling missing values along the column axis using backward filling
new = weather_report.fillna(method="bfill", axis="columns")
# print(new)

# Interpolating missing data using time-based linear interpolation
weather_report.interpolate(method="time")
# print(weather_report)

# Dropping rows with NaN values (if how="all", it drops rows where all values are NaN)
weather_report.dropna()  # inplace=True, how="all"
# print(weather_report)

# Dropping rows with less than 1 non-NaN value (controlled by thresh parameter)
weather_report.dropna(thresh=1)  # inplace=True
# print(weather_report)

# Reindexing the DataFrame using a new date range
dt = pd.date_range("01-01-2017", "26-01-2017")
ind = pd.DatetimeIndex(dt)
weather_report.reindex(ind)

# Printing the updated weather report
print(weather_report)
