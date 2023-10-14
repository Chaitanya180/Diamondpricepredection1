from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # You can implement the function to read and return requirements from a file.
    # For example, to read requirements from a 'requirements.txt' file:
    with open(file_path, 'r') as requirements_file:
        return [line.strip() for line in requirements_file]

setup(
    name='Diamondpredection',
    version='0.0.1',
    author='pwshills',
    author_email='devalraju.chaitanya@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Use a relative path here
    # Other setup options can be added here, like description, classifiers, etc.
)
