# 🔁 Nested `for` and `while` Loops in Python

---

In Python, **nested loops** are loops inside other loops. These are useful when you need to iterate over multi-dimensional data like matrices or perform repeated actions within each iteration of an outer loop.

## 📌 Nested `for` Loop

### ✅ Example: Multiplication Table

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
```
#### 📤 Output:
```python
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
```
## 📌 Nested while Loop
### ✅ Example: Print Matrix
```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"{i},{j}", end='  ')
        j += 1
    print()
    i += 1
```
#### 📤 Output:
```python
1,1  1,2  1,3  
2,1  2,2  2,3  
3,1  3,2  3,3 
```
 
## 📌 Mixed for inside while
```python
i = 1
while i <= 2:
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    i += 1
```
#### 📤 Output:
```python
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
```

#### 📌 Mixed while inside for
```python
for i in range(1, 3):
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
```
#### 📤 Output:
```python
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
```
## 🧠 Summary Table
| Loop Type              | Description                                   |
| ---------------------- | --------------------------------------------- |
| `for` inside `for`     | Good for 2D structures like grids/lists       |
| `while` inside `while` | Good when condition-based nesting is needed   |
| `for` inside `while`   | Useful when the outer loop is condition-based |
| `while` inside `for`   | Combines fixed and condition-based loops      |
