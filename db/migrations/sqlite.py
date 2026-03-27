import psycopg2

conn = psycopg2.connect(
    dbname="ustudy_work2",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)