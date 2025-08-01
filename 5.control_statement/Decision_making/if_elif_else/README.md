# 🔀 Python `if...elif...else` Statement

---

Used for **multi-way branching**, allowing your program to make decisions based on **multiple conditions**.
* `if`: Checked first.
* `elif`: Checked only if previous conditions are False.
* `else`: Executed if all previous conditions are False.
### 🧾 Syntax

```python
if condition1:
    # Code block 1
elif condition2:
    # Code block 2
elif condition3:
    # Code block 3
else:
    # Default code block
```
### ✅ Example
```python
marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
# 📌 Output - Grade: C
```
### ⚡ Short Hand If-Else
For simple one-liners:
```python
a = 10
b = 20

print("a is greater") if a > b else print("b is greater")
```
📋 Summary Table
| Condition                  | Code Block Executed |
| -------------------------- | ------------------- |
| `if` is True               | Code block 1        |
| `if` False, `elif` is True | Code block 2/3/...  |
| All conditions False       | `else` block        |
