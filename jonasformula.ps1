####This function pulls in processor and memory utilization and charts it over time. 
####

function PSPerformanceMonitor {
    param(
        [string]$ComputerName = "Localhost",
        $file = 'C:\Users\gmarsh\desktop\performancemon.csv',
        [DateTime]$currentTime = (get-date),
        [DateTime]$endDate = (get-date).AddHours(24)
    )
   ####Get Total Memory in GB

   $CurrentMemoryBytes = (get-wmiobject -class "win32_physicalmemory" -namespace "root\CIMV2").Capacity 
   foreach($dimm in $CurrentMemoryBytes){
        $totalSize += $dimm
   }
   $totalSizeGB = $totalSize/1073741824

   ####Get Memory and CPU While loop

    while($currentTime -lt $endDate){
        sleep 10
        
        ####Memory Percentage

        $availablememory = Get-Counter -Counter '\Memory\Available MBytes'
        $availablememoryGB = $memory.CounterSamples.CookedValue/1024
        $usedMemoryGB = $totalSizeGB - $availablememoryGB
        [int]$memoryPercentage = $usedMemoryGB/$totalSizeGB*100

        ####CPU Percentage

        $cpuPercentage = (Get-WmiObject win32_processor | select Loadpercentage).Loadpercentage

        ####Create custom object

        $object =  New-Object -TypeName PSObject -Property @{"Time" = (Get-Date).ToString("HH:mm:ss")
                                                             "Memory Percentage" = $memoryPercentage 
                                                              "CPU Percentage" = $cpuPercentage  
        }
        $object
    }

}
PSPerformanceMonitor