"""
iaBot

This is the setup.py file that can be used
to build or install the project.
"""
import setuptools


with open("requirements.txt", "r") as fh:
    requirements = fh.read().split("\n")


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="iaBot",
    version="0.0.5",
    author="Satheesh Kumar",
    author_email="satheesh.101097@gmail.com",
    description="A mini framework for building bots using python and can be served using different ways.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/satheesh1997/iaBot",
    packages=["iabot"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7.0",
)
