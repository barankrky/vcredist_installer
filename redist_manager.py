import os, requests, tempfile, zipfile

vcredist_url = "https://github.com/barankrky/vcredist_installer/raw/refs/heads/master/vcredists.zip"
temp_path = tempfile.gettempdir()
downloaded_zip_path = os.path.join(temp_path, "vcredists.zip")

def download_vcredist(vcredist_url = vcredist_url):
    response = requests.get(vcredist_url)
    with open(downloaded_zip_path, "wb") as f:
        f.write(response.content)

def extract_vcredist():
    with zipfile.ZipFile(downloaded_zip_path) as zip_file:
        zip_file.extractall(temp_path)

def check_vcredist():
    print("Downloading runtime packages...")
    download_vcredist()
    print("Extracting runtime packages...")
    extract_vcredist()