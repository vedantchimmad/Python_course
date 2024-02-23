# Python

---

## What is software..?
Software is a set of instructions,data or programs used to operate computers and execute specific task

## What is program..?
Program is a sequence of instruction telling a computer what to do

## What is programming..?
Process of creating software is called programming

## What is Python
Python is high level,general-purpose,object oriented, simple,dynamic type programming language

## History
The implementation of Python was started in the December 1989 by Guido Van Rossum at CWI in
Netherland.
* In February 1991, van Rossum published the code (labeled version 0.9.0).
* In 1994, Python 1.0 was released with new features like: lambda, map, filter, and reduce.
* Python 2.0 added new features like: list comprehensions, garbage collection system.
* On December 3, 2008, Python 3.0 (also called "Py3K") was released.

## What can python do
* TO create desktop application
* Web application
* Data science
* Game development
* Machine learning
* AI

## Features of python
* Python works on different platforms
* open source and free
* Python has simple syntax similar to the english language,easy to code and easy to understand
* Python runs on **interpreter system** meaning code can be executed as soon as it is written
* Object-oriented approach
* Highly portable
* Large standard library 
* dynamically-typed

## Python Indentation
* space at the beginning of a code line 
* Python uses indentation to indicate block of code

  >[!NOTE]
  >
  > In other language indentation is just for readability but in python it's important

## Comments in python
 
### Uses
* Comments can be used to explain code
* Used to make code more readable
* Used to prevent when execution

  ### 1.Single line comment
  * Comments start with A #
  ```python
   # this is single line comment
   print("Hello world!")
  ```
  ### 2.Multi line comment
  * Python really doesn't have a syntax for multiline comment
  * To add a multiline need to insert # for each line
  ```python
  '''
  This is multi line comment
  '''
  print("Hello world!")
  ```

  >[!NOTE]
  >
  > Since python will ignore string literals that are not assigned to a variable
## keywords
Reserved words in python Language that can not be used as a variable name, function name, or any other identifier.

Example : and, as, or, false etc
```python
import keyword

print(keyword.kwlist)
```

# User Input

---
* In python we can ask the user for input.

* uses the `input()` method.
```python
username = input("Enter username:")
print("Username is: " + username)
```
* Python stops executing when it comes to the input() function, and continues when the user has given some input.