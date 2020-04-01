#THis is just a test to make sure that this works
Configuration startServiceBlue {
    param(
        [Parameter(mandatory=$true)]
        [string]$computerName
    )

    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node $computerName{
        
        Service bluetooth {
            
            Name = 'BTAGService'
            Ensure = 'Present'
            StartupType = 'Automatic'
            State = 'Running'       
        }
    }
}

startServiceBlue -computerName LAPTOP-VSBJF5A4
Start-DscConfiguration -ComputerName LAPTOP-VSBJF5A4 -path startServiceBlue -Force -Wait -Verbose
test-DscConfiguration -Path 'C:\Users\gmarsh\Documents\PowerShell\Scripts\startServiceBlue' -ComputerName LAPTOP-VSBJF5A4