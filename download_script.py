import os
import sys
import shutil
import requests
import pandas as pd

def read_links(filename):
    df = pd.read_csv(filename)

def download_file(url, folder_name):
    local_filename = url.split('/')[-1]
    path = os.path.join("/{}/{}".format(folder_name, local_filename))
    with requests.get(url, stream=True) as r:
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

def main():
    args = sys.argv[1]