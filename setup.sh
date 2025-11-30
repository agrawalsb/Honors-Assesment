#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migration
python migrate.py

# Copy nginx config
sudo cp nginx.conf /etc/nginx/sites-available/inventory-api
sudo ln -sf /etc/nginx/sites-available/inventory-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# Setup systemd service
sudo cp inventory-service.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable inventory-service
sudo systemctl start inventory-service

echo "Setup completed! API should be running on http://localhost/api/"