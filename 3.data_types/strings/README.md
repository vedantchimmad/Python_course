## 🔤 Python String Type

---

In Python, **strings** are sequences of characters enclosed in **single**, **double**, or **triple quotes**.

### ✅ Creating Strings
```python
str1 = 'Hello'
str2 = "World"
str3 = '''This is 
a multi-line string.'''
```
### 🧠 String Properties
| Property  | Description                                   |
| --------- | --------------------------------------------- |
| Immutable | Strings cannot be changed after creation      |
| Ordered   | Characters have a defined index (like arrays) |
| Iterable  | You can loop through them                     |
| Indexed   | Supports indexing and slicing                 |
### 📌 String Indexing
Access characters using their index (starts at 0)
```python
text = "Python"
print(text[0])   # P
print(text[-1])  # n
```
### ✂️ String Slicing
```python
text = "Programming"
print(text[0:6])     # Progra
print(text[:4])      # Prog
print(text[4:])      # ramming
```
### 🔄 String Concatenation & Repetition
```python
a = "Hello"
b = "World"
print(a + " " + b)    # Hello World

print(a * 3)          # HelloHelloHello
```
### ✅ Check Membership
```python
text = "Python"
print("y" in text)     # True
print("z" not in text) # True
```
### 📏 String Length
```python
text = "Data"
print(len(text))  # 4
```