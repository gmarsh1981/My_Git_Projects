Configuration DSCFileShare {
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

        # xSmbShare Resource
        # Create Share

        xSMBShare CreateShare {
            Ensure = "Present"
            Name = 'TestShare'
            Path = 'C:\Users\gmarsh'
            FullAccess = "gmarsh"
            FolderEnumerationMode = "AccessBased"
            DependsOn = '[File]CreateFolder'
        }
    }

}
DSCFileShare .\DSCCreateShare.ps1 -computerName LAPTOP-VSBJF5A4 
Start-DscConfiguration -ComputerName Laptop-VSBJF5A4 -Path DSCFileShare -Force -wait -Verbose