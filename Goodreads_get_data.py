import pandas as pd
import gdown
import os
import requests
import io


# Downloading the csv file from your GitHub account
# Make sure the url is the raw
# version of the file on GitHub
url = "https://raw.githubusercontent.com/MengtingWan/goodreads/master/gdrive_id.csv"

download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

file_ids = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print(file_ids)

file_id_map = dict(zip(file_ids['name'].values, file_ids['id'].values))


def download_by_name(fname, output=None, quiet=False):
    if fname in file_id_map:
        url = 'https://drive.google.com/uc?id=' + file_id_map[fname]
        gdown.download(url, output=output, quiet=quiet)
    else:
        print('The file', fname, 'can not be found!')


# takes 20+min to download
download_by_name('goodreads_books.json.gz')
# takes 44+min to download
download_by_name('goodreads_interactions.csv')


