from config.configuration import ConfigurationManager
from component.data_ingestion import DataIngestion
from logger import logger

STAGE_NAME_01 ="Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        
    def run_data_ingestion(self):
        data_ingestion_config = self.config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config= data_ingestion_config)
        data_ingestion.copy_file()
        data_ingestion.extract_zip_file()
        
    def main(self):
        self.run_data_ingestion()
        
if __name__ == "__main__":
    try:
        logger.info(f"======stage {STAGE_NAME_01} started=======")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f"======stage {STAGE_NAME_01} completed=======")
    except Exception as e:
        raise logger.exception(e)