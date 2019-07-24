from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tor_ssh',                                  # This is the name of your PyPI-package.
    version='0.1',                                   # Update the version number for new releases
    author="banditopazzo",
    author_email="banditopazzo@gmail.com",
    description="Access SSH servers over Tor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)