from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="anime-recommender-Dogu",
    version="0.1",
    author="Doguser",
    packages=find_packages(),
    install_requires = requirements,
)