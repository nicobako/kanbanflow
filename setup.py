from setuptools import setup, find_packages

with open("README.md") as readme:
    description = readme.readlines()

install_requires = ["pydantic"]

setup(
    name="kanbanflow",
    version="0.0.0",
    description=description,
    author="Nico Bakomihalis",
    author_email="nicobako@gmail.com",
    packages=find_packages(),
    install_requires=install_requires,
    url="https://nicobako.github.io/kanbanflow/",
)
