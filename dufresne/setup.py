from setuptools import find_packages, setup

setup(
    name="dufresne",
    version="0.1.1",
    packages=find_packages(".", exclude=["tests", "scripts"]),
)
