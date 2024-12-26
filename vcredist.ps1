
Invoke-WebRequest -Uri "https://github.com/barankrky/vcredist_installer/raw/refs/heads/master/vcredist_installer.exe" -OutFile "$env:TEMP\vcredist_installer.exe"
& "$env:TEMP\vcredist_installer.exe"

