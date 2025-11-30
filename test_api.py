import sqlite3
from lib import calculate_price
import json

def test_products():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.id, p.name, p.price, p.stock, c.name as category_name
        FROM products p
        JOIN categories c ON p.category_id = c.id
        LIMIT 3
    ''')
    products = [dict(row) for row in cursor.fetchall()]
    conn.close()
    print("GET /api/products (sample):")
    print(json.dumps(products, indent=2))
    return products

def test_order():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    product_id = 101
    quantity = 2
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    
    if product and product['stock'] >= quantity:
        total_price = calculate_price(product_id, quantity, product['price'])
        new_stock = product['stock'] - quantity
        cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (new_stock, product_id))
        conn.commit()
        
        result = {
            "total_price": total_price,
            "product_name": product['name'],
            "quantity": quantity,
            "remaining_stock": new_stock
        }
        print("\nPOST /api/order result:")
        print(json.dumps(result, indent=2))
    
    conn.close()

if __name__ == "__main__":
    test_products()
    test_order()