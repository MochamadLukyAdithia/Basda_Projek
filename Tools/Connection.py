import psycopg2
conn = psycopg2.connect(host="localhost",port="5432",dbname='Projek_Basda',user="postgres",password="moluka")
cur = conn.cursor()