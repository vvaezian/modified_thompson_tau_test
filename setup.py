from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="modified-thompson-tau-test",
    version="0.1.3",
    author="Vahid Vaezian",
    author_email="vahid.vaezian@gmail.com",
    description="Implementation of Modified Thompson Tau Test in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vvaezian/modified_thompson_tau_test",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
