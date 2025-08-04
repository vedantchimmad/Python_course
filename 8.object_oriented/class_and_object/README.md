# 🧱 Python: Class and Object

---

## 🧾 What is a Class?

* A **class** is a blueprint for creating objects.
* It defines attributes (variables) and behaviors (methods).
* Logical entity — **does not occupy memory** on its own.

### 📌 Syntax

```python
class MyClass:
    x = 5
```

---

## 🧍 What is an Object?

* An **object** is an instance of a class.
* Physical entity — **occupies memory**.
* Multiple objects can be created from one class.

### 📌 Create an Object

```python
p1 = MyClass()
print(p1.x)
```

---

## 🔧 The `__init__()` Method (Constructor)

* Automatically called when an object is created.
* Used to initialize object properties.
* Does **not return** any value.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Vedant", 25)
print(p1.name)
print(p1.age)
```

> 🧠 `__init__()` runs automatically when an object is instantiated.

---

## 📜 The `__str__()` Method

* Controls the **string representation** of the object.
* If not defined, default memory address is returned.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("John", 36)
print(p1)
```

---

## 🧩 Object Methods

* Methods are functions defined inside a class.
* Use `self` to access instance attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}!")

p1 = Person("John", 36)
p1.greet()
```

---

## 🔁 The `self` Parameter

* Refers to the **current instance** of the class.
* Can be named anything, but `self` is the convention.

```python
class Person:
    def __init__(instance, name, age):
        instance.name = name
        instance.age = age

    def greet(obj):
        print(f"Hi, I'm {obj.name}.")

p1 = Person("Alice", 28)
p1.greet()
```

---

## 🔧 Modify & Delete Properties

### 📝 Modify Property

```python
p1.age = 40
```

### ❌ Delete Property

```python
del p1.age
```

### 🗑️ Delete Object

```python
del p1
```

---

## ⛔ The `pass` Statement

* Classes cannot be empty; use `pass` as a placeholder.

```python
class Dummy:
    pass
```

---

# ⚙️ Methods in Python

## 1️⃣ Instance Methods

* Called **on objects**.
* Can access and modify object state.

```python
class MyClass:
    def display(self, name):
        print(name)

obj = MyClass()
obj.display("Vedant")
```

## 2️⃣ Static Methods

* Marked with `@staticmethod`.
* Cannot access `self` or `cls`.
* Called **using class name**.

```python
class Utility:
    @staticmethod
    def add(a, b):
        print(a + b)

Utility.add(10, 20)
```

> ⚠️ If called using an object, static methods require all arguments to be passed manually.

---

# 🧮 Class Variables vs Local vs Global

```python
# Global variables
a, b = 15, 25

class MyClass:
    # Class variables
    a, b = 10, 20

    def add(self, a, b):  # Local variables
        print("Local:", a + b)
        print("Class:", self.a + self.b)
        print("Global:", globals()['a'] + globals()['b'])

obj = MyClass()
obj.add(100, 200)
```

---

🟩 **Summary**

| Term            | Description                           |
| --------------- | ------------------------------------- |
| Class           | Blueprint for creating objects        |
| Object          | Instance of a class                   |
| `__init__`      | Constructor; initializes object state |
| `__str__`       | String representation of an object    |
| Instance Method | Operates on object (`self`)           |
| Static Method   | No access to object or class          |
| Class Variable  | Shared across all instances           |
| `self`          | Refers to the instance of the class   |

---
