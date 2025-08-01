# 🔁 Python `if...else` Statement

---

The `if...else` statement is used to execute one block of code **if a condition is true**, and another block **if the condition is false**.


### 🧾 Syntax

```python
if condition:
    # Code block if condition is True
else:
    # Code block if condition is False
```
### ✅ Example
```python
num = 10

if num % 2 == 0:
print("Even number")
else:
print("Odd number")
```
### 🔹 Short Hand If-Else (Ternary Expression)
You can write if...else in a single line for simple conditions:
```python
a = 5
b = 10

print("a is greater") if a > b else print("b is greater")
```

### 📋 Summary Table
| Condition | Executes   |
| --------- | ---------- |
| True      | If block   |
| False     | Else block |
