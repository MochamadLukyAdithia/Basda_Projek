import psycopg2
conn = psycopg2.connect(host="localhost",port="5432",database='Projek_Basda',user="moluka",password="moluka")
cur = conn.cursor()