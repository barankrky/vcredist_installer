import os, requests, tempfile, zipfile, platform, sys
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

def install_vcredist():
    os.system("cls")
    print(title)
    print("> Installing runtime packages...\n")
    vcpath = os.path.join(temp_path, "vcredists")
    os.chdir(vcpath)
    arch = platform.architecture()[0]
    if arch == "32bit":
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

    elif arch == "64bit":
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
    os.system("cls")
    os.system("exit")


def start():
    get_vcredist()
    install_vcredist()
