# Match-Case Statement

---
A Python match-case statement takes an expression and compares its value to successive patterns given as one or more case blocks.
>Syntax
> 
> match variable_name:
> 
>case 'pattern 1' : statement 1
> 
>case 'pattern 2' : statement 2
> 
>...
> 
>case 'pattern n' : statement n
```python
def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))
```