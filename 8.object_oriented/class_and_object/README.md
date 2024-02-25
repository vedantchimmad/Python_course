# Class and Object

---
* A Class is a "blueprint" for creating objects.
* Class contains collection of variables(attributes) & methods(behavior)
* Class is a Logical entity
* Class Does not occupy space in the memory

### Create a Class
To create a class, use the keyword `class`
```python
class MyClass:
  x = 5
```
### Create Object
* Now we can use the class named MyClass to create objects.
* object is an instance of class
* Object is a Physical entity
* Occupy certain amount space in the memory
* For one class, we can create multiple objects.

```python
p1 = MyClass()
print(p1.x)
```
### The __init__() Function
* All classes have a function called __init__(), which is always executed when the class is being initiated.
* `__init__()` is called as constructor
* constructor will not return any value
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
## Methods
* Functions are created inside a class
### Types of methods
1. Instance Methods
2. Static Methods

### 1.Instance Methods
* Methods are called only through object
```python
class MyClass:
    def myfun(self):
        pass
    def display(self,name):
        print(name)

mc1=MyClass()
mc1.myfun()
mc1.display("Vedant")
```
### 2.Static Methods
* Methods are called directly using class
```python
class MyClass:
    def m1(self):
        print("this is instance method...")
    @staticmethod
    def m2(self,num):
        print(self,num)

mc=MyClass()
mc.m1()
#calling Static method through object required additional arguments
mc.m2(50,200) 

MyClass.m2(10,20)
```
## Class Variable
* Variable accessed within the class is called as class Variable
* Access class variable using class instance
```python
 # global variables
a,b=15,25  
class MyClass:
    # class variables
    a,b=10,20  
    def add(self,a,b):
        # local varaibles
        print(a+b)
        # class variables
        print(self.a+self.b)
        # global variables
        print(globals()['a']+globals()['b'])  

mc=MyClass()
mc.add(100,200)
```