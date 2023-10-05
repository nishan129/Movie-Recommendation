from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirements_list:List[str] = []
    
    return requirements_list
    

setup(
    name= "Movie-Recommendation-System",
    version= '0.0.0.1',
    author= "Nishant Borkar",
    author_email="nishantborkar139@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements(),
)