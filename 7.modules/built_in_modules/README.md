# 📚 Important Built-in Python Modules

Python provides a wide range of built-in modules that help with various tasks—from math operations to file handling, data manipulation, and more.

---

## 🧮 `math`

Provides mathematical functions.

```python
import math

print(math.sqrt(16))       # 4.0
print(math.pi)             # 3.141592653589793
print(math.factorial(5))   # 120
```

---

## 🎲 `random`

Generates random numbers and selections.

```python
import random

print(random.randint(1, 10))           # Random int between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random item from list
```

---

## 🕒 `datetime`

Works with dates and times.

```python
import datetime

now = datetime.datetime.now()
print(now)  # Current date and time
```

---

## 📂 `os`

Interacts with the operating system.

```python
import os

print(os.getcwd())              # Current working directory
os.mkdir("test_folder")         # Create new folder
```

---

## 🗃️ `sys`

Provides access to system-specific parameters and functions.

```python
import sys

print(sys.version)      # Python version
print(sys.path)         # List of module search paths
```

---

## 📦 `json`

Used to parse JSON and convert Python objects to JSON.

```python
import json

data = {"name": "Vedant", "age": 25}
json_str = json.dumps(data)
print(json_str)  # '{"name": "Vedant", "age": 25}'
```

---

## 📑 `re`

Handles regular expressions.

```python
import re

text = "The rain in Spain"
match = re.search("rain", text)
print(match.group())  # 'rain'
```

---

## 🧪 `statistics`

Performs statistical calculations.

```python
import statistics

print(statistics.mean([1, 2, 3, 4, 5]))  # 3
```

---

## 🔒 `hashlib`

Used for hashing algorithms (MD5, SHA256, etc.)

```python
import hashlib

print(hashlib.md5(b"hello").hexdigest())
```

---

## 📍 `time`

Time-related functions.

```python
import time

print(time.time())       # Current timestamp
time.sleep(1)            # Pause execution for 1 second
```

---

> 🔖 **Note**: These modules are available by default—no need to install them via `pip`.

