# Exception

---
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.

script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.

### Try Except
* The `try` block lets you test a block of code for errors.

* The `except` block lets you handle the error.

* The `else` block lets you execute code when there is no error.

* The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

### Exception Handling
* When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
* These exceptions can be handled using the `try` statement
* Since the try block raises an error, the except block will be executed.
```python
try:
  print(x)
except:
  print("An exception occurred")
```
### Many Exceptions
You can define as many exception blocks as you want, e.g.
```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
### Else
You can use the `else` keyword to define a block of code to be executed if no errors were raised
```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```
### Finally
The `finally` block, if specified, will be executed regardless if the try block raises an error or not.
```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```
### Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
```python
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```
```python
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
```
| Exception	            | Cause of Error                                                                                                              |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| AssertionError        | 	Raised when an `assert` statement fails.                                                                                   |
| AttributeError        | Raised when attribute assignment or reference fails.                                                                        |
| EOFError              | 	Raised when the `input()` function hits end-of-file condition.                                                             |
| FloatingPointError    | Raised when a floating point operation fails.                                                                               |
| GeneratorExit         | 	Raise when a generator's close() method is called.                                                                         |
| ImportError           | 	Raised when the imported module is not found.                                                                              |
| IndexError            | 	Raised when the index of a sequence is out of range.                                                                       |
| KeyError              | 	Raised when a key is not found in a dictionary.                                                                            |
| KeyboardInterrupt     | 	Raised when the user hits the interrupt key (Ctrl+C or Delete).                                                            |
| MemoryError           | 	Raised when an operation runs out of memory.                                                                               |
| NameError             | 	Raised when a variable is not found in local or global scope.                                                              |
| NotImplementedError   | Raised by abstract methods.                                                                                                 |
| OSError               | 	Raised when system operation causes system related error.                                                                  |
| OverflowError	        | Raised when the result of an arithmetic operation is too large to be represented.                                           |
| ReferenceError        | 	Raised when a weak reference proxy is used to access a garbage collected referent.                                         |
| RuntimeError	         | Raised when an error does not fall under any other category.                                                                |
| StopIteration         | 	Raised by next() function to indicate that there is no further item to be returned by iterator.                            |
| SyntaxError           | 	Raised by parser when syntax error is encountered.                                                                         |
| IndentationError      | 	Raised when there is incorrect indentation.                                                                                |
| TabError	             | Raised when indentation consists of inconsistent tabs and spaces.                                                           |
| SystemError           | 	Raised when interpreter detects internal error.                                                                            |
| SystemExit            | 	Raised by sys.exit() function.                                                                                             |
| TypeError	            | Raised when a function or operation is applied to an object of incorrect type.                                              |
| UnboundLocalError     | 	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| UnicodeError          | 	Raised when a Unicode-related encoding or decoding error occurs.                                                           |
| UnicodeEncodeError    | 	Raised when a Unicode-related error occurs during encoding.                                                                |
| UnicodeDecodeError    | 	Raised when a Unicode-related error occurs during decoding.                                                                |
| UnicodeTranslateError | 	Raised when a Unicode-related error occurs during translating.                                                             |
| ValueError            | 	Raised when a function gets an argument of correct type but improper value.                                                |
| ZeroDivisionError     | 	Raised when the second operand of division or modulo operation is zero.                                                    |
### User-Defined Exceptions
create your own exceptions by deriving classes from the standard built-in exceptions.
```python
class MyException(Exception):
   "Invalid marks"
   pass
   
num = 10
try:
   if num <0 or num>100:
      raise MyException
except MyException as e:
   print ("Invalid marks:", num)
else:
   print ("Marks obtained:", num)
```