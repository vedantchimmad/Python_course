# 🔁 `continue` Statement in Python

---

The `continue` statement is used to **skip the current iteration** of a loop and **continue with the next one**. It is helpful when you want to ignore certain conditions during looping but not stop the entire loop.

It can be used with both `for` and `while` loops.

### ✅ Example 1: Using `continue` in a `for` loop

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
#### 📤 Output:
```python
1
2
4
5
```
📝 Explanation: Skips printing 3.

### ✅ Example 2: Using continue in a while loop
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```
#### 📤 Output:
```python
1
2
4
5
```
📝 Explanation: When i == 3, the loop skips the print(i) and continues to the next iteration.

### ✅ Example 3: With continue in nested loops
```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"i={i}, j={j}")
```
#### 📤 Output:
```python
i=1, j=1
i=1, j=3
i=2, j=1
i=2, j=3
i=3, j=1
i=3, j=3
```

📝 Explanation: Skips inner loop when j == 2.

## 📝 Summary Table
| Statement  | Description                        | Loop Continues? |
| ---------- | ---------------------------------- | --------------- |
| `break`    | Exits the loop entirely            | ❌ No            |
| `continue` | Skips current iteration, continues | ✅ Yes           |
