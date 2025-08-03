# 🧩 Functions in Python

---

A **function** is a block of organized, reusable code that performs a specific task.

### ✅ Defining and Calling a Function
* 📘 **Definition**: The `def` keyword is used to declare a function in Python.
```python
def my_function():
    print("Hello from a function")

my_function()
```
### 📥 Arguments/Parameters
📘 **Definition**: Arguments are inputs you provide to a function when calling it. Parameters are the names used in the function definition.
* Functions can take arguments (also called parameters).
* Arguments are specified after the function name inside the parentheses.

```python
def greet(name):
    print(name + " Refsnes")

greet("Emil")
greet("Tobias")
greet("Linus")

```
### 📌 Positional Arguments
📘 **Definition**: These must be provided in the correct order as expected by the function.
* The order of values matters.
```python
def passing_number(a, b):
    print(a + b)

passing_number(5, 6)

```

📌 Keyword Arguments
📘 **Definition**: Keyword arguments use the form key=value, allowing flexibility in order.
* Use key=value syntax; order doesn’t matter.
```python
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

```
### ⚖️ Argument Count
📘 **Definition**: Functions must be called with the exact number of arguments unless default or variable arguments are used.
```python
def full_name(fname, lname):
    print(fname + " " + lname)

full_name("Emil", "Refsnes")

```
### 🌟 Arbitrary Arguments `*args`
📘 Definition: Allows a function to accept any number of positional arguments as a tuple.
* Used when number of positional arguments is unknown.
```python
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

```
🌟 Arbitrary Keyword Arguments `**kwargs`
📘 **Definition**: Allows a function to accept any number of keyword arguments as a dictionary
* Used when number of keyword arguments is unknown.
```python
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

```
### 🛡️ Default Argument Values
📘 **Definition**: Assigns a default value to a parameter, used if no argument is passed.
```python
def my_function(country="Norway"):
    print("I am from " + country)

my_function("India")
my_function()

```
📚 List as Argument
📘 **Definition**: You can pass lists (or other data types) to functions to work on collections of data.
```python
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
```
### 🔁 Return Values
📘 **Definition**: The `return` statement sends a value back to the caller and ends the function.
```python
def my_function(x):
    return 5 * x

print(my_function(3))
```
### 🎯 Positional-only Arguments
📘 **Definition**: Enforces that arguments must be passed by position only (introduced in Python 3.8+).

```python
def my_function(x, /):
    print(x)

my_function(3)

```
### 🎯 Keyword-only Arguments
📘 **Definition**: Enforces that arguments must be passed using keywords only.
```python
def my_function(*, x):
    print(x)

my_function(x=3)

```
### ♻️ Recursion
📘 **Definition**: When a function calls itself directly or indirectly, it’s known as recursion.
```python
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

```
### 🧵 Closure Function
📘 **Definition**: A closure is an inner function that remembers and has access to variables in the local scope where it was created, even after the outer function has finished executing.
```python
def clouser():
    a = "vedant"
    def hi():
        print(a)
    return hi

b = clouser()
b()

```
### 🎀 Decorator Function
📘 **Definition**: A decorator is a function that modifies the behavior of another function without changing its source code.
```python
def decorator(fun):
    def wrapper(msz):
        print("*" * 10)
        fun(msz)
        print("*" * 5)
    return wrapper

def display(msz):
    print(msz)

decorated = decorator(display)
decorated("hello")
```