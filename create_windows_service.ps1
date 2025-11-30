# Create Windows Service using sc command
$serviceName = "InventoryAPI"
$exePath = "python"
$workingDir = "d:\rbu_honors_assessment-main\rbu_honors_assessment-main"
$args = "-m uvicorn server:app --host 0.0.0.0 --port 8000"

# Create the service
sc.exe create $serviceName binPath= "`"$exePath`" $args" start= auto DisplayName= "Inventory API Service"
sc.exe config $serviceName obj= "LocalSystem"

Write-Host "Service created. Start with: sc start InventoryAPI"
Write-Host "Check status with: sc query InventoryAPI"