from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from db.dbContext import getConnection, createUserTableIfNotExists


load_dotenv()

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def web_form():
    conn = getConnection()
    cur = conn.cursor()

    if request.method == "POST":
        username = request.form["username"]
        phone_number = request.form["phone_number"]
        product_id = request.form["product_id"]
        quantity = request.form["quantity"]

        """Проверка, существует ли пользователь"""
        cur.execute("SELECT id FROM users WHERE phone_number = %s", (phone_number,))
        user = cur.fetchone()

        """Если пользователь не существует, добавляем его"""
        if not user:
            cur.execute("INSERT INTO users (username, phone_number) VALUES (%s, %s) RETURNING id", (
                username,
                phone_number
            ))
            user_id = cur.fetchone()[0]
            conn.commit()
        else:
            user_id = user[0]

        """Проверка, существует ли заказ для этого пользователя"""
        cur.execute("SELECT id FROM orders WHERE user_id = %s AND product_id = %s", (user_id, product_id))
        order = cur.fetchone()

        """Если заказ не существует, он создается; если существует — обновляется количество."""
        if not order:
            cur.execute("INSERT INTO orders (user_id, product_id, quantity, status) VALUES (%s, %s, %s, 'Pending')", (
                user_id,
                product_id,
                quantity
            ))
        else:
            cur.execute("UPDATE orders SET quantity = %s WHERE id = %s", (quantity, order[0]))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    """Получение списка продуктов, которые потом передаются в шаблон index.html для отображения на веб-странице."""
    cur.execute("SELECT id, name, price FROM products")
    products = cur.fetchall()
    conn.close()

    return render_template("index.html", products=products)


@app.route("/orders_status", methods=["POST"])
def order_status():
    conn = getConnection()
    cur = conn.cursor()

    phone_number = request.form["phone_number"]

    """Получение заказов пользователя"""
    cur.execute("""
        SELECT o.created_at, p.name, o.quantity. o.status
        FROM orders o
        JOIN users u ON o.user_id = u.id
        JOIN products p ON o.product_id = p.id
        WHERE u.phone_number = %s
    """, (phone_number,))
    orders = cur.fetchall()

    """Формирование ответа"""
    response = ""
    for order in orders:
        response += f"Заказ создан: {order[0]}, Товар: {order[1]}, Количество: {order[2]}, Статус: {order[3]}\n"
    conn.close()

    return response


if __name__ == "__main__":
    createUserTableIfNotExists(getConnection(), app.app_context().g.db_cur)
    app.run(debug=True)
