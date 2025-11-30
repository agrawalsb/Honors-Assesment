# Install as Windows Service using NSSM
# Download NSSM first: https://nssm.cc/download

# Install the service
nssm install InventoryAPI "d:\rbu_honors_assessment-main\rbu_honors_assessment-main\start_service.bat"
nssm set InventoryAPI DisplayName "Inventory API Service"
nssm set InventoryAPI Description "FastAPI Inventory Management Service"
nssm start InventoryAPI

Write-Host "Service installed. Check with: Get-Service InventoryAPI"