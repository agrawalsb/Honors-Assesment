# Test Nginx proxy
Write-Host "Testing Nginx proxy..."
Invoke-WebRequest -Uri "http://localhost/api/products" | Select-Object StatusCode, Content

Write-Host "`nTesting direct API..."
Invoke-WebRequest -Uri "http://localhost:8000/api/products" | Select-Object StatusCode, Content