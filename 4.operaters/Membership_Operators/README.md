# Membership operators

---
Membership operators are used to test if a sequence is presented in an object:

| Operator | Name                                                                                                                           | Example                   |
|----------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| in       | Returns True if both variables are the same objectReturns True if a sequence with the specified value is present in the object | x in y                    |
| not in   | Returns True if a sequence with the specified value is not present in the object                                               | x not in y                |

```python
x = ["apple", "banana"]

# returns True because a sequence with the value "banana" is in the list
print("banana" in x)

# returns True because a sequence with the value "pineapple" is not in the list
print("pineapple" not in x)

```