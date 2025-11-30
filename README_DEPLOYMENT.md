# Deployment Instructions

## Prerequisites
- Ubuntu/Debian Linux or WSL
- Python 3.8+
- Nginx
- Git

## Quick Setup

1. **Clone and setup environment:**
```bash
cd rbu_honors_assessment-main
chmod +x setup.sh
./setup.sh
```

2. **Manual steps if needed:**

### Database Migration
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python migrate.py
```

### Start API Server
```bash
python server.py
```

### Configure Nginx
```bash
sudo cp nginx.conf /etc/nginx/sites-available/inventory-api
sudo ln -sf /etc/nginx/sites-available/inventory-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Setup Background Service
```bash
# Edit inventory-service.service with correct paths
sudo cp inventory-service.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable inventory-service
sudo systemctl start inventory-service
```

### Public Access with ngrok
```bash
# Install ngrok first
ngrok http 80
```

## API Endpoints

- `GET /api/products` - List all products
- `POST /api/order` - Create order with `{"product_id": 1, "quantity": 2}`

## Testing

### Test products endpoint:
```bash
curl http://localhost/api/products
```

### Test order endpoint:
```bash
curl -X POST http://localhost/api/order \
  -H "Content-Type: application/json" \
  -d '{"product_id": 101, "quantity": 2}'
```

### Verify database:
```bash
sqlite3 inventory.db "SELECT p.name, c.name FROM products p JOIN categories c ON p.category_id = c.id LIMIT 5;"
```

## Required Screenshots
1. `db_proof.png` - SQL JOIN query result
2. `logic_proof.png` - POST /api/order response
3. `service_status.png` - systemctl status
4. `browser_proof.png` - Public URL access