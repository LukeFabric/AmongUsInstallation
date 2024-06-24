$user = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$userSplit = $user.Split("\")
$username = $userSplit[1]
Remove-Item -Recurse -Force -Path C:\Users\"$username"\AppData\LocalLow\Innersloth
if ( [System.IO.File]::Exists('C:\Program Files (x86)\Steam\depotcache\945361_2536144614134451205.manifest') ) {
    Remove-Item -Force -Path 'C:\Program Files (x86)\Steam\depotcache\945361_2536144614134451205.manifest'
}
& 'C:\Program Files (x86)\Steam\steam.exe'