# Identity operators

---
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


| Operator | Name                                                  | Example    |
|----------|-------------------------------------------------------|------------|
| is       | Returns True if both variables are the same object    | x is y     |
| is not   | Returns True if both variables are not the same object| x is not y |

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns True because z is the same object as x
print(x is z)

# returns False because x is not the same object as y, even if they have the same content
print(x is y)

print(x is not y)

```