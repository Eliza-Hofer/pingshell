# Set the target hosts (replace with the desired IP addresses or hostnames)
$targetHost1 = "192.168.1.1"
$targetHost2 = "10.0.0.2"

# Continuously listen for incoming pings
while ($true) {
    $pingResult1 = Test-Connection -ComputerName $targetHost1 -Count 1 -ErrorAction SilentlyContinue
    $pingResult2 = Test-Connection -ComputerName $targetHost2 -Count 1 -ErrorAction SilentlyContinue

    if ($pingResult1) {
        Write-Host "Pinged from $targetHost1"
        # Add your specific action for targetHost1 here
        
    }
    elseif ($pingResult2) {
        Write-Host "Pinged from $targetHost2"
        # Add your specific action for targetHost2 here
    }

    Start-Sleep -Seconds 5  # Wait for a few seconds before checking again
}
