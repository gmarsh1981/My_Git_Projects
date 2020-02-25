$csv = Get-Content -Path C:\Python\Projects\FolderSizeLookup\usernames.csv
$usernames = $csv.Split(',')

$folder = Get-Content C:\Python\Projects\FolderSizeLookup\filepath.txt
$path = Get-ChildItem $folder -Recurse

Add-Content -Path C:\Python\Projects\FolderSizeLookup\Foldersize.csv -Value "Username, Foldersize"


foreach($username in $usernames){ 
    $size = 0
    if($username -ne ''){
        foreach($file in $path){
            $f = Get-Acl $file.FullName
            if($f.Owner -eq $username){
                $size = $size + [float]$file.Length             
            }        
        }
        $totalsize = [float]$size / 1000000000
        Add-Content -Path C:\Python\Projects\FolderSizeLookup\Foldersize.csv -Value "$username, $totalsize" 
    }
}

