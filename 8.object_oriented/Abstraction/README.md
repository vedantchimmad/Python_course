# 🧱 Abstraction in Python

---

Abstraction is a fundamental concept in object-oriented programming which is used to **hide irrelevant details** from the user and **show only relevant information**.

### 🚗 Real-life Example

A car has an accelerator, clutch, and brake. We know pressing the accelerator increases speed and using the brake stops the car — but we don't need to know how it works internally.

---

## 🔹 Achieving Abstraction in Python

* Achieved using **abstract classes**.
* Abstract classes can be created using the `abc` (Abstract Base Class) module and the `abstractmethod` decorator.

---

## 🏗️ Abstract Classes

When a method is declared inside a class without implementation, it is known as an **abstract method**.

### 🔸 Abstract Method

* Created using `@abstractmethod` decorator.
* Abstract methods **must be implemented** by any subclass.
* If not implemented, Python will throw an error.

```python
from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
        pass  # empty body
```

---

### 🔸 Concrete Method

* Defined with full implementation in the abstract base class.
* Helps **avoid code duplication** in subclasses.

```python
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = True

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.model}'s engine.")
            self.engine_started = True
        else:
            print("Engine is already running.")
```

---

## 📦 Steps to Create Abstract Class

1. Import `ABC` and `abstractmethod` from `abc` module.
2. Create a base class inheriting from `ABC`.
3. Define abstract and concrete methods.

```python
from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
        pass
```

---

## 🧪 Complete Example

```python
from abc import ABC, abstractmethod

# Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print("speed up ...")

    def break_applied(self):
        print("Car stop")

# Child class 1
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def Sunroof(self):
        print("Not having this feature")

# Child class 2
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def Sunroof(self):
        print("Available")

# Object creation
car1 = Hatchback("Maruti", "Alto", "2022")
car1.printDetails()
car1.accelerate()
```

---

📌 **Note**: Abstract classes cannot be instantiated directly.

```python
car = Car("Brand", "Model", 2023)  # ❌ Raises TypeError
```
