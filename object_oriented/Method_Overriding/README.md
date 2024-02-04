# Method overriding

---
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.
```python
 
# Defining parent class 
class Parent(): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
          
    # Parent's show method 
    def show(self): 
        print(self.value) 
          
# Defining child class 
class Child(Parent): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"
          
    # Child's show method 
    def show(self): 
        print(self.value) 
          
          
# Driver's code 
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show() 
```
### Using supper()
```python
class Parent(): 
      
    def show(self): 
        print("Inside Parent") 
          
class Child(Parent): 
      
    def show(self): 
          
        # Calling the parent's class 
        # method 
        super().show() 
        print("Inside Child") 
          
# Driver's code 
obj = Child() 
obj.show() 
```