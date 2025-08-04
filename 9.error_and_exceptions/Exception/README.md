# 🐍 Errors in Python

---

Errors in Python can be classified into two main categories:

1. **Syntax Errors**
2. **Exceptions (Runtime Errors)**

---

## 🔹 1. Syntax Errors

* These occur when Python parser is unable to understand a line of code.
* Caused by mistakes like missing colons, parentheses, indentation errors, etc.

```python
# ❌ Syntax Error Example
if True
    print("Missing colon")
```

---

## 🔹 2. Exceptions (Runtime Errors)

* These are raised during the execution of the program.
* Can be handled using `try-except` blocks.

### ✅ Common Built-in Exceptions:

| Exception           | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| `ZeroDivisionError` | Raised when a number is divided by zero                                     |
| `TypeError`         | Raised when an operation is applied to an object of inappropriate type      |
| `ValueError`        | Raised when a function receives the correct type but an inappropriate value |
| `IndexError`        | Raised when accessing an invalid index of a list or tuple                   |
| `KeyError`          | Raised when accessing a non-existing key in a dictionary                    |
| `NameError`         | Raised when a variable is not defined                                       |
| `ImportError`       | Raised when an import statement fails                                       |
| `FileNotFoundError` | Raised when a file or directory is not found                                |

---

## 🔹 Example: Handling an Exception

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

---

## 🔹 Using `else` and `finally`

```python
try:
    print("Hello")
except:
    print("An error occurred")
else:
    print("No errors occurred")
finally:
    print("This will always execute")
```

---

## 🔹 Raising Exceptions Manually

```python
x = -1
if x < 0:
    raise ValueError("x should not be negative")
```

---

> 💡 **Tip:** Use `try-except` blocks to handle predictable exceptions gracefully.
