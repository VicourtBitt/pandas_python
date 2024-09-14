import mysql.connector as sql
import pandas as pd

db = sql.connect(host= "localhost", database= 'gc2024', user='root', password='vicourt01')

df = pd.read_sql('SELECT * FROM userInfo', db)

print(df)