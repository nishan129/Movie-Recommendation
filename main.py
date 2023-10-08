from src.constant.training_pipeline import ARTIFACT_DIR
from src.components.data_transformation import DataTransformation
from src.constant.training_pipeline import filepath
from src.entity.config_entity import DataTransformationConfig
from src.pipeline.trainingpipeline import TraningPipeline

if __name__ == '__main__':
    trainig = TraningPipeline()
    trainig.run_pipeline()
    
# ab = DataTransformationConfig
# if ab.transformed_object_file_path is True:
#     print("True")
# else:
#     print("Failed")