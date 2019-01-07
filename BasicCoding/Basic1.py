l=[1,2,3,4]
l1=[5,6,7,8]
# a=zip(l,l1)
# print(set(a))
# print(list(a))
for a in list(zip(l,l1)):
    # print(a)
    pass

itr=iter(list(zip(l,l1)))
i=0
while True:
 try:
     print(itr.__next__())
 except :
     break
 i+=1



