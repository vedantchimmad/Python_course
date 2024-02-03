# Nested_loops

---
Python programming language allows to use one loop inside another loop.
## Nested For Loop
>Syntax
```python
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```
```python
months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]


for x in months:
  for y in days:
    print(x, y)

print("Good bye!")
```
## Nested While Loop
>Syntax
```python
while expression:
   while expression:
      statement(s)
   statement(s)
```
```python
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i, " is prime")
   i = i + 1

print("Good bye!")
```