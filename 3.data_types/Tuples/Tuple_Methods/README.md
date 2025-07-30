## 🔧 Python Tuple Methods

---

Tuples are **immutable**, so they support **fewer methods** than lists. Only two built-in methods are available:

---

### 1. `count()`
👉 Returns the number of times a specified value appears in the tuple.

```python
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))  # Output: 3
```
### 2. index()
👉 Returns the first index of the specified value. Raises ValueError if the value is not found.
```python
t = (10, 20, 30, 20, 40)
print(t.index(20))  # Output: 1
```
### ℹ️ Summary
| Method    | Description                          |
| --------- | ------------------------------------ |
| `count()` | Counts how many times a value occurs |
| `index()` | Finds the index of a value           |
### ✅ Since tuples are immutable:
* No `append()`, `remove()`, `pop()`, or `sort()` like in lists.
* They're useful for fixed data, hashable keys, or when data integrity is required.