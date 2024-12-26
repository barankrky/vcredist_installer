$url = "https://github.com/barankrky/vcredist_installer/raw/refs/heads/master/vcredist_installer.exe"
$path = "$env:TEMP\vcredist_installer.exe"

$wc = New-Object System.Net.WebClient
$wc.DownloadFile($url, $path)

& $destinationPath