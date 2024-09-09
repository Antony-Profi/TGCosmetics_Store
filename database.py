from psycopg2.extras import RealDictCursor
from db.dbContext import getConnection


def getOrderStatus(phone_number):
    conn = getConnection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = """
            SELECT o.id, u.username, p.name as product_name, o.quantity, o.status
            FROM orders o
            JOIN users u ON o.user_id = u.id
            JOIN products p ON o.product_id = p.id
            WHERE u.phone_number = %s
            ORDER BY o.id DESC
            LIMIT 1
            """

            cur.execute(query, (phone_number,))
            result = cur.fetchone()
        return result
    finally:
        conn.close()
