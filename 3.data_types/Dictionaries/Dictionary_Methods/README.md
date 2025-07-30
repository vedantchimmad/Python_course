## 📘 Python Dictionary Methods

---

### ✅ 1. dict.clear()
**Removes all elements from the dictionary**

```python
my_dict = {"name": "Alice", "age": 25}
my_dict.clear()
print(my_dict)  # {}
```
### ✅ 2. dict.copy()
**Returns a shallow copy of the dictionary**
```python
original = {"name": "Bob"}
copy_dict = original.copy()
print(copy_dict)  # {'name': 'Bob'}
```
### ✅ 3. dict.fromkeys(seq, value)
**reates a new dictionary with keys from seq and all values set to value**
```python
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}
```
### ✅ 4. dict.get(key, default=None)
**Returns the value for key, or default if the key is not found**
```python
my_dict = {"name": "Alice"}
print(my_dict.get("name"))       # Alice
print(my_dict.get("age", 0))     # 0
```
### ✅ 5. dict.items()
**Returns a view of (key, value) pairs**
```python
my_dict = {"a": 1, "b": 2}
print(list(my_dict.items()))  # [('a', 1), ('b', 2)]
```
### ✅ 6. dict.keys()
**Returns a view of all the keys**
```python
my_dict = {"a": 1, "b": 2}
print(list(my_dict.keys()))  # ['a', 'b']
```
### ✅ 7. dict.values()
**Returns a view of all the values**
```python
my_dict = {"a": 1, "b": 2}
print(list(my_dict.values()))  # [1, 2]
```
### ✅ 8. dict.pop(key[, default])
**Removes key and returns its value; if key not found, returns `default` or raises `KeyError`**
```python
my_dict = {"a": 1, "b": 2}
val = my_dict.pop("b")
print(val)       # 2
print(my_dict)   # {'a': 1}
```
### ✅ 9. dict.popitem()
**Removes and returns the last inserted key-value pair (LIFO)**
```python
my_dict = {"x": 10, "y": 20}
key, val = my_dict.popitem()
print(key, val)  # y 20
```
### ✅ 10. dict.setdefault(key[, default])
**Returns the value of `key`. If not found, inserts key with `default` value**
```python
my_dict = {"a": 100}
val = my_dict.setdefault("b", 200)
print(my_dict)  # {'a': 100, 'b': 200}
```
### ✅ 11. dict.update([other])
**Updates dictionary with key-value pairs from another dictionary or iterable**
```python
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 2}
```
### 🔎 Summary Table:
| Method         | Description                                |
| -------------- | ------------------------------------------ |
| `clear()`      | Removes all items                          |
| `copy()`       | Returns shallow copy                       |
| `fromkeys()`   | Creates new dict from keys & a default val |
| `get()`        | Gets value by key with default             |
| `items()`      | Returns (key, value) pairs                 |
| `keys()`       | Returns keys                               |
| `values()`     | Returns values                             |
| `pop()`        | Removes item by key                        |
| `popitem()`    | Removes last inserted item                 |
| `setdefault()` | Gets value or sets if missing              |
| `update()`     | Adds items from another dict               |
