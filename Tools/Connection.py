import psycopg2
# conn = psycopg2.connect(host="localhost",port="5432",dbname='Projek_Basda',user="postgres",password="moluka")
conn = psycopg2.connect(database='Projek_Basda', user='postgres', password='tiarahmadina', host='localhost', port=5432)
cur = conn.cursor()