import requests
import json

base_url = "http://localhost:8000"

def test_root():
    try:
        response = requests.get(f"{base_url}/")
        print("GET /:")
        print(response.json())
        return True
    except Exception as e:
        print(f"Root endpoint failed: {e}")
        return False

def test_products():
    try:
        response = requests.get(f"{base_url}/api/products")
        print("\nGET /api/products:")
        print(json.dumps(response.json()[:2], indent=2))
        return True
    except Exception as e:
        print(f"Products endpoint failed: {e}")
        return False

def test_order():
    try:
        order_data = {"product_id": 102, "quantity": 1}
        response = requests.post(f"{base_url}/api/order", json=order_data)
        print("\nPOST /api/order:")
        print(json.dumps(response.json(), indent=2))
        return True
    except Exception as e:
        print(f"Order endpoint failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing API endpoints...")
    if test_root():
        test_products()
        test_order()
    else:
        print("Server not running. Start with: python run_server.py")