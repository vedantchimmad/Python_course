# Class and Object

---
Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

### Create a Class
To create a class, use the keyword `class`
```python
class MyClass:
  x = 5
```
### Create Object
Now we can use the class named MyClass to create objects.
```python
p1 = MyClass()
print(p1.x)
```
### The __init__() Function
All classes have a function called __init__(), which is always executed when the class is being initiated.
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Vedant", 25)

print(p1.name)
print(p1.age)
```
>[!NOTE]
> 
> The __init__() function is called automatically every time the class is being used to create a new object.
### The __str__() Function
* The __str__() function controls what should be returned when the class object is represented as a string.
* If the __str__() function is not set, the string representation of the object is returned.
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
```
### Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```
>[!NOTE]
> 
> The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
### The self Parameter
* The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

* It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
```python
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```
### Modify Object Properties
You can modify properties on objects like this
```python
p1.age = 40
```
### Delete Object Properties
You can delete properties on objects by using the del keyword.
```python
del p1.age
```
### Delete Objects
You can delete objects by using the `del` keyword
```python
del p1
```
### The pass Statement
`class` definitions cannot be empty, but if you for some reason have a `class` definition with no content, put in the `pass` statement to avoid getting an error.
```python
class Person:
  pass
```