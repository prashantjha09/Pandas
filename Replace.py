import pandas as pd
import numpy as np
data=pd.read_csv("/Users/praveen/PycharmProjects/csv/weather_data1.csv")
# print(data)
data.replace({"temperature":-99999,"windspeed":-99999,"event":"0"},np.NAN,inplace=True)
print(data)