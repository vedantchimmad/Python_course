# Variables

---

* Variables are containers to stor data 
* python has no command for declaring the variables
* Variable is created the moment assign a value to it

## Casting
If you want to store the data type that can be done using casting
```python
x = str(3)  # x will be'3'
y = int(3)  # y will be 3
z = float(3) # z will be 3.0
```
## variable names
A variable can be short name(like x and y) or more descriptive name (age,carname etc)
* A variable name must start with later or _ character
* Variable name can't start with number
* A variable name contain only alphanumeric and underscores(A-z,0-9,and _)
* variable names are case-sensitive(age=!AGE)
* Variable name can't be python keywords

## Multi words variable names
* variable name with more than one word is difficult to read hence there are several techniques to make more readable 
  1. Camel case
  
     Each word except first start with capital later
     ```python
     myVariableName="vedant'
     
     print(myVariableName)
     ```
  2. Pascal case
  
     Each word start with capital later
     ```python
     MyVariableName = "Vedant"
     
     print(MyVariableName)
     ```
  3. Snake case
  
     Each word separated by underscore
     ```python
     my_variable_name = "Vedant"
     
     print(my_variable_name)
     ```
## Assign multiple values in a variable
* Many values to multiple variables

  Python allows you to assign values to multiple variable in single line
  ```python
  x,y,z = "apple","orange","mango"
  
  print(x)
  print(y)
  print(z)
  ```
* One value to multiple variable

  Assign same value to multiple variable
  ```python
  x = y = z = "apple"
  
  print(x)
  print(y)
  print(z)
  ```
* Unpack collection

   If you have collection of values in a list,tuple etc.Python allows you to extract values into variables
   ```pthon
   names = ["vedant", "Vrashab", "Basavaraj"]
  
   x,y,z = names
   print(x)
   print(y)
   print(z)
   ```
## type of variable
* Global variables
  
  * Variables that are created outside the function 
  * Variable used both inside and outside function
  ```pthon
  x = "hello welcome"
  
  def myfunc():
     print(x)
  myfunc()
  ```
* Local variables
  * Variable created inside the function
  * Can't be use outside function
  ```python
  x = "hello welcome"
  
  def myfunc():
     x = "hello world!"
     print(x)
  
  myfunc()
  ```
* Global keyword
  * used to make local variable to global variable
  ```python
  def myfunc():
    global x
    x = "welcome"
  
  myfunc()
  
  print(x)
  ```