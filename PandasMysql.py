import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost/djangoproject')
df = pd.read_sql_table('auth_user',engine)
df = pd.read_sql_table('auth_user',engine,columns=["id","date_joined"])
df = pd.read_sql_query("select id,date_joined from auth_user",engine)
print(df)
df.rename(columns={
    'x': 'name',
    'y': 'phone_number'
}, inplace=True)
df.to_sql(
    name='auth_user', # database table name
    con=engine,
    if_exists='replace',#it can be fail,append and repalace depending on the condition
    index=False
)
# df.to_csv("my.csv")