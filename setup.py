from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name = "processa_imagem",
    version = '0.0.1',
    author="Lucas",
    url = 'https://github.com/tiemi/image-processing-package.git',
    packages=find_packages(),
    install_requires = requirements,
    python_requires = ">=3.6"
)