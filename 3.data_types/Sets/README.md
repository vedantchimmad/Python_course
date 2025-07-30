# 📘 Python Sets

---
A **set** is a collection which is unordered, unchangeable (items cannot be changed, but you can add/remove items), and unindexed. Sets do not allow duplicate values.


### ✅ Create a Set

```python
my_set = {"apple", "banana", "cherry"}
print(my_set)
```
### ❗ Duplicates Not Allowed
```python
my_set = {"apple", "banana", "apple"}
print(my_set)  # Output: {'apple', 'banana'}
```
### 🔄 Loop Through a Set
```python
for item in {"apple", "banana", "cherry"}:
    print(item)
```
### 🔍 Check if Item Exists
```python
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)  # Output: True
```
---
## ➕ Add Items
### `add()`
```python
my_set = {"apple", "banana"}
my_set.add("cherry")
print(my_set)
```
### `update()` — Add multiple items
```python
my_set = {"apple", "banana"}
my_set.update(["cherry", "orange"])
print(my_set)
```
---
## ❌ Remove Items
### `remove()` — Raises error if not found
```python
my_set = {"apple", "banana"}
my_set.remove("banana")
print(my_set)
```
### `discard()` — No error if item not found
```python
my_set = {"apple", "banana"}
my_set.discard("banana")
print(my_set)
```
### `pop()` — Removes a random item
```python
my_set = {"apple", "banana", "cherry"}
item = my_set.pop()
print(item)
print(my_set)
```
### `clear()` — Empties the set
```python
my_set = {"apple", "banana"}
my_set.clear()
print(my_set)  # Output: set()
```
---
## 🧬 Set Operations
### `union()` — Combine sets (no duplicates)
```python
a = {"apple", "banana"}
b = {"cherry", "banana"}
print(a.union(b))  # Output: {'apple', 'banana', 'cherry'}
```
### `intersection()` — Common items
```python
a = {"apple", "banana"}
b = {"banana", "cherry"}
print(a.intersection(b))  # Output: {'banana'}
```
### `difference()` — Items in set A but not in B
```python
a = {"apple", "banana"}
b = {"banana", "cherry"}
print(a.difference(b))  # Output: {'apple'}
```
### `symmetric_difference()` — Items not in both
```python
a = {"apple", "banana"}
b = {"banana", "cherry"}
print(a.symmetric_difference(b))  # Output: {'apple', 'cherry'}
```
