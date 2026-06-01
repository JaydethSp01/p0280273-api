import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = psycopg.connect(DATABASE_URL)
else:
    conn = psycopg.connect("dbname=test user=postgres password=secret")

# Function to initialize database (create tables)
def init_db():
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS productos (id SERIAL PRIMARY KEY, nombre VARCHAR(255) NOT NULL)")
        # Add more table creations here
        conn.commit()