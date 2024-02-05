# If

---
The if statement contains a logical expression using which data is compared and a decision is made based on the result of the comparison.
>Syntax
>
>if expression:
> 
> statement(s)
* If the boolean expression evaluates to TRUE, then the block of statement(s) inside the if statement is executed.
* If boolean expression evaluates to FALSE, then the first set of code after the end of the if statement(s) is executed.
```python
discount = 0
amount = 1200

# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100

print("amount = ", amount - discount)
```
## Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.
```python
if a > b: print("a is greater than b")
```
## And
The and keyword is a logical operator, and is used to combine conditional statements
```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```
## or
The or keyword is a logical operator, and is used to combine conditional statements.
```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```
## Not
The not keyword is a logical operator, and is used to reverse the result of the conditional statement
```python
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```
