# 🔚 `break` Statement in Python

---

The `break` statement is used to **exit the loop prematurely**, even if the loop condition is still true.

It can be used with `for` or `while` loops and is often useful when a condition is met and no further iteration is needed.


## ✅ Example 1: Using `break` in a `for` loop

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```
#### 📤 Output:
```python
1
2
3
4
```
### ✅ Example 2: Using `break` in a `while` loop
```python
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
```
#### 📤 Output:
```python
1
2
3
4
5
```
### ✅ Example 3: Breaking out of Nested Loops
```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i={i}, j={j}")
```
#### 📤 Output:
```python
i=1, j=1
i=2, j=1
i=3, j=1
```

### 🧠 Use Case
Use `break` when:

* Searching for an item and want to stop once found.
* Exiting an infinite loop when a condition is met.
* Reducing unnecessary iterations.

### 📝 Summary Table
| Loop Type | Can Use `break` | Stops Execution When |
| --------- | --------------- | -------------------- |
| `for`     | ✅ Yes           | `break` is reached   |
| `while`   | ✅ Yes           | `break` is reached   |
