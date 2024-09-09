import psycopg2

from os import environ
from dotenv import load_dotenv


load_dotenv()


def getConnection():
    return psycopg2.connect(
        environ["DATABASE_URL"]
    )


def createUserTableIfNotExsits():
    conn = getConnection()
    try:
        with conn.cursor() as curs:
            curs.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(30),
                    phone_number VARCHAR(20) UNIQUE
            )""")

            curs.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(54),
                description TEXT,
                PRICE DECIMAL(10, 2)
            )""")

            curs.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                product_id INTEGER REFERENCES products(id),
                quantity INTEGER,
                status VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")

        conn.commit()
    finally:
        conn.close()
