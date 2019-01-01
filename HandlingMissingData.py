import pandas as pd
# weather_report=pd.read_csv("C:\\Users\Prashant Jha\Desktop\weather_data.csv")
# print(weather_report)
# print(type(weather_report["day"]))
# Now we day is string type so we need to make it as date type
weather_report=pd.read_csv("C:\\Users\Prashant Jha\Desktop\weather_data.csv",parse_dates=["day"])
weather_report.set_index("day",inplace=True)
# weather_report.fillna({"temperature":0,"event":"Not available","windspeed":"Not availabe",},inplace=True)
# print(weather_report)
# we will fill the previous day value at place of nan(ffill)
ffill=weather_report.fillna(method="ffill",)#we can also give inplaceis true
# print(ffill)
# we will fill the next day value at place of nan(bfill)
bfill=weather_report.fillna(method="bfill")#we can also give inplaceis true
# print(bfill)

# we can also use axis as if required by the data
new=weather_report.fillna(method="bfill",axis="columns")
# print(new)


#for better guess of data we can use linerInterpolation
#method : {‘linear’, ‘time’, ‘index’, ‘values’, ‘nearest’, ‘zero’,
#           ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘krogh’, ‘polynomial’, ‘spline’, ‘piecewise_polynomial’, ‘from_derivatives’, ‘pchip’, ‘akima’}
weather_report.interpolate(method="time")
# print(weather_report)


#if we want to delete data having na value here if we give how="all" it will drop only the row which wilkl be having all the nan value
weather_report.dropna()#inplace=True  ,how="all"
# print(weather_report)

# here we can give thresh as a parameter will mean how many valid value we need to keep the data in the dataframe
weather_report.dropna(thresh=1)#,inplace=True
# print(weather_report)

# Reindexing the dataframe using dattime and reindexing
dt=pd.date_range("01-01-2017","26-01-2017")
ind=pd.DatetimeIndex(dt)
weather_report.reindex(ind)
print(weather_report)