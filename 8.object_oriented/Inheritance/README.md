# 🧬 Inheritance in Python

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and simplifies code maintenance.

---

## 🔑 Key Concepts

| Term             | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| **Parent Class** | The class being inherited from (also called base or superclass)        |
| **Child Class**  | The class that inherits from another class (also called derived class) |

---

## 🛠 Syntax

```python
class Parent:
    # parent class code

class Child(Parent):
    # child class code
```

---

## ✅ Example

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # Inherited from Animal
d.bark()    # Defined in Dog
```

---

## 🯩 Types of Inheritance

### 1. Single Inheritance

One child inherits from one parent.

```python
class Parent:
    def func1(self):
        print("Function in Parent")

class Child(Parent):
    def func2(self):
        print("Function in Child")

c = Child()
c.func1()
c.func2()
```

---

### 2. Multilevel Inheritance

A class inherits from a child class which itself inherits from another parent class.

```python
class Grandparent:
    def func1(self):
        print("Grandparent")

class Parent(Grandparent):
    def func2(self):
        print("Parent")

class Child(Parent):
    def func3(self):
        print("Child")

c = Child()
c.func1()
c.func2()
c.func3()
```

---

### 3. Multiple Inheritance

A child inherits from more than one parent class.

```python
class Father:
    def house(self):
        print("House from Father")

class Mother:
    def jewelry(self):
        print("Jewelry from Mother")

class Child(Father, Mother):
    pass

c = Child()
c.house()
c.jewelry()
```

---

### 4. Hierarchical Inheritance

Multiple child classes inherit from a single parent class.

```python
class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def child1_method(self):
        print("Child1")

class Child2(Parent):
    def child2_method(self):
        print("Child2")

c1 = Child1()
c2 = Child2()
c1.show()
c2.show()
```

---

### 5. Hybrid Inheritance

Combination of two or more types of inheritance.

```python
class A:
    def func1(self):
        print("A")

class B(A):
    def func2(self):
        print("B")

class C:
    def func3(self):
        print("C")

class D(B, C):
    def func4(self):
        print("D")

d = D()
d.func1()
d.func2()
d.func3()
d.func4()
```

---

## 🧐 Method Overriding

When a child class redefines a method from the parent class.

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()
```

---

## 📌 Notes

* Use `super()` to call methods from the parent class inside the child.
* Helps in **code reusability** and **readability**.
* Ensures **extensibility** and **modularity** in OOP.
