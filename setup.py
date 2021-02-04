from setuptools import setup, find_packages

setup(
    name='Demo Project',
    version='1.0',
    description='',
    author='Carl Schreep',
    author_email='cschreep@gmail.com',
    packages=find_packages(
        where='src',
    ),
    package_dir={"": "src"}
)
