import logging
import psycopg2

from os import environ
from dotenv import load_dotenv


load_dotenv()


def getConnection():
    try:
        return psycopg2.connect(
            host=environ["LOCALHOST"],
            port=environ["DATABASE_PORT"],
            dbname=environ["DATABASE_NAME"],
            user=environ["USER"],
            password=environ["PASSWORD"],
        )
    except psycopg2.Error as e:
        logging.error(f"Error connecting to the database: {e}")
        raise e


def createUserTableIfNotExists(conn, cur):
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
            cur.execute(
                "INSERT INTO products (name, description, price) VALUES ('Product 1', 'Description 1', 10.99), ('Product 2', 'Description 2', 20.99) ON CONFLICT DO NOTHING")

        conn.commit()
    except psycopg2.Error as e:
        logging.error(f"Error creating tables: {e}")
        raise e
    finally:
        conn.close()
