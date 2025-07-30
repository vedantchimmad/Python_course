## 🧵 Python String Methods

---

Python offers a variety of built-in methods to manipulate and analyze strings.

### 1. `capitalize()`
👉 Converts the first character to uppercase.
```python
text = "hello world"
print(text.capitalize())  # Hello world
```
### 2. casefold()
👉 Converts the string to lowercase (more aggressive than lower()).
```python
text = "HELLO"
print(text.casefold())  # hello
```
### 3. center(width)
👉 Centers the string within the specified width.
```python
text = "cat"
print(text.center(10, "-"))  # ---cat----
```
### 4. count(sub)
👉 Returns the number of occurrences of a substring.
```python
text = "banana"
print(text.count("a"))  # 3
```
### 5. encode()
👉 Returns encoded version of the string.
```python
text = "hello"
print(text.encode())  # b'hello'
```
### 6. endswith(suffix)
👉 Checks if string ends with the specified suffix.
```python
text = "hello.txt"
print(text.endswith(".txt"))  # True
```
### 7. find(sub)
👉 Returns the lowest index of the substring or -1 if not found.
```python
text = "elephant"
print(text.find("ph"))  # 3
```
### 8. format()
👉 Formats string using placeholders.
```python
print("My name is {}".format("Alice"))  # My name is Alice
```
### 9. index(sub)
👉 Returns index of first occurrence. Raises error if not found.
```python
text = "elephant"
print(text.index("ph"))  # 3
```
### 10. isalnum()
👉 Returns True if string has only alphanumeric characters.
```python
text = "abc123"
print(text.isalnum())  # True
```
### 11. isalpha()
👉 Returns True if all characters are alphabetic.
```python
text = "Hello"
print(text.isalpha())  # True
```
### 12. isdigit()
👉 Returns True if all characters are digits.
```python
text = "12345"
print(text.isdigit())  # True
```
### 13. islower()
👉 Returns True if all characters are lowercase.
```python
text = "hello"
print(text.islower())  # True
```
### 14. isupper()
👉 Returns True if all characters are uppercase.
```python
text = "HELLO"
print(text.isupper())  # True
```

### 15. isspace()
👉 Returns True if string only contains whitespace.
```python
text = "   "
print(text.isspace())  # True
```
### 16. istitle()
👉 Returns True if string follows title case.
```python
text = "Hello World"
print(text.istitle())  # True
```
### 17. join(iterable)
👉 Joins elements of an iterable with the string as separator.
```python
words = ["a", "b", "c"]
print("-".join(words))  # a-b-c
```

### 18. lower()
👉 Converts string to lowercase.
```python
text = "HELLO"
print(text.lower())  # hello
```
### 19. upper()
👉 Converts string to uppercase.
```python
text = "hello"
print(text.upper())  # HELLO
```

### 20. replace(old, new)
👉 Replaces old substring with new one.
```python
text = "I like apple"
print(text.replace("apple", "banana"))  # I like banana
```
21. rfind()
👉 Returns highest index of substring.
```python
text = "banana"
print(text.rfind("a"))  # 5
```
### 22. split()
👉 Splits string into a list.
```python
text = "a,b,c"
print(text.split(","))  # ['a', 'b', 'c']
```

### 23. strip()
👉 Removes whitespace from both ends.
```python
text = "  hello  "
print(text.strip())  # hello
```

### 24. startswith(prefix)
👉 Checks if string starts with the specified prefix.
```python
text = "hello world"
print(text.startswith("hello"))  # True
```
### 25. title()
👉 Converts string to title case.
```python
text = "hello world"
print(text.title())  # Hello World
```

### 26. swapcase()
👉 Swaps uppercase to lowercase and vice versa.
```python
text = "Hello World"
print(text.swapcase())  # hELLO wORLD
```
27. zfill(width)
👉 Pads the string on the left with zeros to make it width characters long.
```python
text = "42"
print(text.zfill(5))  # 00042
```
