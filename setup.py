from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''

    try:
        with open('requirements.txt', 'r') as f:
            req = f.readlines()
            req = [dependencies.replace('\n', '') \
                    for dependencies in req \
                    if not dependencies == '-e.']

            return req

    except Exception as e:
        print(e)

setup(
    name='NetworkSecurity',
    version='0.0.1',
    description='This is a project of network security',
    author='Muhammad Talha',
    author_email='tackletalha@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)