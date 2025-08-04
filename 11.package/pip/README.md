# 📦 Python Packages

---

A **package** in Python is a way of organizing related modules into a single directory hierarchy. It allows you to structure your application and reuse code efficiently.

---

## 📁 What is a Package?

A **package** is simply a **directory** containing a special `__init__.py` file and one or more module files.

```plaintext
mypackage/
│
├── __init__.py
├── module1.py
└── module2.py
```

* `__init__.py`: Initializes the package. Can be empty or include package-level variables/functions.

---

## 📦 Creating a Package

1. Create a folder for the package.
2. Add an `__init__.py` file.
3. Add modules (.py files).

📁 **Example Structure**:

```plaintext
mathutils/
│
├── __init__.py
├── add.py
└── subtract.py
```

📄 `add.py`

```python
def add(a, b):
    return a + b
```

📄 `subtract.py`

```python
def subtract(a, b):
    return a - b
```

---

## 🧯 Using a Package

You can import modules from the package using dot notation:

```python
from mathutils import add, subtract

print(add.add(10, 5))         # 15
print(subtract.subtract(10, 3))  # 7
```

---

## 📦 Import Variants

### 1. Import Entire Module

```python
import mypackage.module1
mypackage.module1.function()
```

### 2. Import Specific Function

```python
from mypackage.module1 import function
function()
```

### 3. Import All

```python
from mypackage.module1 import *
```

---

## 📚 Installing External Packages

Use `pip` to install packages from the Python Package Index (PyPI):

```bash
pip install package_name
```

Example:

```bash
pip install requests
```

Then use in code:

```python
import requests
response = requests.get("https://api.example.com")
print(response.status_code)
```

---

## 🔍 Checking Installed Packages

```bash
pip list
```

## 🔄 Updating a Package

```bash
pip install --upgrade package_name
```

## ❌ Uninstalling a Package

```bash
pip uninstall package_name
```

---

✅ Python packages help keep your code modular, organized, and scalable.
