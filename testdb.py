import psycopg2

conn = psycopg2.connect(database='postgres',user='postgres',password='yisheng',host='192.168.23.180',port='5432')
print(conn)