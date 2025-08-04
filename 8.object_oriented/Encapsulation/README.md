# Encapsulation in Python

---

Encapsulation is one of the fundamental concepts in Object-Oriented Programming (OOP).
It is the mechanism of wrapping the data (variables) and code (methods) together as a single unit and restricting access to some of the object's components.

### 🧹 Key Points

* Prevents direct modification of object data.
* Achieved using **private**, **protected**, and **public** access specifiers.
* Improves **security**, **modularity**, and **code maintainability**.

---

## Access Modifiers in Python

| Modifier  | Syntax       | Access Level                     |
| --------- | ------------ | -------------------------------- |
| Public    | `self.var`   | Accessible everywhere            |
| Protected | `self._var`  | Accessible in class & subclasses |
| Private   | `self.__var` | Accessible only in the class     |

---

## 🔓 Public Members

Public members can be accessed from anywhere.

```python
class Person:
    def __init__(self, name):
        self.name = name  # public

p = Person("Vedant")
print(p.name)  # ✅ Accessible
```

---

## 🔐 Private Members

Private members are prefixed with `__` (double underscore) and can only be accessed inside the class.

```python
class Person:
    def __init__(self, name):
        self.__name = name  # private

    def display(self):
        print(f"Name: {self.__name}")

p = Person("Vedant")
p.display()          # ✅ Accessible via method
# print(p.__name)    # ❌ Error: AttributeError
```

> ℹ️ You can still access private members using **name mangling**:

```python
print(p._Person__name)  # Not recommended but possible
```

---

## 🛡️ Protected Members

Protected members are prefixed with `_` (single underscore) and are intended to be accessed only within the class and its subclasses.

```python
class Person:
    def __init__(self, name):
        self._name = name  # protected

class Employee(Person):
    def show(self):
        print(f"Employee name: {self._name}")

e = Employee("Vedant")
e.show()            # ✅ Accessible via subclass
print(e._name)      # ⚠️ Technically accessible but discouraged
```

---

## Why Use Encapsulation?

✅ Protects object integrity
✅ Prevents accidental modification of data
✅ Improves modularity and reusability
✅ Allows validation before data modification

---

## ✅ Example: Encapsulation with Getters and Setters

```python
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(85)
print(s.get_marks())  # 85
```

> Using getters and setters allows validation and control over private data.

---
