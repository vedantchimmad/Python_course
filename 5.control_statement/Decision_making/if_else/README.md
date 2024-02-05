# if-else

---
* The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t.
* if we want to do something else if the condition is false, we can use the else statement with the if statement.
>Syntax
> 
> if (condition):
> 
>Executes this block if condition is true
> 
>else:
> 
>Executes this block if condition is false
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```
## Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
```python
a = 2
b = 330
print("A") if a > b else print("B")
```