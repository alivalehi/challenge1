import sqlite3
import json
import pandas as pd
conn = sqlite3.connect('sqlite.db')
df = pd.read_sql_query("SELECT * FROM 'exec';", conn)
for values in enumerate(df.rates):
   Dic = json.loads((values[1]))
   print(Dic["1"])
   print(Dic["5"])
   