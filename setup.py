from setuptools import setup, find_packages

with open("README.md") as readme:
    description = readme.readlines()

setup(
    name="kanbanflow",
    version="0.0.0",
    description=description,
    author="Nico Bakomihalis",
    author_email="nicobako@gmail.com",
    packages=find_packages(),
)