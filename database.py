import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="fastapi_db",
    user="postgres",
    password="postgresql@2026"
)

cursor = conn.cursor()
