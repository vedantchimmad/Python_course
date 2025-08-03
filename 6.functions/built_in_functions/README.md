# 📘 Python Built-in Functions

Python provides a rich set of built-in functions that are always available for use. These functions perform common tasks and help simplify code.

---

## 📌 Table of Contents

- [abs()](#abs)
- [all()](#all)
- [any()](#any)
- [bin()](#bin)
- [chr()](#chr)
- [filter()](#filter)
- [input()](#input)
- [len()](#len)
- [map()](#map)
- [max()](#max)
- [min()](#min)
- [iter()](#iter)
- [next()](#next)
- [open()](#open)
- [pow()](#pow)
- [range()](#range)
- [reversed()](#reversed)
- [round()](#round)
- [slice()](#slice)
- [sorted()](#sorted)
- [sum()](#sum)
- [super()](#super)
- [zip()](#zip)

---

## 🧮 abs()

Returns the absolute value of a number.

```python
x = abs(-7.25)
print(x)  # 7.25
```

| Parameter | Description            |
|-----------|------------------------|
| n         | Required. A number     |

---

## ✅ all()

Returns `True` if all items in an iterable are true (or if iterable is empty).

```python
mylist = [True, 1, "hello"]
print(all(mylist))  # True
```

| Parameter | Description                    |
|-----------|--------------------------------|
| iterable  | An iterable like list/tuple    |

---

## 🔍 any()

Returns `True` if any item in an iterable is true.

```python
mylist = [0, False, 5]
print(any(mylist))  # True
```

---

## 🔢 bin()

Returns the binary representation of an integer.

```python
print(bin(10))  # 0b1010
```

---

## 🔠 chr()

Returns the character that represents the specified Unicode.

```python
print(chr(97))  # 'a'
```

---

## 🔍 filter()

Filters elements using a function.

```python
nums = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [2, 4]
```

---

## 🧾 input()

Takes input from the user.

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

## 🔢 len()

Returns the length (number of items) of an object.

```python
x = len("Vedant")
print(x)  # 6
```

---

## 🔁 map()

Applies a function to all items in an iterable.

```python
nums = [1, 2, 3]
squared = map(lambda x: x**2, nums)
print(list(squared))  # [1, 4, 9]
```

---

## 🧮 max()

Returns the item with the highest value.

```python
print(max([4, 7, 1]))  # 7
```

---

## 🧮 min()

Returns the item with the lowest value.

```python
print(min([4, 7, 1]))  # 1
```

---

## 🔁 iter()

Returns an iterator object.

```python
mylist = [1, 2, 3]
it = iter(mylist)
print(next(it))  # 1
```

---

## ⏭️ next()

Returns the next item from an iterator.

```python
it = iter(["a", "b"])
print(next(it))  # a
print(next(it))  # b
```

---

## 📂 open()

Opens a file and returns a file object.

```python
f = open("sample.txt", "r")
print(f.read())
```

| Mode | Description |
|------|-------------|
| "r"  | Read (default) |
| "w"  | Write |
| "a"  | Append |
| "x"  | Create |
| "t"  | Text mode (default) |
| "b"  | Binary mode |

---

## 🔢 pow()

Returns the result of a number raised to a power.

```python
print(pow(2, 3))       # 8
print(pow(2, 3, 5))    # 3 (8 % 5)
```

---

## 🔁 range()

Returns a sequence of numbers.

```python
for i in range(1, 5):
    print(i)
```

---

## 🔄 reversed()

Returns a reversed iterator.

```python
for i in reversed(["a", "b", "c"]):
    print(i)
```

---

## 🔁 round()

Rounds a number to specified decimals.

```python
print(round(3.14159, 2))  # 3.14
```

---

## ✂️ slice()

Returns a slice object to slice sequences.

```python
s = "Python"
print(s[slice(1, 4)])  # yth
```

---

## 🔃 sorted()

Returns a sorted list.

```python
print(sorted([3, 1, 2]))  # [1, 2, 3]
```

---

## ➕ sum()

Returns the sum of all items in an iterable.

```python
print(sum([1, 2, 3]))  # 6
```

---

## 🧬 super()

Calls a method from a parent class.

```python
class A:
    def __init__(self):
        print("Parent")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child")

B()
```

---

## 🔗 zip()

Combines multiple iterables element-wise.

```python
names = ["a", "b"]
scores = [10, 20]
print(list(zip(names, scores)))  # [('a', 10), ('b', 20)]
```

---

> 🔖 **Tip**: All these functions are part of the Python standard library and do not require any imports.

📌 For a complete list of all Python built-in functions, refer to:  
🔗 [Python Docs - Built-in Functions](https://docs.python.org/3/library/functions.html)