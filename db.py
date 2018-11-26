import psycopg2
import psycopg2.extras


conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='azt',
    user='admin',
    password='admin',
    cursor_factory=psycopg2.extras.RealDictConnection)

cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sql = "select * from azt.customer where id = 19"
cursor.execute(sql)
a = cursor.fetchone()
print(a)