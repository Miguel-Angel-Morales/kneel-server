import sqlite3
from models.orders import Order
from models.styles import Style
from models.metals import Metals
from models.sizes import Size


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                o.style_id,
                o.size_id,
                o.metal_id,
                o.id,
                st.style AS style_style,
                st.price AS style_price,
                m.metal AS metal_metal,
                m.price AS metal_price,
                si.carets AS size_carets,
                si.price AS size_price
            FROM Orders o
            JOIN Styles st ON o.style_id = st.id
            JOIN Metals m ON o.metal_id = m.id
            JOIN Sizes si ON o.size_id = si.id
        """)

        orders = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['style_id'], row['size_id'],
                          row['metal_id'], row['id'])
            style = Style(row['style_id'], row['style_style'],
                          row['style_price'])
            metal = Metals(row['metal_id'],
                           row['metal_metal'], row['metal_price'])
            size = Size(row['size_id'], row['size_carets'], row['size_price'])
            order.size = size.__dict__
            order.style = style.__dict__
            order.metal = metal.__dict__
            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.style_id,
            o.size_id,
            o.metal_id,
            o.id
        FROM orders o
        WHERE o.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        # Create an Order instance from the current row
        order = Order(data['style_id'], data['size_id'],
                      data['metal_id'], data['id'])
        return order


def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders 
            (style_id, size_id, metal_id)
        VALUES 
            (?, ?, ?)
        """, (new_order['style_id'],
              new_order['size_id'],
              new_order['metal_id']))

        # Get the last inserted row id
        id = db_cursor.lastrowid

        # Set the id property of the new_order object
        new_order['id'] = id

    return new_order


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM orders
            WHERE id = ?
            """, (id,))


def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE orders
        SET style_id = ?, size_id = ?, metal_id = ?
        WHERE id = ?
        """, (new_order.style_id, new_order.size_id, new_order.metal_id, id))
