# 🔢 Python Numeric Data Types

Python has 3 primary numeric types:

| Type     | Description                      | Example       |
|----------|----------------------------------|---------------|
| int      | Integer (whole numbers)          | `x = 10`      |
| float    | Floating-point (decimals)        | `x = 10.5`    |
| complex  | Complex numbers (real + imag)    | `x = 3 + 5j`  |

---

### ✅ int (Integer)
Used to represent whole numbers (positive or negative) without decimals.

```python
a = 5
b = -100
c = 0
print(type(a))  # <class 'int'>
```
### ✅ float (Floating Point)
Used for decimal or fractional values.
```python
a = 3.14
b = -0.001
c = 5.0     # Still float
print(type(b))  # <class 'float'>
```
### ✅ complex (Complex Numbers)
Represents numbers in the form a + bj, where a is real and b is imaginary.
```python
a = 2 + 3j
b = complex(5, -2)
print(a.real)    # 2.0
print(a.imag)    # 3.0
print(type(a))   # <class 'complex'>
```
---
## 🧠 Type Conversion Examples
```python
x = 10        # int
y = float(x)  # convert to float
z = complex(x)  # convert to complex

print(y)  # 10.0
print(z)  # (10+0j)
```
## 🧮 Built-in Numeric Functions
| Function     | Description               | Example               |
| ------------ | ------------------------- | --------------------- |
| `abs(x)`     | Absolute value            | `abs(-7) → 7`         |
| `pow(x, y)`  | x to the power y          | `pow(2, 3) → 8`       |
| `round(x)`   | Round to nearest integer  | `round(2.6) → 3`      |
| `int(x)`     | Convert to integer        | `int(4.9) → 4`        |
| `float(x)`   | Convert to float          | `float(4) → 4.0`      |
| `complex(x)` | Convert to complex number | `complex(3) → (3+0j)` |
