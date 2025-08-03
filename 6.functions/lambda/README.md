# 🧮 lambda

A `lambda` function is a small anonymous function defined using the `lambda` keyword. It can have any number of arguments, but only one expression.

### 🔹 Syntax

```python
lambda arguments: expression
```

The expression is evaluated and returned automatically.

---

### 🔹 Example 1: Basic lambda

```python
square = lambda x: x * x
print(square(5))  # 25
```

---

### 🔹 Example 2: Lambda with multiple arguments

```python
add = lambda a, b: a + b
print(add(3, 4))  # 7
```

---

### 🔹 Example 3: Using lambda with `map()`

```python
nums = [1, 2, 3, 4]
squared = map(lambda x: x**2, nums)
print(list(squared))  # [1, 4, 9, 16]
```

---

### 🔹 Example 4: Using lambda with `filter()`

```python
nums = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [2, 4]
```

---

### 🔹 Example 5: Using lambda with `sorted()`

```python
data = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [(3, 'a'), (1, 'b'), (2, 'c')]
```