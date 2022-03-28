
import os
# import shutil, glob

# from pathlib import Path
# from datetime import date
# from zipfile import ZipFile
# import csv
# import tempfile


# Create a directory at the `path` passed as an argument
def create_directory_if_not_exists(path):
    """
    Create a new directory if it doesn't exists
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

# Save the file obtained to the specified directory

def save_new_scraped_data(source_path, df):
    """
    Save new raw data from the source
    """
    # create path
    create_directory_if_not_exists(source_path)

    # Save dataframe to CSV format
    df.to_csv(source_path, index=False)