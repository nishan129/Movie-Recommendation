from datetime import datetime
import os
from src.constant.training_pipeline import PIPELINE_NAME, ARTIFACT_DIR
from src.constant import training_pipeline
class TrainingPipelineConfig:
    
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name:str = PIPELINE_NAME
        self.artifact_dir:str = os.path.join(ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp
 
class DataTransformationConfig:
           
           def __init__(self,training_pipeline_config:TrainingPipelineConfig):
               
               self.data_transformation_dir:str = os.path.join(training_pipeline_config.artifact_dir,
                                                               training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
               self.data_transformed_object_dir: str = os.path.join(
                   self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                   training_pipeline.PREPROCSSING_OBJECT_FILE_NAME)
