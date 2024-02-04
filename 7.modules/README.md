# Modules

---
### What is a Module?
* Consider a module to be the same as a code library.
* A module is a file containing definition of functions, classes, variables, constants or any other Python object. 

### Create a Module
To create a module just save the code you want in a file with the file extension `.py`.
```python
def greeting(name):
  print("Hello, " + name)
```
### Use a Module
Now we can use the module we just created, by using the import statement.
```python
import mymodule

mymodule.greeting("vedant")
```
>[!NOTE]
> 
> When using a function from a module, use the syntax: module_name.function_name.

### Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
```python
person1 = {
  "name": "Vedant",
  "age": 25,
  "country": "India"
}
```
Import the module named mymodule, and access the person1 dictionary
```python
import mymodule

a = mymodule.person1["age"]
print(a)
```
### Naming a Module
You can name the module file whatever you like, but it must have the file extension `.py`

### Re-naming a Module
You can create an alias when you import a module, by using the `as` keyword
```python
import mymodule as mx

a = mx.person1["age"]
print(a)
```
### Import From Module
You can choose to import only parts from a module, by using the `from` keyword.

The module named mymodule has one function and one dictionary
```python
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "vedant",
  "age": 25,
  "country": "India"
}
```
```python
from mymodule import person1

print (person1["age"])
```
>[!NOTE]
> 
> When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], ~~not mymodule.person1["age"]~~

## Module Attributes
A module is an object of module class, and hence it is characterized by attributes.
* `__file__` returns the physical name of the module.

* `__package__` returns the package to which the module belongs.

* `__doc__` returns the docstring at the top of the module if any

* `__dict__` returns the entire scope of the module

* `__name__` returns the name of the module

```python
import mymodule

print ("__file__ attribute:", mymodule.__file__)
print ("__doc__ attribute:", mymodule.__doc__)
print ("__name__ attribute:", mymodule.__name__)
```
## The __name__Attribute
In an interactive shell, __name__ attribute returns '__main__'
```python
print ("__name__ attribute within a script:", __name__)
```
```python
def sum(x,y):
   return x+y

if __name__ == "__main__":
   print ("sum:",sum(10,20))
```