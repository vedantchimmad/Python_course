# 📦 Creating and Installing User-Defined Packages in Python

---

In Python, user-defined packages help organize your code and can be **shared** or **reused** across projects by installing them using tools like `pip`. Here’s a complete guide on how to create, structure, and install your own packages.

---

## ✅ 1. Create a Python Package

### 📁 Directory Structure

```
my_package/
│
├── my_package/              ← Package source code
│   ├── __init__.py
│   └── greet.py
│
├── setup.py                 ← Configuration for installation
└── README.md                ← Optional documentation
```

---

### ✍️ Sample Code

#### `my_package/greet.py`

```python
def hello(name):
    return f"Hello, {name}!"
```

#### `my_package/__init__.py`

```python
from .greet import hello
```

---

### 🛠️ `setup.py` – Required for pip installation

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    description='A simple greeting package',
    author='Your Name',
    author_email='your.email@example.com',
    keywords=['greeting', 'example', 'custom package'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
```

---

## 📦 2. Build and Install the Package

### 🧰 Step 1: Build the package

```bash
python setup.py sdist
```

This creates a `dist/` folder containing a `.tar.gz` source distribution file.

---

### 📥 Step 2: Install Locally Using pip

```bash
pip install dist/my_package-0.1.tar.gz
```

✔️ Now you can import and use your package anywhere:

```python
from my_package import hello

print(hello("Vedant"))
```

---

## 🚀 Optional: Install Using Editable Mode (for development)

```bash
pip install -e .
```

> This links the source code directory directly, so changes are reflected immediately.

---

## 📤 Optional: Publish to PyPI (Public Installation)

1. Install build and twine:

```bash
pip install build twine
```

2. Build the package:

```bash
python -m build
```

3. Upload to PyPI:

```bash
twine upload dist/*
```

> 🔐 You must have an account on [https://pypi.org](https://pypi.org)

---

## 📘 Summary

| Step | Task                                                   |
| ---- | ------------------------------------------------------ |
| 1.   | Structure your package with `__init__.py`              |
| 2.   | Write `setup.py` with metadata                         |
| 3.   | Use `python setup.py sdist` to build                   |
| 4.   | Use `pip install` to install locally or upload to PyPI |

---
