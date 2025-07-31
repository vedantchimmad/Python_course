## ✨ Python String Formatting

---

Python provides several ways to format strings. Here's a breakdown of the **most commonly used techniques**:

---

### 1. `f-strings` (Python 3.6+)
👉 Most modern and readable way to embed expressions.

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.
```
### 2. str.format()
👉 Allows reordering, naming, and formatting of values.
```python
print("My name is {} and I am {} years old.".format("Bob", 30))
# Output: My name is Bob and I am 30 years old.

print("My name is {1} and I am {0} years old.".format(30, "Charlie"))
# Output: My name is Charlie and I am 30 years old.
```

### 3. % Formatting (Old Style)
👉 Similar to C-style formatting, less preferred in new code.
```python
name = "David"
age = 28
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is David and I am 28 years old.
```
### 📌 Formatting Numbers
#### Floating Point Precision
```python
pi = 3.1415926535
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
# Output: Pi rounded to 2 decimal places: 3.14
```
#### Padding and Alignment
```python
print(f"{'Left':<10}{'Center':^10}{'Right':>10}")
# Output: Left      Center      Right
```
### 📌 With Dictionaries & Variables
```python
person = {"name": "Eve", "age": 22}
print("Name: {name}, Age: {age}".format(**person))
# Output: Name: Eve, Age: 22
```
### ✅ Summary Table
| Method         | Syntax Example            | Notes                       |
| -------------- | ------------------------- | --------------------------- |
| f-strings      | `f"Hello {name}"`         | Best practice (Python 3.6+) |
| `.format()`    | `"Hello {}".format(name)` | Flexible and safe           |
| `%` formatting | `"Hello %s" % name`       | Legacy, avoid in new code   |
