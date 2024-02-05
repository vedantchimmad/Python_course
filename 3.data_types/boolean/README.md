# Booleans

---
* Booleans represent one of two values: True or False
* When you compare two values, the expression is evaluated and Python returns the Boolean answer
  ```python
  print(10 > 9)
  print(10 == 9)
  print(10 < 9)
  ```
When you run a condition in an if statement, Python returns True or False:
```python
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```
## Values are True
* Any string is True, except empty strings.
* Any number is True, except 0.
* Any list, tuple, set, and dictionary are True, except empty ones.
  ```python
  x = "Hello"
  y = 15

  print(bool(x))
  print(bool(y))
  ```
## Values are False
* In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
  ```python
  a = bool(False)
  b = bool(None)
  c = bool(0)
  d = bool("")
  e = bool(())
  f = bool([])
  g = bool({})
  
  print(a)
  print(b)
  print(c)
  print(d)
  print(e)
  print(f)
  print(g)
  ```
* One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
  ```python
  class myclass():
  def __len__(self):
    return 0

  myobj = myclass()
  print(bool(myobj))
  ```