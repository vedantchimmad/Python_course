# ✅ Booleans in Python

---

## 🔹 What Are Booleans?
- Booleans represent **one of two values**:
  - `True`
  - `False`

---

## 🔹 Boolean Comparisons

Python returns Boolean values from comparisons:

```python
print(10 > 9)    # True
print(10 == 9)   # False
print(10 < 9)    # False
```
Used in control structures like `if`:
```python
a = 250
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # Output
```
## 🔹 Values That Are Considered `True`
The following values return True when passed to bool():
* Non-empty strings
* Non-zero numbers
* Non-empty sequences or collections (list, tuple, dict, set)
```python
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True
```
## 🔹 Values That Are Considered `False`
The following values evaluate to `False`:
* False
* `None`
* `0`, `0.0`
* `""` (empty string)
* `[]`, `()`, `{}` (empty list, tuple, dict)
* `set()`
```python
a = bool(False)
b = bool(None)
c = bool(0)
d = bool("")
e = bool(())
f = bool([])
g = bool({})

print(a, b, c, d, e, f, g)  # All will be False
```
## 🔹 Custom Object Evaluates to False
You can override the boolean value of an object using `__len__` method:
```python
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  # False
```