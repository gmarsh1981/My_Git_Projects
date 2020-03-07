Configuration DSCFileShareTest {
    param
    (
        [Parameter(mandatory=$True)]
        [string[]]$computerName
    )

    Import-DscResource -ModuleName PsDesiredStateConfiguration
    Import-DscResource -ModuleName xSmbShare
    
    # Target Node
    Node $computerName {

        # File Resource
        # Create folder
        
        File CreateFolder {
            DestinationPath = 'C:\Users\gmarsh\TestShare'
            Type = 'Directory'
            Ensure = 'Present'
        }

    }
}
DSCFileShareTest .\DSCCreateShareTest.ps1 -computerName LAPTOP-VSBJF5A4 
Start-DscConfiguration -ComputerName Laptop-VSBJF5A4 -Path DSCFileShareTest -wait -Verbose