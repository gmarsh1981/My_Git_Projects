$folderPermissions = Get-ChildItem '\\labs.ludwigsd.org\zhou\' -Directory -Recurse -ErrorAction SilentlyContinue | Get-Acl 
Write-Host "Completed recurse scan"

foreach($folderpermission in $folderPermissions){
    $path = $folderPermission.Path
    $users = $folderPermission.Access      
    foreach($user in $users){
        $username = $user.IdentityReference
        $userString = $username.ToString()
        $adUser1 = $userString.Split('\')[0]
        $adUser2 = $userString.Split('\')[1]
        if($adUser1 -eq "LUDWIGSD" -and $adUser2 -ne 'Domain Admins' -and $adUser2 -ne 'Zhou Group'  -and $adUser2 -ne 'Administrator'){
            $userInfo = Get-ADUser -Identity $aduser2
            if($userInfo.Enabled -eq $False){
                $userInfo.Name + "             " + $path  | Out-File C:\Users\gmarsh\Desktop\disabledUsersZhou.txt -Append
            }
        }
       
    }
}

