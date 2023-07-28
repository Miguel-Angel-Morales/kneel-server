import sqlite3
from models.metals import Metals

def get_all_metals(id=None):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        if id is not None:
            db_cursor.execute("""
            SELECT
                m.metal,
                m.price,
                m.id
            FROM Metals m
            WHERE m.id = ?
            """, (id,))
        else:
            db_cursor.execute("""
            SELECT
                m.metal,
                m.price,
                m.id
            FROM Metals m
            """)

        data = db_cursor.fetchall()

        metals = []
        for row in data:
            metal = Metals(row['metal'], row['price'], row['id'])
            metals.append(metal.__dict__)

        return metals


# Function with a single parameter
def get_single_metal(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.metal,
            m.price,
            m.id
        FROM Metals m
        WHERE m.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        if data:
            metal = Metals(data['metal'], data['price'], data['id'])
            return metal.__dict__
        else:
            return None


def create_metal(metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Metals (metal, price)
        VALUES (?, ?)
        """, (metal['metal'], metal['price']))

        new_id = db_cursor.lastrowid
        metal['id'] = new_id

    return metal


# The rest of the functions remain unchanged.
# ... (delete_metal and update_metal)


def delete_metal(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        # Check if the metal exists before attempting to delete
        db_cursor.execute("""
        SELECT COUNT(*) as count
        FROM Metals
        WHERE id = ?
        """, (id,))

        data = db_cursor.fetchone()

        if data['count'] == 0:
            return False  # Metal with the given ID doesn't exist

        # Execute the DELETE statement to remove the metal
        db_cursor.execute("""
        DELETE FROM Metals
        WHERE id = ?
        """, (id,))

        # Check the row count to see if any row was affected
        row_affected = db_cursor.rowcount

    return row_affected > 0


def update_metal(id, new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
            SET        
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id,))
        
        row_affected = db_cursor.rowcount

    if row_affected == 0:
        return False
    else:
        return True