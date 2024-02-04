# Lambda

---
* A lambda function is a small anonymous function.

* A lambda function can take any number of arguments, but can only have one expression.
>Syntax
> 
> lambda arguments : expression
* The expression is executed and the result is returned
```python
x = lambda a : a + 10
print(x(5))
```
* Lambda functions can take any number of arguments.
```python
x = lambda a, b : a * b
print(x(5, 6))
```
### Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```

