from src.entity.config_entity import DataTransformationConfig,TrainingPipelineConfig
from src.components.data_transformation import DataTransformation
from src.exception import ModelException
from src.constant.training_pipeline import filepath
from src.logger import logging
import sys
from src.entity.artifact_entity import DataTransformationArtifact

class TraningPipeline:
    def __init__(self):
        try:
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise ModelException(e,sys)
        
    def start_data_transformation(self, filepath: filepath):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(filepath=filepath,data_transformation_config=data_transformation_config)
            
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise ModelException(e,sys)   
        
    def run_pipeline(self):
        try:
            data_transformation_artifact = self.start_data_transformation(filepath=filepath)
            return data_transformation_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
        