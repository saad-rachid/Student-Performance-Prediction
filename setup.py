from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_pth:str)->List[str]:
    '''
        this function will return th list of requirements 
    '''
    requirements=[]
    with open(file_pth) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name ='MLproject',
version='0.0.1',
author= 'saad',
author_email='r.rachidsaad@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')

)