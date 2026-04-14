## 🔄 Control Statements in Python

---

By default, program instructions execute **sequentially** (top to bottom). However, **control statements** alter this flow based on conditions or repetitions.


## ✅ Types of Control Flow Statements

---

### 1. 🚦 Decision-Making Statements

These statements evaluate conditions and decide which block of code should run.

#### 🔹 `if`, `elif`, `else`

```python
x = 10
if x > 15:
    print("Greater than 15")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 15")
```
#### 🔹 match-case (Python 3.10+)
Used like a switch-case.
```python
value = 2

match value:
case 1:
print("One")
case 2:
print("Two")
case _:
print("Something else")
```
### 2. 🔁 Iteration Statements (Loops)
These are used to repeat blocks of code multiple times.

#### 🔹 for loop
```python
for i in range(3):
print("Iteration", i)
```
#### 🔹 while loop
```python
count = 0
while count < 3:
print("Count is", count)
count += 1
```
### 🔍 Summary Table
| Category        | Statement            | Description                              |
| --------------- | -------------------- | ---------------------------------------- |
| Decision Making | `if`, `elif`, `else` | Executes code blocks based on conditions |
|                 | `match-case`         | Matches fixed values (like switch-case)  |
| Iteration       | `for`                | Repeats block for a sequence             |
|                 | `while`              | Repeats block while condition is true    |
