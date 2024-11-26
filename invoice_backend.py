import sqlite3

# Connect to the database
def connect():
    conn = sqlite3.connect("invoices.db")
    cur = conn.cursor()
    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS invoice (
            id INTEGER PRIMARY KEY,
            customer_name TEXT,
            item_name TEXT,
            price REAL,
            quantity INTEGER,
            total REAL
        )
    """)
    conn.commit()
    conn.close()

# Insert a new invoice
def insert(customer_name, item_name, price, quantity, total):
    conn = sqlite3.connect("invoices.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO invoice (customer_name, item_name, price, quantity, total) VALUES (?, ?, ?, ?, ?)", 
                (customer_name, item_name, price, quantity, total))
    conn.commit()
    conn.close()

# View all invoices
def view():
    conn = sqlite3.connect("invoices.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM invoice")
    rows = cur.fetchall()
    conn.close()
    return rows

# Delete an invoice by ID
def delete(id):
    conn = sqlite3.connect("invoices.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM invoice WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Update an invoice
def update(id, customer_name, item_name, price, quantity, total):
    conn = sqlite3.connect("invoices.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE invoice
        SET customer_name=?, item_name=?, price=?, quantity=?, total=?
        WHERE id=?
    """, (customer_name, item_name, price, quantity, total, id))
    conn.commit()
    conn.close()

connect()  # Ensure the table is created when the script runs
