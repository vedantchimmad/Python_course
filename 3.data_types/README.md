# 🧩 Python Data Types

Python has built-in data types that define the **kind of value** a variable holds.

---

### 🔢 1. Numeric Types

| Type   | Description                        | Example         |
|--------|------------------------------------|-----------------|
| int    | Integer numbers                    | `x = 10`        |
| float  | Decimal/real numbers               | `x = 10.5`      |
| complex| Complex numbers                    | `x = 3 + 5j`    |

```python
x = 10         # int
y = 3.14       # float
z = 5 + 2j     # complex
print(type(z)) # Output: <class 'complex'>
```
### 📝 2. Text Type
| Type | Description               | Example       |
| ---- | ------------------------- | ------------- |
| str  | Text/string of characters | `x = "Hello"` |
```python
x = "Python is fun!"
print(type(x))  # Output: <class 'str'>
```
### 📜 3. Sequence Types
| Type  | Description                           | Example         |
| ----- | ------------------------------------- | --------------- |
| list  | Ordered, mutable, allows duplicates   | `x = [1, 2, 3]` |
| tuple | Ordered, immutable, allows duplicates | `x = (1, 2, 3)` |
| range | Immutable sequence of numbers         | `x = range(5)`  |
```python
x = [1, 2, 3]          # list
y = (1, 2, 3)          # tuple
z = range(5)           # range
print(list(z))         # Output: [0, 1, 2, 3, 4]
```
### 🔢 4. Set Types
| Type      | Description              | Example                    |
| --------- | ------------------------ | -------------------------- |
| set       | Unordered, no duplicates | `x = {1, 2, 3}`            |
| frozenset | Immutable set            | `x = frozenset([1, 2, 3])` |
```python
x = {1, 2, 3, 3}           # set
y = frozenset([1, 2, 2])   # frozenset
print(x, y)
```
### 🗂️ 5. Mapping Type
| Type | Description                 | Example                |
| ---- | --------------------------- | ---------------------- |
| dict | Key-value pairs (unordered) | `x = {"name": "John"}` |
```python
person = {"name": "Alice", "age": 25}
print(person["name"])   # Output: Alice
```
### ✅ 6. Boolean Type
| Type | Description       | Example    |
| ---- | ----------------- | ---------- |
| bool | `True` or `False` | `x = True` |
```python
x = 5 > 3
print(x)           # Output: True
```
### ❌ 7. None Type
| Type | Description           | Example    |
| ---- | --------------------- | ---------- |
| None | Represents null/empty | `x = None` |
```python
x = None
print(type(x))     # Output: <class 'NoneType'>
```
## 📋 Summary Table
| Category  | Types               |
| --------- | ------------------- |
| Numeric   | int, float, complex |
| Text      | str                 |
| Sequence  | list, tuple, range  |
| Set       | set, frozenset      |
| Mapping   | dict                |
| Boolean   | bool                |
| None Type | NoneType            |
