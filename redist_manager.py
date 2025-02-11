import os, requests, tempfile, zipfile, platform, shutil
from time import sleep
from tqdm import tqdm
from main import title

vcredist_url = "https://github.com/barankrky/vcredist_installer/raw/refs/heads/master/vcredists.zip"
temp_path = tempfile.gettempdir()
downloaded_zip_path = os.path.join(temp_path, "vcredists.zip")

def download_vcredist():
    response = requests.get(vcredist_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(downloaded_zip_path, "wb") as f, tqdm(
            desc="",
            total=total_size,
            unit='B',
            unit_scale=True,
            ncols=100
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            pbar.update(len(data))
            f.write(data)

def extract_vcredist():
    with zipfile.ZipFile(downloaded_zip_path) as zip_file:
        zip_file.extractall(temp_path)

def get_vcredist():
    print("> Downloading runtime packages...")
    download_vcredist()
    print("> Extracting runtime packages...")
    extract_vcredist()

def clean_up():
    if os.path.exists(downloaded_zip_path):
        os.remove(downloaded_zip_path)
    if os.path.exists(os.path.join(temp_path, "vcredists")):
        shutil.rmtree(os.path.join(temp_path, "vcredists"))  # Kurulum dizinini sil

def install_vcredist_x86():
    os.system("cls")
    print(title)
    print("> Installing runtime packages...\n")
    vcpath = os.path.join(temp_path, "vcredists")
    os.chdir(vcpath)

    print("> Installing vcredist2005_x86.exe...")
    os.system(r'vcredist2005_x86.exe /q:a /c:"msiexec /i vcredist.msi /qn"')

    print("> Installing vcredist2008_x86.exe...")
    os.system(r'vcredist2008_x86.exe /q:a /c:"msiexec /i vcredist.msi /qn"')

    print("> Installing vcredist2010_x86.exe...")
    os.system(r"vcredist2010_x86.exe /q")

    print("> Installing vcredist2012_x86.exe...")
    os.system(r"vcredist2012_x86.exe /install /quiet /norestart")

    print("> Installing vcredist2013_x86.exe...")
    os.system(r"vcredist2013_x86.exe /install /quiet /norestart")

    print("> Installing vcredist2015_2017_2019_2022_x86.exe...")
    os.system(r"vcredist2015_2017_2019_2022_x86.exe /install /quiet /norestart")

    os.system("cls")
    print(title)
    print("> Installation complete. Exiting in 5 seconds...")
    sleep(5)
    
    clean_up()  # Geçici dosyaları sil

    os.system("cls")
    os.system("exit")

def install_vcredist_x64():
    os.system("cls")
    print(title)
    print("> Installing runtime packages...\n")
    vcpath = os.path.join(temp_path, "vcredists")
    os.chdir(vcpath)

    print("> Installing vcredist2005_x86.exe...")
    os.system(r'vcredist2005_x86.exe /q:a /c:"msiexec /i vcredist.msi /qn"')
    print("> Installing vcredist2005_x64.exe...")
    os.system(r'vcredist2005_x64.exe /q:a /c:"msiexec /i vcredist.msi /qn"')

    print("> Installing vcredist2008_x86.exe...")
    os.system(r'vcredist2008_x86.exe /q:a /c:"msiexec /i vcredist.msi /qn"')
    print("> Installing vcredist2008_x64.exe...")
    os.system(r'vcredist2008_x64.exe /q:a /c:"msiexec /i vcredist.msi /qn"')

    print("> Installing vcredist2010_x86.exe...")
    os.system(r"vcredist2010_x86.exe /q")
    print("> Installing vcredist2010_x64.exe...")
    os.system(r"vcredist2010_x64.exe /q")

    print("> Installing vcredist2012_x86.exe...")
    os.system(r"vcredist2012_x86.exe /install /quiet /norestart")
    print("> Installing vcredist2012_x64.exe...")
    os.system(r"vcredist2012_x64.exe /install /quiet /norestart")

    print("> Installing vcredist2013_x86.exe...")
    os.system(r"vcredist2013_x86.exe /install /quiet /norestart")
    print("> Installing vcredist2013_x64.exe...")
    os.system(r"vcredist2013_x64.exe /install /quiet /norestart")

    print("> Installing vcredist2015_2017_2019_2022_x86.exe...")
    os.system(r"vcredist2015_2017_2019_2022_x86.exe /install /quiet /norestart")
    print("> Installing vcredist2015_2017_2019_2022_x64.exe...")
    os.system(r"vcredist2015_2017_2019_2022_x64.exe /install /quiet /norestart")

    os.system("cls")
    print(title)
    print("> Installation complete. Exiting in 5 seconds...")
    sleep(5)
    
    clean_up()  # Geçici dosyaları sil

    os.system("cls")
    os.system("exit")

def start():
    get_vcredist()
    
    if platform.architecture()[0] == '32bit':
        install_vcredist_x86()
    else:
        install_vcredist_x64()
