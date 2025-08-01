# 🔍 Python `if` Statement

---

The `if` statement evaluates a condition and executes a block of code **only if** the condition is `True`.
* ✅ If the condition is True, the indented block runs.
* ❌ If the condition is False, it skips the block.


### 🧾 Syntax

```python
if condition:
    # statement(s)
```
#### ✅ Basic Example
```python
discount = 0
amount = 1200

if amount > 1000:
   discount = amount * 10 / 100

print("amount =", amount - discount)
```
#### ⚡ Short Hand If
For simple one-line conditions:
```python
a = 10
b = 5
if a > b: print("a is greater than b")
```
### 🧠 Logical Operators in if
#### 🔗 and
Executes block only if both conditions are true.
```python
a = 200
b = 33
c = 500
if a > b and c > a:
print("Both conditions are True")
```
#### 🔗 or
Executes block if at least one condition is true.
```python
a = 200
b = 33
c = 500
if a > b or a > c:
print("At least one of the conditions is True")
```
#### 🔁 not
Reverses the result of the condition.
```python
a = 33
b = 200
if not a > b:
print("a is NOT greater than b")
```

### 📋 Summary Table
| Operator | Meaning                       | Example            | Result              |
| -------- | ----------------------------- | ------------------ | ------------------- |
| `if`     | Condition check               | `if x > 5:`        | Executes if `x` > 5 |
| `and`    | Both conditions must be True  | `x > 5 and x < 10` | True if both        |
| `or`     | Either condition must be True | `x > 5 or x < 3`   | True if any         |
| `not`    | Inverts the condition         | `not(x > 5)`       | True if False       |
