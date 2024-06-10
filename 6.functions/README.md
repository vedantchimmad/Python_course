# Functions

---
* A function is a block of code which only runs when it is called.
* A function can return data as a result.
* In Python a function is defined using the `def` keyword
* To call a function, use the function name followed by parenthesis.
```python
def my_function():
  print("Hello from a function")

my_function()
```
## Arguments
* Information can be passed into functions as arguments.
* Arguments are specified after the function name, inside the parentheses,separate them with comma.
```python
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```
>[!NOTE]
> 
> * An argument is the value that is sent to the function when it is called.
> * parameter is the variable listed inside the parentheses in the function definition.
## Positional Arguments
* Passing a positional aruguments while calling a function
```python
def passing_number(a, b):
    add=a+b

passing_number(5,6)
```
>[!NOTE]
>
> Always pass positional arguments first while calling a function
## Keyword Arguments
* You can also send arguments with the key = value syntax.
* This way the order of the arguments does not matter.
```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```
## Number of Arguments
* By default, a function must be called with the correct number of arguments.
  ```python
  def my_function(fname, lname):
    print(fname + " " + lname)

  my_function("Emil", "Refsnes")
  ```
* If you try to call the function with 1 or 3 arguments, you will get an error.
## Arbitrary Arguments, *args
* If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```
## Arbitrary Keyword Arguments, **kwargs
* If you do not know how many keyword arguments that will be passed into your function, add two asterisk: `**` before the parameter name in the function definition.
* This way the function will receive a dictionary of arguments, and can access the items accordingly.
```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```
## Default Parameter Value
* If we call the function without argument, it uses the default value.
```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```
## Passing a List as an Argument
* You can send any data types of argument to a function (string, number, list, dictionary etc.).
* if you send a List as an argument, it will still be a List when it reaches the function.
```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```
## Return Values
* To let a function return a value, use the return statement.
```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```
## Positional-Only Arguments
* You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
* To specify that a function can have only positional arguments, add , / after the arguments.
```python
def my_function(x, /):
  print(x)

my_function(3)
```
## Keyword-Only Arguments
* To specify that a function can have only keyword arguments, add *, before the arguments.
```python
def my_function(*, x):
  print(x)

my_function(x = 3)
```
## Recursion
* Recursion is a common mathematical and programming concept. It means that a function calls itself.
```python
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
```
## Closer function
* Returning the inner function to the caller variable is called clouser function
```python
def clouser():
  a = "vedant"
  def hi():
    print(a())
  return hi
b = clouser()
b()
```