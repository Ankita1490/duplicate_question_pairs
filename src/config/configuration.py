from distutils.command.config import config
import os
from pathlib import Path
from constants import CONFIG_FILE_PATH
from utils.common import read_yaml, create_directories
from entity.config_entity import DataIngestionConfig, DataProcessingConfig


class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH ):
        self.config = read_yaml(config_file_path)
        self.is_exists = os.path.exists(self.config.artifacts)
        if not self.is_exists:
            create_directories([self.config.artifacts])
            
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config = self.config.data_ingestion
        is_exists = os.path.exists(data_ingestion_config.root_dir)
        if not is_exists:
            create_directories([data_ingestion_config.root_dir])
            
        data_ingestion_config =DataIngestionConfig(
            root_dir= data_ingestion_config.root_dir,
            source_data= data_ingestion_config.source_data,
            local_data_file= data_ingestion_config.local_data_file,
            unzip_dir = data_ingestion_config.unzip_dir
        )
        
        return data_ingestion_config
        
