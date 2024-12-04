from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT_="_e."

def get_requirements(file:str)->List[str]:
    requirements=[]
    with open(file,'r') as file_obj:
        r=file_obj.readlines() 
        r=[i.replace('\n',"") for i in r ]


    if HYPEN_E_DOT_ in requirements:
        requirements.remove(HYPEN_E_DOT_)
    
    return requirements




setup(
    name='sensor_fault_detection',
    version='1.1.0',
    author='venkat',
    author_email='saikiranmandapati@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)