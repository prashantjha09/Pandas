import pandas as pd
details=[('Bob', 968), ('Jessica', 155), ('Mary', 77), ('John', 578), ('Mel', 973)]
# det=pd.DataFrame(details)
# print(det)
det=pd.DataFrame(details,columns=["Name","point"])
# print(str(det))
with open('panda.txt','w+') as  o:
    o.write(str(det))

