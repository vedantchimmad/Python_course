# Pip

---
### What is PIP?
PIP is a package manager for Python packages, or modules if you like.
### What is a Package?
A package contains all the files you need for a module.

A package contains all the files you need for a module.
### Download a Package
Downloading a package is very easy.
```commandline
pip install camelcase
```
### Using a Package
Import the "camelcase" package into your project.
```python
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```
### Remove a Package
use the uninstall command to remove a package.
```commandline
pip uninstall camelcase
```
### List Packages
Use the list command to list all the packages installed on your system.
```commandline
pip list
```