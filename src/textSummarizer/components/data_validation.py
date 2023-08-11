import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    validation_status = False
                    logger.info(f"Validation failed for {file}")
                    break                   
                else:
                    validation_status = True

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Overall Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e