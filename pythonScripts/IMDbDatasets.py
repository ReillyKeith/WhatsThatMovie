"""
This python script will be used to download the latest movies from IMDb
Author: Keith Reilly
Date: 12/07/2021
"""
import urllib.request
import gzip


def get_ds_filenames(data):
    """
    This function will return all
    the datasets listed in IMDb.
    Names can be found in config file
    :param data:
    :return:
    """
    datasets = []
    for value in data['Datasets']:
        datasets.append(data['Datasets'][f'{value}'])

    return datasets


def download_ds_files(imdb_url, filenames):
    """
    This function will download the datasets
    :param imdb_url:
    :param filenames:
    :return:
    """

    for file in filenames:
        filename = str(file).split('.tsv')[0]
        out_file = f'datasets/{filename}.txt'

        url = f'{imdb_url}{file}'
        print(f"Downloading: {url}")

        # Download files
        try:
            # Read the file inside the .gz archive located at url
            with urllib.request.urlopen(url) as response:

                with gzip.GzipFile(fileobj=response) as uncompressed:
                    file_content = uncompressed.read()

            # write to file in binary mode 'wb'
            with open(out_file, 'wb') as f:
                f.write(file_content)
                f.close()
                print(f"Downloading Complete: datasets/{filename}.txt")


        except Exception as e:
            print(e)
            return 1

def convert_datasets():
    """
    This function will convert the txt file
    into sql file which can be used to search for data
    :return:
    """