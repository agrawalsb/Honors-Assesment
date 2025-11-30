import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

print("=== JOIN Query: Products with Categories ===")
cursor.execute('''
    SELECT p.name, c.name, p.price, p.stock 
    FROM products p 
    JOIN categories c ON p.category_id = c.id 
    LIMIT 5
''')

for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]} | ${row[2]} | Stock: {row[3]}")

conn.close()