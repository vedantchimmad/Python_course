# Errors in Python

---

In Python, errors are broadly classified into the following three types:

## 1. Syntax Errors 💡

* Occur when Python's syntax rules are violated.
* Detected during compilation (before execution).
* Prevent the code from running.

> Example:

```python
# Missing closing parenthesis
print("Hello"
```

**Error Output:**

```plaintext
SyntaxError: unexpected EOF while parsing
```

---

## 2. Logical Errors 🧠

* The code runs without throwing an error, but the output is incorrect.
* Often caused by flawed logic or incorrect assumptions.
* Harder to detect because they don’t crash the program.

> Example:

```python
# Incorrect logic for average
def average(a, b):
    return a + b / 2  # wrong logic: should use (a + b) / 2

print(average(10, 20))  # Expected 15, but returns 20
```

---

## 3. Runtime Errors ⚠️ (Exceptions)

* Errors that occur during execution.
* These are called **exceptions** in Python.
* Can be handled using `try` and `except` blocks.

> Example:

```python
a = 10
b = 0
print(a / b)
```

**Error Output:**

```plaintext
ZeroDivisionError: division by zero
```

> Example with Exception Handling:

```python
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

> ✅ **Tip**: Use `try-except` to handle unexpected runtime situations gracefully without crashing your program.
