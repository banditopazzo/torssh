from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='torssh',                                  # This is the name of your PyPI-package.
    version='0.1',                                   # Update the version number for new releases
    author="banditopazzo",
    author_email="banditopazzo@gmail.com",
    install_requires=[
        "stem >= 1.7.1",
    ],
    description="A simple utility to use SSH and SCP over Tor",
    url="https://github.com/banditopazzo/torssh",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points = {
        'console_scripts': ['torssh=torssh.cli:ssh','torscp=torssh.cli:scp'],
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)