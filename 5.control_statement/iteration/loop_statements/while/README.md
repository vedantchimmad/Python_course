# 🔄 Python `while` Loop

---

A `while` loop is used to **repeat a block of code as long as a condition is true**.
* ✅ The loop keeps running while the condition is True.
* ❌ It stops when the condition becomes False.
### 🧾 Syntax

```python
while condition:
    # Code block to execute
```
## 🧩  Examples
### ✅ Example 1: Basic While Loop
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
#### 📌 Output:
```python
1
2
3
4
5
```
### ✅ Example 2: Using break
```python
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
```
#### 📌 Output:
```python
1
2
3
4
5
```

### ✅ Example 3: Using continue
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```
#### 📌 Output:
```python
1
2
4
5
```
### ✅ Example 4: Using else with while
```python
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Loop finished!")
```
#### 📌 Output:
```python
1
2
3
Loop finished!
```

### 🧠 Summary Table
| Feature           | Description                          | Example               |
| ----------------- | ------------------------------------ | --------------------- |
| `while`           | Repeats while condition is `True`    | `while x < 10:`       |
| `break`           | Exits the loop early                 | `if x == 5: break`    |
| `continue`        | Skips current iteration              | `if x == 3: continue` |
| `else` with while | Executes when loop finishes normally | `else: print("Done")` |
