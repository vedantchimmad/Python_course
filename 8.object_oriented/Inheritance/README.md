# Inheritance

---
Inheritance allows us to define a class that inherits all the methods and properties from another class.
* `Parent` class is the class being inherited from, also called base class.
* `Child` class is the class that inherits from another class, also called derived class.

### Types of Inheritance
* **Single Inheritance**: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

* **Multilevel Inheritance**: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 
* **Hierarchical Inheritance**: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
* **Multiple Inheritance**: Multiple-level inheritance enables one derived class to inherit properties from more than one base class.
### Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class.
```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```
### Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
```python
class Student(Person):
  pass
```
### the __init__() Function
* We want to add the `__init__()` function to the child class (instead of the pass keyword).
* When you add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.
>[!NOTE]
> 
> When you add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.
* To keep the inheritance of the parent's `__init__()` function, add a call to the parent's __init__() function:
```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
```
### Use the super() Function
Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent
```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
```
>[!NOTE]
> 
> By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
### Add Methods
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

```