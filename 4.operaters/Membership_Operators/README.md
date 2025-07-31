## 🔎 Python Membership Operators

---

Membership operators test whether a **value or variable** is **present in a sequence** (such as a string, list, tuple, set, or dictionary).

---

### 📊 Membership Operators Table

| Operator | Description                                | Example             | Result     |
|----------|--------------------------------------------|---------------------|------------|
| `in`     | Returns `True` if a value is present       | `"a" in "apple"`    | `True`     |
| `not in` | Returns `True` if a value is **not** present | `"x" not in "apple"`| `True`     |

---

## ✅ Examples

### 1. `in`
```python
# String
print("a" in "apple")          # True
print("x" in "apple")          # False

# List
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     # True
print("grape" in fruits)      # False

# Dictionary (checks keys)
person = {"name": "John", "age": 30}
print("name" in person)       # True
print("John" in person)       # False
```
### 2. `not in`
```python
# String
print("z" not in "apple")     # True
print("p" not in "apple")     # False

# Tuple
numbers = (1, 2, 3, 4)
print(5 not in numbers)       # True
print(2 not in numbers)       # False

```
### 🧠 Summary
* Use `in` to check if an item exists.
* Use `not in` to verify if it doesn't exist.