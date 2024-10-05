import pandas as pd
#Read csv file and skip first rows and add header as A,B,C,D,E
# stock_data=pd.read_csv("C:\\Users\Prashant Jha\Desktop\stock_data.csv",skiprows=1,names=["A","B","C","D","E"])
#This will add index to the stocvk_data
# stock_data["index"]=range(1,stock_data.shape[0]+1)
# stock_data.set_index("index",inplace=True)
# print(stock_data)

#If we want to print only 3 rows then
# stock_data=stock_data.tail(2)
# print(stock_data)


#cleaning data
stock_data=pd.read_csv("C:\\Users\Prashant Jha\Desktop\stock_data.csv")
print(stock_data)

#now from avove result result we find that few data is invalid so we need to make changes
stock_data=pd.read_csv("C:\\Users\Prashant Jha\Desktop\stock_data.csv",skiprows=1,names=["Company","eps","revenue","price","people"],na_values={"revenue":["not availabe",-1,"n.a."],"eps":["not availabe","n.a."],"people":["not availabe","n.a."]})
stock_data.set_index("Company",inplace=True)
print(stock_data)
# Writing csv files
stock_data.to_csv("new_stock.csv")
#writing select rows in the csv files
# stock_data=stock_data.head(3)
stock_data=stock_data.tail(3)
stock_data.to_csv("new1_stock.csv",header=False)


