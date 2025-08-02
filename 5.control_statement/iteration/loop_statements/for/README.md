# 🔁 Python `for` Loop

---

A `for` loop in Python is used to **iterate over a sequence** (like a list, tuple, string, or range). It executes a block of code **once for each item** in the sequence.

### 🧾 Syntax

```python
for variable in sequence:
    # Code block to execute
```
## 🧩  Examples
### ✅ Example 1: Loop through a list
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
print(fruit)
```
#### 📌 Output:
```python
apple
banana
cherry
```
### ✅ Example 2: Loop through a string
```python
for char in "Python":
print(char)
```
#### 📌 Output:
```python
P
y
t
h
o
n
```
### ✅ Example 3: Using range()
```python
for i in range(5):
print(i)
```
#### 📌 Output:
```python
0
1
2
3
4
```
### ✅ Example 4: Using range(start, stop, step)
```python
for i in range(2, 10, 2):
print(i)
```
#### 📌 Output:
```python
2
4
6
8
```
### ✅ Example 5: for with else
```python
for i in range(3):
print("Number:", i)
else:
print("Loop finished!")
```

#### 📌 Output:
```python
Number: 0
Number: 1
Number: 2
Loop finished!
```
## 🧠 Summary Table
| Usage            | Code Example         | Output Example            |
| ---------------- | -------------------- | ------------------------- |
| Loop over list   | `for x in [1, 2]:`   | 1 2                       |
| Loop over string | `for ch in "hi":`    | h i                       |
| Loop with range  | `for i in range(3):` | 0 1 2                     |
| Loop with step   | `range(1, 5, 2)`     | 1 3                       |
| For-else         | see above            | includes "Loop finished!" |
