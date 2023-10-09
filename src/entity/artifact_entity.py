from dataclasses import dataclass

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path : str 
    transformed_data_file_path : str