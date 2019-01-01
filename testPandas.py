import pandas as pd
import numpy as np
# dic={}
# dic["Prashant"]=[67,34,56]
# dic["shubham"]=[3,345,455]
# dic["Prabhat"]=[123,35,45]
# dic["Index"]=[1,2,3]
# dic=pd.DataFrame(dic)
# dic.columns=["PRASHANT","SHUBHAM","PRABHAT","INDEX"]
# dic.set_index("INDEX",inplace=True)
# dic=dic.sort_values(["PRABHAT","PRASHANT"])
# print(dic)
# dic=dic.tail(2)
# dic=dic.head(2)
# dic.to_csv('out.csv')#Creating CSV file
dcsv=pd.read_csv('out.csv')#Reading CSV file
# print(dcsv)
# s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
# s.to_csv('out1.csv')
# print(s)

# csv_without_header=pd.read_csv("C:\\Users\Prashant Jha\Desktop\csv_file_without_header.csv",skiprows=1,names=["a","b","c"])
# csv_without_header.set_index("a",inplace=True)
# print(csv_without_header)
# print(csv_without_header.colu)



# dicto = {'first_name': ["Jason" , "Molly" , "Tina" , "Jake" ,"Amy"] ,
#          'last name': ["Miller" , "Jacobson" , "." , "Milner" , "Cooze"],
#          'age':[42,52,36,24,73],
#          'pre test score' : [ 4,24,31,"24","16"],
#          'post test score': ["24" ,"94" ,57 ,62 ,70]}
#
# print(dicto)
# data=pd.DataFrame(dicto)
# print(data)
# print(data.sort_values(["age","pre test score"]))
# print(pd.DataFrame(dicto,columns=["first_name","age","kutta"]))
# # data.to_csv("identity.csv")
# readdata=pd.read_csv("identity.csv",index_col=["first_name","last name"])
# print(readdata)
# readskippeddata=pd.read_csv("identity.csv",skiprows=1)
# print(readskippeddata)
# print(data.columns)
# print(data.age)#or we can also write it as print(data["age"])
# print(type(data.age))
# print(type(list(data["age"])))
# print(data.shape)
# print(data.shape[0])#no. of rows
# print((data.shape)[1])#no  of columns
# lst=range(1,5)
# data["Index"]=range(1,data.shape[0]+1)
# data.set_index("Index",inplace=True)
# print(data)
#

# np_array=np.array([1,2,3])
# print(np_array)
# print(np_array+np.array([5,5,5]))
# print(np_array+5)
# print(np_array-5)
# print(np_array*5)
# print(np_array/5)
#
# def sqr(x):
#     return(x**2)
#
# print(sqr(np_array))
#
# a=np.linspace(1,2,100)#it returns 100 values equally spaced including a and b
# print(len(a))

# two_d_array=np.array([[1,2,3],[4,5,6]])
# print(two_d_array)
# for i in range(len(two_d_array)):
#  for j in  two_d_array[i]:
#     print(j,end=" , ")
# print()
# print(two_d_array)
# print(two_d_array.shape)two_d_array.reshape((3,2)))
# print(two_d_array[0,1]) # this is same as writing print(two_d_array[0][1])
# three_d_array=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(three_d_array)

# array1=pd.DataFrame(np.array([[1,2,3,4],[5,6,7,8]]))
# array1["index"]=["p","q"]
# array1.set_index("index",inplace=True)
# array1.columns=["a","b","c","d"]
# print(array1)
# print()
# array2=pd.DataFrame(np.array([[10,11,12,13],[14,15,16,17]]))
# array2["index"]=["r","s"]
# array2.set_index("index",inplace=True)
# array2.columns=["a","b","c","d"]
# print(array2)
# print(array1.append(array2,sort=True))

s1 = pd.DataFrame({"id":[278,421] , "begin":[56,18] , "conditional":["false", "false"] , "discovery":[0,0], "technique":[1,1]})
# s1["index"]=range(s1.shape[0])
# s1.set_index("index",inplace=True)
s2=pd.DataFrame({"id":[278,421],"cocept":["A","B"],"text_book":["xyz","klm"]})
# s=s1.join(s2)
# print(s1)
# print("--------------------------------------------")
# print(s2)
# print("--------------------------------------------")

result = s1.merge(s2,left_on="id",right_on="id")
# print(result)
del result["text_book"]
# print(result)
# print(result.loc[result["begin"].isin([45,18]) | (result["id"]==421)])

import matplotlib.pyplot as plt
# x = np.linspace(0,100,20)
# print(x)
# y = np.sin(x)
# plt.scatter(x, y,color="red")
# plt.title("graph of sin x")
# plt.xlabel("x-axix")
# plt.ylabel("y-axis")
# plt.show()
# plt.plot(x,y)
# plt.show()


# x=np.array([0,1,2,3,4,5])
# y=np.array([0,1,2,3,4,5])
# y=[j for j in np.linspace(-10,11,100)]
# x=np.linspace(-10,11,100)
# plt.plot(x,y,'ro',color="green")
# plt.plot([i**2 for i in np.linspace(-10,11,100)])
# plt.show()
#



