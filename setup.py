from setuptools import setup, find_packages

setup(
    name="nocatscan",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "nocatscan=nocatscan.main:main"
        ]
    }
)