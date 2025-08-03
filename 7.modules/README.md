# 📦 Python Modules

Modules in Python are files containing Python code (functions, classes, variables) that can be imported and reused in other Python programs.

They help organize code logically and promote reusability.

---

### 🔹 What is a Module?

A **module** is simply a `.py` file that can be imported using the `import` statement.

For example, if you have a file `math_utils.py`, you can import it as a module.

---

### 🔹 Creating a Module

```python
# File: mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

---

### 🔹 Importing a Module

```python
import mymodule

print(mymodule.greet("Vedant"))  # Hello, Vedant!
```

---

### 🔹 Importing Specific Items

```python
from mymodule import greet

print(greet("World"))  # Hello, World!
```

---

### 🔹 Renaming a Module

```python
import mymodule as mm

print(mm.greet("Friend"))  # Hello, Friend!
```

---

### 🔹 Built-in Modules

Python comes with many built-in modules like `math`, `random`, `datetime`.

```python
import math

print(math.sqrt(16))  # 4.0
```

---

### 🔹 Listing All Functions in a Module

```python
import math

print(dir(math))
```

---

### 🔹 Installing External Modules (Using pip)

```bash
pip install requests
```

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

---

### 🔹 Module Attributes

Python modules have some built-in attributes:

| Attribute      | Description                                     |
|----------------|-------------------------------------------------|
| `__name__`     | Name of the module                              |
| `__file__`     | File path of the module                         |
| `__doc__`      | The docstring defined in the module (if any)    |
| `__package__`  | Package name the module belongs to              |

```python
# File: example.py
print("Name:", __name__)
print("File:", __file__)
print("Doc:", __doc__)
print("Package:", __package__)
```

> If a module is run directly, `__name__` will be `"__main__"`.

