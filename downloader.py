import pandas as pd
import os
import sys
import shutil
import requests
import pandas as pd

def download_file(url, file_name, folder_name):
    current_path = os.getcwd()
    path = os.path.join(current_path, folder_name, file_name + ".jpg")
    with requests.get(url, verify=False, stream=True) as r:
        r.raw.decode_content=True
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print("successfully downloaded: " + file_name)

def main():
    if len(sys.argv) != 3:
        print("Usage: python downloader.py csv_name name")
    else:
        csv_name = sys.argv[1]
        name = sys.argv[2]
        df = pd.read_csv(csv_name)
        ids_images = pd.Series(df.Image.values, index=df.id).to_dict()
        for id, url in ids_images.items():
            download_file(url, id, name)

if __name__ == "__main__":
    main()