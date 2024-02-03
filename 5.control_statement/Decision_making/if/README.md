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
