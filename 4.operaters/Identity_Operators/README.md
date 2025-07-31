## 🆔 Python Identity Operators

---

Identity operators are used to compare the **memory locations** of two objects, i.e., whether two variables point to the **same object** in memory.

---

### 📊 Identity Operators Table

| Operator | Name     | Description                                      | Example                |
|----------|----------|--------------------------------------------------|------------------------|
| `is`     | is       | Returns True if both variables reference the same object | `a is b`              |
| `is not` | is not   | Returns True if variables reference different objects | `a is not b`          |

---

## ✅ Examples

### 1. `is`
```python
a = [1, 2, 3]
b = a
print(a is b)       # True (same memory reference)

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)       # False (different memory references)
```
### 2. is not
```python
print(a is not x)   # True (a and x do not point to the same object)
```
---
### 🔎 Notes
* `is` compares object identity.
* Use `==` to compare values instead of memory addresses.
```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)    # True (values are the same)
print(x is y)    # False (different objects in memory)
```
