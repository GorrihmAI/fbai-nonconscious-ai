from setuptools import setup, find_packages

setup(
    name="fbai",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26.0",
        "scipy>=1.11.0",
    ],
)   