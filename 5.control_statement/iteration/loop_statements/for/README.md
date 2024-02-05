# For

---
* The for loop in Python has the ability to iterate over the items of any sequence, such as a list, tuple or a string.
* With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
>Syntax
> 
```python
for iterating_var in sequence:
   statements(s)
```
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
## The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
>Syntax
>
> range(start, stop, step)
```python
for x in range(2, 30, 3):
  print(x)
```
## Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```
