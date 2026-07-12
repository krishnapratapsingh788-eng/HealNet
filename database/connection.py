import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="healnet",
        user="postgres",
        password="healnet123",
        port="5432"
    )
    return conn