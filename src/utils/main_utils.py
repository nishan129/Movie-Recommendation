from src.exception import ModelException
from src.logger import logging
import yaml
import sys
import numpy as np
import dill
import os

def save_data(filepath: str, obj:object) -> None:
    try:
        logging.info("saving data is start")
        fil = os.makedirs(os.path.join(filepath), exist_ok=True)
        with open(filepath,'rb') as file_obj:
            np.save(file_obj, obj)
    except Exception as e:
        raise ModelException (e,sys)

def save_obj(filepath: str, obj:object) -> None:
    try:
        logging.info("Enter the save_object method of MainUnit class")
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        
        with open(filepath,'wb') as file_obj:
            dill.dump(obj,file_obj)
        
        logging.info("Exited the save_object method and main_unit class")
    except Exception as e:
        raise ModelException(e,sys)
    
    
def load_object(file_path:str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception("file path: {file_path} is not exists")
        
        with open(file_path,'rb') as file_obj:
            
            logging.info("object is loaded")
            return dill.load(file_obj)
    except Exception as e:
        raise ModelException(e,sys)