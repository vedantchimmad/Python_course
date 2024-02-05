# Strings

---
Strings are surrounded by single quotation or double quotation mark
>Example
> 
> 'hello' is same as "hello"

Assign string to a variable
```python
a = "vedant"
print(a)
```
>[!NOTE]
>
>You can assign multiline string to a variable with three double quotes or three single quotes
## Strings are array
Strings in python are arrays of bytes representing unicode characters

```python
a = "hello world!"
print(a[1])
```
>[!NOTE]
> 
> Single character is simply string with length of 1
### Looping through a string
Since strings are arrays we can loop through character from a string using for loop
```python
a = "banana"

for x in a :
  print(x)
```
#### String length 
To get the length of string use the len() function
```python
a = "vedant"

print(len(a))
```
#### Check string
To check certain phrase or character is present in a string, we can use the keyword "in"
```python
a = "best thing in life is free"

print("free" in a)
```
Check if not in
```python
a = "best thing in life is free"

print("hello" not in a)
```
---
## Slicing
You can return range of characters by using slice syntax

Specify the start and end of the index, separated by colon 
```python
a = "hello, word!"

print(a[2:5])
```
>[!NOTE]
> 
> First character has index zero

### Slice from the start 
By leaving out the start index, the range will start at the first character
```python
a = "hello, world!"

print(a[:5])
```
### Slice to the end
By leaving out the end index, the range will go to the end
```python
a = "hello, world!"

print(a[2:])
```
### Negative indexing
Use negative indexes to start the slice from the end of string
```python
a = "hello, world!"

print(a[-5:-2])
```