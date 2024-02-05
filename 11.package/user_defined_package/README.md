# Package

---
* Package in Python is a folder that contains various modules as files.
* additionally a special file `__init__.py` file which may be empty but may contain the package list.

### Python wheel
They are designed to make it easier to install and manage Python packages,

he following command is used for building a pure-python wheel from the setup.py of a package
```commandline
python setup.py bdist_wheel
```
This will create a .whl file in the dist directory that can be installed on any platform with a compatible version of Python.

### setup.py
setup.py is a module used to build and distribute Python packages.
```python
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
```
To use the setup.py file in Python, you first need to have the setuptools module installed.
```commandline

pip install setuptools 
```
Once you have setuptools installed, you can use the setup.py file to build and distribute your Python package by running the following command
```commandline
python setup.py sdist bdist_wheel 
```