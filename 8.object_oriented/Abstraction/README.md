# Abstraction

---
 which is used to hide irrelevant details from the user and show the details that are relevant to the users. 
 
Example :  A car has an accelerator, clutch, and break we all know that pressing an accelerator will increase the speed of the car and applying the brake can stop the car
*  we can achieve data abstraction by using `abstract classes`
* abstract classes can be created using `abc` (abstract base class) module and `abstractmethod` of abc module

### Abstraction classes
When a method is declared inside the class without its implementation is known as abstract method.

#### abstract method
* To create abstract method and abstract classes we have to import the `“ABC”` and `“abstractmethod”` classes from abc (Abstract Base Class) library.
* Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class.
*  If we do not implement the abstract methods of base class in the child class then our code will give error.
```python
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass
```
#### Concrete Method
*  Concrete methods are the methods defined in an abstract base class with their complete implementation.
* Concrete methods are required to avoid reprication of code in subclasses. 
*  we write the implementation of that method in abstract base class after which we do not need to write implementation of the concrete method again and again in every subclass.
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
#### Create Abstract Base Class and Abstract Method
1. Firstly, we import `ABC` and `abstractmethod` class from abc (Abstract Base Class) library.
2. Create a `BaseClass` that inherits from the ABC class. In Python, when a class inherits from ABC, it indicates that the class is intended to be an abstract base class.
3. Inside BaseClass we declare an abstract method named `“method_1”` by using `“abstractmethod”` decorater. Any subclass derived from BaseClass must implement this method_1 method. We write pass in this method which indicates that there is no code or logic in this method.
```python
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass
```
```python


# Import required modules
from abc import ABC, abstractmethod
 
# Create Abstract base class
class Car(ABC):
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
     
  # Create abstract method      
  @abstractmethod
  def printDetails(self):
    pass
   
  # Create concrete method
  def accelerate(self):
    print("speed up ...")
   
  def break_applied(self):
    print("Car stop")
     
# Create a child class
class Hatchback(Car):
   
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
    print("Not having this feature")
     
# Create a child class
class Suv(Car):
   
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
    print("Available")
 
     
car1 = Hatchback("Maruti", "Alto", "2022");
 
car1.printDetails()
car1.accelerate()
```