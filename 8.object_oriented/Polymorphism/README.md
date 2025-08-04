# 🔄 Polymorphism in Python

---

### 📌 Definition

**Polymorphism** means "many forms". In object-oriented programming, polymorphism allows the same interface (method or operator) to behave differently depending on the object using it.

---

### 🧠 Key Concepts

- **Compile-time Polymorphism** (not natively supported in Python):
    - Achieved via **method overloading**.
    - Python doesn’t support it directly; can be mimicked using default arguments or `multipledispatch`.

- **Run-time Polymorphism** (fully supported in Python):
    - Achieved through **method overriding**.
    - Child class provides a specific implementation of a method already defined in the parent class.

---

### ✅ Example: Polymorphism with Functions and Objects

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def animal_sound(animal):
    animal.speak()

cat = Cat()
dog = Dog()

animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Bark
```
### 🔁 Example: Polymorphism with Inheritance
```python
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.flight()     # Output: Most birds can fly.
obj_sparrow.flight()  # Output: Sparrows can fly.
obj_ostrich.flight()  # Output: Ostriches cannot fly.

```
### 📎 Summary
| Type         | Description                                              |
| ------------ | -------------------------------------------------------- |
| Compile-time | Method overloading (not directly supported in Python)    |
| Run-time     | Method overriding (fully supported in Python)            |
| Key benefit  | Enables generic code to work with different object types |
