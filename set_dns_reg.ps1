$adapter = Get-NetAdapter
$x = 0
for($x -eq 0; $x -lt $adapter.Length; $x++){
    if($adapter[$x].ifDesc -match "Intel" -and $adapter[$x].Status -eq 'Up'){
        $index = $adapter[$x].ifIndex
        Set-DnsClientServerAddress -InterfaceIndex $index -ServerAddresses ("132.239.201.2","169.228.38.100")
    }  
}  


