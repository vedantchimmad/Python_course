from setuptools import setup

setup(
    name='mypackage',
    version='0.1',
    description='A sample Python package',
    author='vedant',
    author_email='vedantchimmad@gmail.com',
    packages=['my_package'],
    install_requires=[
        'numpy',
        'pandas',
    ],
) 