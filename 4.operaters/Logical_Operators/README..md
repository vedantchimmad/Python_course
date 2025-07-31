## 🔗 Python Logical Operators

---

Logical operators are used to combine conditional statements. They evaluate expressions and return `True` or `False`.

---

### 📊 Logical Operators Table

| Operator | Name  | Description                                               | Example               |
|----------|-------|-----------------------------------------------------------|-----------------------|
| `and`    | AND   | Returns True if **both** statements are true              | `x > 5 and y < 10`    |
| `or`     | OR    | Returns True if **at least one** statement is true        | `x > 5 or y < 10`     |
| `not`    | NOT   | Reverses the result, returns False if the result is true  | `not(x > 5)`          |

---

## ✅ Examples

### 1. `and`
```python
x = 10
y = 20

print(x > 5 and y < 25)   # True (both conditions are True)
print(x > 15 and y < 25)  # False (x > 15 is False)
```
### 2. `or`
```python
x = 10
y = 20

print(x > 15 or y < 25)   # True (y < 25 is True)
print(x > 15 or y > 25)   # False (both are False)
```

### 3. `not`
```python
x = 10

print(not(x > 5))     # False (x > 5 is True → not True = False)
print(not(x < 5))     # True (x < 5 is False → not False = True)
```
### 🧠 Summary
* `and`: True only if both are true.
* `or`: True if any one is true.
* `not`: Reverses the condition.