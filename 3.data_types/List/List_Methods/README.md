## 📘 Python List Methods 

Below are the commonly used list methods with individual examples.

---

### 🔹 1. `append()`
Adds a single element to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']
```
### 🔹 2. extend()
Adds all elements from another iterable (list, tuple, etc.).
```python
fruits = ["apple", "banana"]
fruits.extend(["kiwi", "orange"])
print(fruits)  # ['apple', 'banana', 'kiwi', 'orange']
```
### 🔹 3. insert()
Inserts an element at the specified position.
```python
fruits = ["apple", "banana"]
fruits.insert(1, "grape")
print(fruits)  # ['apple', 'grape', 'banana']
```
### 🔹 4. remove()
Removes the first occurrence of the specified value.
```python
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)  # ['banana', 'apple']
```
### 🔹 5. pop()
Removes and returns the element at the specified position (or last by default).
```python
fruits = ["apple", "banana", "cherry"]
popped_item = fruits.pop()
print(popped_item)  # cherry
print(fruits)       # ['apple', 'banana']
```
### 🔹 6. clear()
Removes all elements from the list.
```python
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # []
```
### 🔹 7. index()
Returns the index of the first occurrence of the specified value.
```python
fruits = ["apple", "banana", "cherry"]
idx = fruits.index("banana")
print(idx)  # 1
```
### 🔹 8. count()
Returns the number of times a value appears in the list.
```python
fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # 2
```
### 🔹 9. sort()
Sorts the list in ascending order.
```python
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]
```
### 🔹 10. reverse()
Reverses the order of the elements in the list.
```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # [4, 3, 2, 1]
```
### 🔹 11. copy()
Returns a shallow copy of the list.
```python
original = ["apple", "banana"]
copied = original.copy()
print(copied)  # ['apple', 'banana']
```
---
## 🛠 All Common List Methods
| Method             | Description                                       | Example                             |
| ------------------ | ------------------------------------------------- | ----------------------------------- |
| `append(x)`        | Adds an element to the end of the list            | `fruits.append("orange")`           |
| `extend(iterable)` | Adds all elements from an iterable                | `fruits.extend(["grape", "melon"])` |
| `insert(i, x)`     | Inserts an element at a specific position         | `fruits.insert(1, "kiwi")`          |
| `remove(x)`        | Removes the first item with the specified value   | `fruits.remove("banana")`           |
| `pop([i])`         | Removes the element at the given position         | `fruits.pop(2)`                     |
| `clear()`          | Removes all elements from the list                | `fruits.clear()`                    |
| `index(x)`         | Returns the index of the first item with value x  | `fruits.index("apple")`             |
| `count(x)`         | Returns the count of a value                      | `fruits.count("apple")`             |
| `sort()`           | Sorts the list in ascending order (modifies list) | `fruits.sort()`                     |
| `reverse()`        | Reverses the order of elements in the list        | `fruits.reverse()`                  |
| `copy()`           | Returns a shallow copy of the list                | `new_fruits = fruits.copy()`        |
