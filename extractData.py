import sqlite3
import pandas as pd
conn = sqlite3.connect('sqlite.db')
df = pd.read_sql_query("SELECT * FROM 'exec';", conn)

