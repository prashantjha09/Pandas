# Here we will be working on the csv file which is a weather report ::
import pandas as pd
weather_data=pd.read_csv("C:\\Users\Prashant Jha\Desktop\weather_data.csv")
# print(weather_data)                                  #Printing complete data
# print(weather_data[["temperature","windspeed"]])     #Printing selected columns
# print(type(weather_data))                            #Print the type of the data
# print(weather_data.shape)                            #Print the shape of the data i.e no of rows and number of columns
# weather_data["index"]=range(1,weather_data.shape[0]+1)
# weather_data.set_index("index",inplace=True)
# print(weather_data)
# print("Maximum temperature is "+str(weather_data["temperature"].max()))             #this will print maximum temperature
# print("Mean temperature is "+str(weather_data["temperature"].mean()))               #this will print mean temperature
# print("Minimum temperature is "+str(weather_data["temperature"].min()))             #this will print mainimum temperature
# print("Std temperature is "+str(weather_data["temperature"].std()))                 #this will print standared deviation
              # describing stats:
# print(weather_data.describe())


# Printing using certain conditions
# print(weather_data[weather_data["temperature"]>30]) # Printing data where temperature is above 30
# print(weather_data[(weather_data["temperature"]>30) & (weather_data["temperature"] <33)])  # This is how we can use and in pandas for boolean data featching
# print(weather_data[(weather_data.temperature>32) | (weather_data.temperature<25)])           # This is how we can use and in pandas for boolean data featching

#Dataframe using Python list of tuple
data=[("jan",23,7),("Feb",24,8),("Mar",30,6),("April",32,8),("May",34,9),("Jun",35,9)]
pd_data=pd.DataFrame(data,columns=["Months","Temperature","WindSpeed"])

pd_data.set_index()
print(pd_data)



