import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import opendatasets as od
import shutil
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            dir= self.config.unzip_dir
            dataset = f"{self.config.source_URL}"
            # print(dataset)
            od.download(dataset)
            shutil.move('chest-xray-pneumonia', dir)
            logger.info(f"Download Successful!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        """
        
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)