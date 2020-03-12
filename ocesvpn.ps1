$ServerAddress = "	oak-creek-energy-wlan-wired-krmnkmczzp.dynamic-m.com"

$ConnectionName = "OCES VPN"

$PresharedKey = "O4kCr33KVPN-2018!"
Get-VpnConnection | Remove-VpnConnection

Add-VpnConnection -Name "$ConnectionName" -ServerAddress "$ServerAddress" -TunnelType L2tp -AllUserConnection -L2tpPsk "$PresharedKey" -AuthenticationMethod Pap -RememberCredential -Force -PassThru -verbose