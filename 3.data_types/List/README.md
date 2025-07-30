# 📘 Python List

A **List** in Python is a collection of **ordered**, **mutable**, and **allowing duplicate** elements.

```python
# Example list
my_list = [1, 2, 3, 4, 5]
```
### 🔹 List Characteristics
| Property          | Description                         |
| ----------------- | ----------------------------------- |
| Ordered           | Items have a defined order          |
| Mutable           | You can change items after creation |
| Allows Duplicates | Yes                                 |
| Indexing          | 0-based indexing                    |
| Nesting           | Lists can contain other lists       |
### ✅ Common List Operations
```python
my_list = [10, 20, 30, 40]

print(my_list[1])       # 20
print(my_list[-1])      # 40
print(my_list[1:3])     # [20, 30]

my_list[1] = 25
print(my_list)          # [10, 25, 30, 40]
```
### 🛠 List Methods
| Method         | Description                                    | Example              |
| -------------- | ---------------------------------------------- | -------------------- |
| `append(x)`    | Adds item at the end                           | `lst.append(6)`      |
| `extend(iter)` | Appends all items from iterable                | `lst.extend([7,8])`  |
| `insert(i, x)` | Inserts item at index                          | `lst.insert(1, 'a')` |
| `remove(x)`    | Removes first occurrence of x                  | `lst.remove(30)`     |
| `pop([i])`     | Removes & returns item at index (default last) | `lst.pop()`          |
| `clear()`      | Removes all elements                           | `lst.clear()`        |
| `index(x)`     | Returns index of first x                       | `lst.index(25)`      |
| `count(x)`     | Returns number of times x appears              | `lst.count(10)`      |
| `sort()`       | Sorts the list in-place                        | `lst.sort()`         |
| `reverse()`    | Reverses the list in-place                     | `lst.reverse()`      |
| `copy()`       | Returns shallow copy                           | `lst.copy()`         |
### 🔄 Looping Through a List
```python
my_list = [1, 2, 3]

for item in my_list:
    print(item)
```
### 🔧 List Comprehension
```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```
### 📚 Nested List
```python
matrix = [[1,2,3], [4,5,6]]
print(matrix[1][2])  # 6
```
### 🔎 Summary Table
| Feature    | Supported |
| ---------- | --------- |
| Indexing   | ✅         |
| Slicing    | ✅         |
| Duplicates | ✅         |
| Mutability | ✅         |
| Nesting    | ✅         |


