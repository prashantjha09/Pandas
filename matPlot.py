import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# x=[10,15,20,25]
# y=[10,20,40,80]
#
# x1=[10,11,12,13]
# y1=[10,30,90,270]
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Data to analise\nmathematically")
# # plt.bar(x,y,color="red",label="first_line")
# # plt.bar(x1,y1,color="blue",label="second_line")
# plt.plot(x,y,color="red",label="first_line")
# plt.plot(x1,y1,color="blue",label="second_line")
# plt.legend()
# plt.show()

#
# population_age=[100,10,22,55,63,78,89,97,78,9,56,65,78,45,74,32,123,45,90]
# bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]
# plt.hist(population_age,bins,histtype="bar",rwidth=0.8)#histtype=step or histtype=stepfilled
# plt.xlabel("Age Group")
# plt.ylabel("Number of People ")
# plt.title("Data to analise\nmathematically")
# plt.show()


# x=[11,2,3,4,5,16,7]
# y=[10,11,12,13,4,15,16]
# plt.scatter(x,y,label='skitscat',color=['c'],marker="*",s=100)
# plt.show()

# plt.title("analysis daily data")
# slice=[70,5,13]
# activities=['sleeping','working','playing']
# plt.pie(slice,labels=activities,colors=["r","b","m","k","c"],startangle=90,shadow=True,autopct='%1.1f%%',explode=[0.1,0,0])
# plt.legend()
# plt.show()


data={"x":[11,2,3,4,5,16,7],"y":[10,11,12,13,4,15,16]}
df=pd.DataFrame(data)
# df.to_csv("out1.csv",index=False)
#  print(pd.read_csv("out1.csv"))
x,y=np.loadtxt("out1.csv",delimiter=",",skiprows=1,unpack=True)
plt.bar(x,y,color='red')
plt.show()
plt.plot(x,y,color='b')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Data")
plt.legend()
plt.show()