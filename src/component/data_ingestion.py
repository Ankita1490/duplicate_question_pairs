import os
import shutil
import zipfile

from logger import logger
from entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        
    def copy_file(self):
        "Copy zip file in the artifact/data_ingestion folder"
        
        if not os.path.exists(self.data_ingestion_config.local_data_file):
           
           shutil.copy(self.data_ingestion_config.source_data,self.data_ingestion_config.local_data_file)
           file_path, file_name = os.path.split(self.data_ingestion_config.local_data_file)
           logger.info(f"{file_name} in copied in {file_path}")
           
    def extract_zip_file(self):
        """Extract zip file into the data directory"""
        unzip_path = self.data_ingestion_config.unzip_dir
        
        if os.path.exists(self.data_ingestion_config.local_data_file):
            try:
                with zipfile.ZipFile(self.data_ingestion_config.local_data_file,'r') as zip_ref:
                    zip_ref.extractall(unzip_path)
                    
                    logger.info(f"The zip file has been extracted in this path {unzip_path}")
            except zipfile.BadZipFile:
                logger.error(f"False to extract {self.data_ingestion_config.local_data_file}: Bad zip file")
            except Exception as e:
                logger.error(f"Error Extracting zip file: {str (e)}")    
                raise e
            
        else:
            logger.info("The source file is missing")
            