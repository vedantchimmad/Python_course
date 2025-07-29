# 📘 Python Variables

---
## 🎯 What is a Variable?
A **variable** is a container for storing data values.

In Python, variables are **created automatically** when you assign a value.
* Python is dynamically typed
### 🛠️ Syntax

```python
variable_name = value
```
#### ✅ Examples
```python
x = 5
name = "Alice"
price = 99.99
is_active = True
```
---
## 🔄 Python Type Casting (Type Conversion)

### 🎯 What is Casting?
**Type casting** (or type conversion) means converting a variable from one data type to another.

In Python, you can **manually convert** (cast) between types using built-in functions.

### 🧪 Common Casting Functions

| Function   | Converts To      | Example                     |
|------------|------------------|-----------------------------|
| `int()`    | Integer           | `int("5") → 5`              |
| `float()`  | Float             | `float("3.14") → 3.14`      |
| `str()`    | String            | `str(100) → "100"`          |
| `bool()`   | Boolean           | `bool(1) → True`            |

---

### 📦 Examples

#### ✅ Convert string to integer
```python
x = "123"
y = int(x)
print(y + 1)  # 124
```
---
## 🧠 Python Memory Address

### 🎯 What is a Memory Address?
Every object in Python is stored in memory. A **memory address** is the location in memory where the object is stored.

### 🧰 Function: `id()`

Python provides a built-in function:

```python
id(object)
# 🔹 It returns the unique identifier of the object (its memory address in CPython implementation).
```
### 📌 Important Notes:
* `id()` is unique and constant for an object during its lifetime.
* For immutable objects (like integers, strings), Python may reuse memory addresses for optimization (called interning).
* For mutable objects (like lists or dictionaries), new objects will have new addresses even if content is same.
### 🧪 Example
#### 1. immutable
```python
x = 10
y = x

print("ID of x:", id(x))
print("ID of y:", id(y))  # Same as x since both refer to same object
```
#### 2. Immutable
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # e.g., 23232344
print(id(b))  # different from a
```
---

## 🏷️ Variable Names

### ✅ What is a Variable Name?
A **variable name** is an identifier used to refer to a value stored in memory. It allows us to access and manipulate data in a Python program.

### 📜 Rules for Naming Variables in Python

| Rule # | Description |
|--------|-------------|
| 1️⃣ | Must start with a **letter** (a–z, A–Z) or an **underscore** (_) |
| 2️⃣ | The rest of the name can include **letters**, **numbers** (0–9), or **underscores** |
| 3️⃣ | Cannot be a **Python keyword** (like `if`, `else`, `while`, etc.) |
| 4️⃣ | Python is **case-sensitive** (`Name`, `name`, and `NAME` are different) |

### ✅ Valid Variable Names

```python
name = "Alice"
_age = 25
total_amount1 = 100.50
```

## 🔤 Multi-Word Variable Names in Python

In Python, **multi-word variable names** help make your code more readable and descriptive. There are several naming conventions to follow based on your coding style or project guidelines.

### ✅ Common Naming Conventions

#### 1. snake_case ✅ (Most common in Python)
* Uses lowercase letters
* Words separated by underscores
* Preferred in Python community (PEP 8 standard)
```python
first_name = "Alice"
total_price = 150.75
user_profile_picture_url = "http://..."
```
#### 2. camelCase ❌ (Common in JavaScript, not Pythonic)
```python
firstName = "Bob"
totalPrice = 99.99
```
* First word starts lowercase
* Subsequent words are capitalized
* Not preferred in Python
#### 3. PascalCase ❌ (Used for Class Names in Python)
* Each word starts with a capital letter
* Used only for class names by convention
```python
FirstName = "Charlie"
TotalPrice = 120.00
```
### 📌 Summary Table
| Convention   | Example            | Valid in Python? | Recommended?    |
| ------------ | ------------------ | ---------------- | --------------- |
| `snake_case` | `total_amount_due` | ✅ Yes            | ✅ Yes           |
| `camelCase`  | `totalAmountDue`   | ✅ Yes            | ❌ No            |
| `PascalCase` | `TotalAmountDue`   | ✅ Yes            | ❌ No (for vars) |
| `kebab-case` | `total-amount-due` | ❌ No             | ❌ No            |

## 📦 Assigning Multiple Values to Variables in Python

Python allows assigning **multiple values** to one or more variables in a single line. This improves code clarity and reduces repetition.

### ✅ Assign Multiple Values to Multiple Variables
* Assigns values 10 → x, 20 → y, 30 → z
* Number of variables must match number of values
```python
x, y, z = 10, 20, 30
print(x)  # 10
print(y)  # 20
print(z)  # 30
```
### ✅ Assign Same Value to Multiple Variables
* All variables `a`, `b`, `c` reference the same value
```python
a = b = c = 100
print(a, b, c)  # 100 100 100
```
### ✅ Unpacking a Collection (Tuple/List)
* This is called unpacking
* Works with tuples, lists, or any iterable
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry
```
### ✅ Use Asterisk * for Variable-Length Unpacking
* `*b` captures the middle items as a list
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```
### 🧪 Summary
| Syntax                       | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| `a, b, c = 1, 2, 3`          | Assign multiple values to multiple vars |
| `a = b = c = 100`            | Assign same value to multiple vars      |
| `a, b, c = [1, 2, 3]`        | Unpack list or tuple                    |
| `a, *b, c = [1, 2, 3, 4, 5]` | Extended unpacking with `*`             |

---
## 🧠 Types of Variables in Python

Python allows variables to be categorized based on **scope and lifetime**.

### 🌍 1. Global Variables

- Defined **outside of functions**.
- Can be **accessed anywhere** in the code (inside and outside of functions).

```python
x = "hello welcome"  # Global variable

def myfunc():
    print(x)         # Accessing global variable

myfunc()
```
### 🔒 2. Local Variables
- Defined inside a function.
- Accessible only within that function.
- Overrides any global variable of the same name within the function scope.
```python
x = "hello welcome"  # Global variable

def myfunc():
    x = "hello world!"  # Local variable
    print(x)

myfunc()  # Output: hello world!
```
### 🧱 3. Class Variables
- Defined inside a class but outside all methods.
- Shared by all instances of the class.
- Accessed using `self` or `ClassName.variable.`
```python
# Global variables
i, j = 15, 25

class MyClass:
    # Class variables
    a, b = 10, 20

    def add(self, x, y):
        # x, y → Local variables
        print("Local sum:", x + y)

        # Class variables
        print("Class sum:", self.a + self.b)

        # Global variables
        print("Global sum:", i + j)

mc = MyClass()
mc.add(100, 200)
```
### 🔑 Global Keyword
- Used to modify a global variable from within a function.
- Without `global`, any assignment inside a function creates a local variable.
```python
def myfunc():
    global x
    x = "welcome"  # Declares x as global

myfunc()
print(x)  # Output: welcome
```
### 🧾 Summary
| Scope  | Defined In       | Accessible In               |
| ------ | ---------------- | --------------------------- |
| Global | Outside function | Entire file                 |
| Local  | Inside function  | Only inside that function   |
| Class  | Inside class     | Through instances or `self` |