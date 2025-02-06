from redist_manager import *
vcpath = os.path.join(temp_path, "vcredists")
print(fr'vcredist2005_x86.exe /q:a /c:"msiexec /i {vcpath}\vcredist.msi /qn"')