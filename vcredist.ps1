$downloadUrl = "https://github.com/barankrky/vcredist_installer/raw/refs/heads/master/vcredist_installer.exe"
$destinationPath = "$env:TEMP\vcredist_installer.exe"
Invoke-WebRequest -Uri $downloadUrl -OutFile $destinationPath

if (Test-Path $destinationPath) {
    Start-Process -NoNewWindow -FilePath $destinationPath
} else {
}
