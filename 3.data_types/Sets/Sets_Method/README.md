## 🧰 Python Set Methods

---

Python provides several built-in methods to work with sets.

### 1. `add()`
👉 Adds a single element to the set.

```python
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}
```
### 2. clear()
👉 Removes all elements from the set.
```python
s = {1, 2, 3}
s.clear()
print(s)  # set()
```
### 3. copy()
👉 Returns a shallow copy of the set.
```python
s = {1, 2, 3}
copy_set = s.copy()
print(copy_set)  # {1, 2, 3}
```
### 4. difference()
👉 Returns the difference between two sets.
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))  # {1}
```
### 5. difference_update()
👉 Removes the items from the first set that are also in the second.
```python
a = {1, 2, 3}
b = {2, 3, 4}
a.difference_update(b)
print(a)  # {1}
```
### 6. discard()
👉 Removes the specified item; does NOT raise an error if not found.
```python
s = {1, 2, 3}
s.discard(2)
s.discard(5)
print(s)  # {1, 3}
```
### 7. intersection()
👉 Returns common items from sets.
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
```
### 8. intersection_update()
👉 Keeps only items that are present in both sets.
```python
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)  # {2, 3}
```
### 9. isdisjoint()
👉 Returns True if no items in common.
```python
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True
```
### 10. issubset()
👉 Checks if all items in one set exist in another.
```python
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # True
```
### 11. issuperset()
👉 Checks if a set contains all elements of another set.
```python
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))  # True
```
### 12. pop()
👉 Removes and returns a random element.
```python
s = {1, 2, 3}
s.pop()
print(s)  # May vary, e.g., {2, 3}
```
### 13. remove()
👉 Removes a specific element. Raises error if not found.
```python
s = {1, 2, 3}
s.remove(2)
# s.remove(5)  # Raises KeyError
print(s)  # {1, 3}
```

### 14. symmetric_difference()
👉 Returns elements not common in both sets.
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))  # {1, 4}
```
### 15. symmetric_difference_update()
👉 Updates the set with items that are in either set but not both.
```python
a = {1, 2, 3}
b = {2, 3, 4}
a.symmetric_difference_update(b)
print(a)  # {1, 4}
```
### 16. union()
👉 Combines items from both sets without duplicates.
```python
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}
```
### 17. update()
👉 Adds items from another set (or iterable).
```python
a = {1, 2}
a.update([2, 3, 4])
print(a)  # {1, 2, 3, 4}
```