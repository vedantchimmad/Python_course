## 📦 Python Tuple

---

A **tuple** is a collection which is:

- **Ordered**
- **Immutable** (cannot be changed after creation)
- **Allows duplicate values**

---

### ✅ Creating Tuples

```python
# Simple tuple
t1 = (1, 2, 3)

# Tuple with mixed data types
t2 = ("apple", 3.14, True)

# Tuple without parentheses (still valid)
t3 = 1, 2, 3

# Single-element tuple (note the comma!)
t4 = ("hello",)
```
### 📌 Tuple Indexing
```python
t = ("a", "b", "c", "d")
print(t[0])    # a
print(t[-1])   # d
```
### ✂️ Tuple Slicing
```python
print(t[1:3])   # ('b', 'c')
print(t[:2])    # ('a', 'b')
print(t[::2])   # ('a', 'c')
```

### 🔄 Tuple Operations
```python
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
print(t1 + t2)  # (1, 2, 3, 4)

# Repetition
print(t1 * 2)   # (1, 2, 1, 2)
```
### 📏 Tuple Length
```python
t = (10, 20, 30)
print(len(t))   # 3
```
### ✅ Membership Check
```python
t = (1, 2, 3)
print(2 in t)     # True
print(5 not in t) # True
```
### ♻️ Tuple Packing & Unpacking
```python
# Packing
t = ("red", "green", "blue")

# Unpacking
a, b, c = t
print(a)  # red
print(b)  # green
print(c)  # blue
```
### ⚠️ Tuple Immutability
```python
t = (1, 2, 3)
# t[0] = 10  ❌ This will raise TypeError
```