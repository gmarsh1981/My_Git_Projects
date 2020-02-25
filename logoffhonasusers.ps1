#This program will run a query to identify all the sessions that are disconnected
#or over 24 hours old and remove the session
 
Set-ExecutionPolicy Bypass -Force
$session = query USER | select -Skip 1
foreach ($line in $session){
   $line = -split $line
 
 #Get sessions that are disconnected
   
   if($line.Length -eq 7){
        $sessionid = $line[1]
        $sessionState = $line[2]
        if($sessionState -like "Disc"){
            logoff $sessionid 
        }

    # Get Sessionid of sessions that are over 24 hours old

   }elseif($line.Length -eq 8){
        $seesionDate = $line[5]+" "+" "$line[6]+" "+" "$line[7]+" "+" "$line[8]
        [DateTime]$session = $seesionDate
        $AmountofTime = $session - (get-date)
        if($AmountofTime -gt 24){
            $sessionid = $line[1]
            logoff $sessionid
        }
   }
}
