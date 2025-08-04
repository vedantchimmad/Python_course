# 🔁 Method Overriding

---

### 📌 Definition

**Method Overriding** occurs when a **child class** provides a **specific implementation** of a method that is already defined in its **parent class**.

- The method in the child class **must have the same name, parameters, and return type** as the method in the parent class.
- It allows **runtime polymorphism** in Python.

---

### 🧠 Key Points

- Used to **customize or extend** the behavior of the inherited method.
- Only the method in the **child class** is executed when called through the child class object.
- Python allows overriding using simple redefinition.

---

### 💡 Example: Method Overriding in Python

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()  # Output: Some generic animal sound
dog.sound()     # Output: Bark
cat.sound()     # Output: Meow
```
### 🔎 Accessing Parent Method from Child Class
If you still want to use the parent class method inside the child class, use super():
```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

d = Dog()
d.sound()
# Output:
# Some generic animal sound
# Bark

```
### 📎 Summary
| Feature          | Description                                   |
| ---------------- | --------------------------------------------- |
| Concept          | Redefining parent class method in child class |
| Purpose          | Customize behavior of inherited method        |
| Accessing parent | Use `super()` inside child class              |
| Achieves         | Runtime Polymorphism                          |
