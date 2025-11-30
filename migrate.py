import sqlite3
import json

def migrate_data():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')
    
    # Load and insert categories
    with open('categories.json', 'r') as f:
        categories = json.load(f)
    
    for category in categories:
        cursor.execute(
            'INSERT OR REPLACE INTO categories (id, name, description) VALUES (?, ?, ?)',
            (category['id'], category['name'], category['description'])
        )
    
    # Load and insert products
    with open('inventory.json', 'r') as f:
        products = json.load(f)
    
    for product in products:
        cursor.execute(
            'INSERT OR REPLACE INTO products (id, name, price, stock, category_id) VALUES (?, ?, ?, ?, ?)',
            (product['id'], product['name'], product['price'], product['stock'], product['category_id'])
        )
    
    conn.commit()
    conn.close()
    print("Migration completed successfully!")

if __name__ == "__main__":
    migrate_data()