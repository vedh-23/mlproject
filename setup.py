from setuptools import find_packages,setup
from typing import List
H='-e .'
def get_requirements(file_path:str)->List[str]:
  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","") for req in requirements]
    if(H in requirements):
      requirements.remove(H)
    
  return requirements
setup(
  name='mlproject',
  version='0.0.1',
  author='Vedh',
  author_email='vedhvirat@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirement.txt')
)