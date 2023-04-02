import pandas as pd
import glob
from urllib.request import urlretrieve
import opendatasets as od
import os
import zipfile
import io



def extract_data():
    url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/ebc3f9c2-2f80-4405-bf4f-5fb309581485/resource/d83a5249-fb07-4c38-9145-9e12a32ce1d4/download/pcard-expenses.zip"
    od.download(url, './data1')
    zip_file = zipfile.ZipFile('./data1/pcard-expenses.zip')
    csv_file_names = [name for name in zip_file.namelist() if name.endswith('.xlsx')]
    dfs = []
    for name in csv_file_names:
        csv_file = zip_file.read(name)
        df = pd.read_excel(io.BytesIO(csv_file))
        dfs.append(df)
    zip_file.close()
    final_df = pd.concat(dfs, ignore_index=True)
    print(final_df.shape)







if __name__ == '__main__':
    extract_data()

