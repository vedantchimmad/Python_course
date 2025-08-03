# 🧭 `pass` Statement in Python

---

The `pass` statement is a **null operation**. It is used when a **statement is syntactically required** but **no action is needed**. It acts as a **placeholder** for future code or when a block of code is intentionally left empty.


### ✅ Syntax

```python
pass
```
### ✅ Example 1: In functions
```python
def my_function():
    pass  # Placeholder for future code

print("Function defined.")
```
#### 📤 Output:
```python
Function defined.
```

### ✅ Example 2: In conditionals
```python
x = 10

if x > 5:
    pass  # TODO: handle values greater than 5
else:
    print("x is 5 or less")
```
#### 📤 Output:
```python
(no output)
```

### ✅ Example 3: In loops
```python
for i in range(3):
    pass  # Loop does nothing

print("Loop finished.")
```
#### 📤 Output:
```python
Loop finished.
```
## 🧠 Use Cases
| Use Case                | Description                            |
| ----------------------- | -------------------------------------- |
| Placeholder for logic   | When you're still writing your code.   |
| Avoid syntax errors     | When a block is needed syntactically.  |
| Empty class or function | Useful in stubs, templates, or drafts. |
## ❗ Difference from `continue` and `break`
| Statement  | Action                                 |
| ---------- | -------------------------------------- |
| `pass`     | Does nothing; moves to next statement. |
| `continue` | Skips to next iteration of the loop.   |
| `break`    | Exits the loop entirely.               |
