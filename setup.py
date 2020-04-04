"""
iaBot

This is the setup.py file that can be used
to build or install the project.
"""
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="iaBot",
    version="0.0.1",
    author="Satheesh Kumar",
    author_email="satheesh.101097@gmail.com",
    description="A mini framework for building bots using python which can help you in automating your tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/satheesh1997/iaBot",
    packages=["iabot"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7.0",
)
