.\wget.exe "https://drive.usercontent.google.com/download?id=1m5NFFeDbGEkdMSBuFJhBK_OpWx13kxfu&export=download&authuser=0" -O 945361_2536144614134451205.manifest
$user = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$userSplit = $user.Split("\")
$username = $userSplit[1]
Remove-Item -Recurse -Force -Path C:\Users\"$username"\AppData\LocalLow\Innersloth
Remove-Item -Recurse -Force -Path 'C:\Program Files (x86)\Steam\steamapps\common\Among Us'
Remove-Item -Force -Path 'C:\Program Files (x86)\Steam\depotcache\945361_5073468987524498627.manifest'
if ( [System.IO.File]::Exists('C:\Program Files (x86)\Steam\depotcache\945361_2536144614134451205.manifest') ) {
    Remove-Item -Force -Path 'C:\Program Files (x86)\Steam\depotcache\945361_2536144614134451205.manifest'
}
& '.\steamcmd\steamcmd.exe'
Write-Output 