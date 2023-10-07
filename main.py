from src.constant.training_pipeline import ARTIFACT_DIR
from src.components.data_transformation import DataTransformation
from src.constant.training_pipeline import filepath
from src.entity.config_entity import DataTransformationConfig


if __name__ == '__main__':
    data = DataTransformation(filepath=filepath,data_transformation_config=DataTransformationConfig)
    data.initiate_data_transformation()