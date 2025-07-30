# 🧾 Python Dictionaries

---

### 📘 What is a Dictionary?

- A **dictionary** is a collection of **key-value** pairs.
- Unordered (until Python 3.7), changeable (mutable), and does not allow duplicate keys.

#### 🧠 Note:
* Dictionary keys must be immutable (string, number, tuple).
* Values can be of any data type.
* Duplicate keys are not allowed — the last assignment wins.
```python
my_dict = {
  "name": "Alice",
  "age": 25,
  "city": "New York"
}
```
### 🧩 Dictionary Features
| Feature         | Description               | Example               |
| --------------- | ------------------------- | --------------------- |
| Unordered       | Items have no index       | `{}` vs list `[ ]`    |
| Key-Value Pairs | Keys must be unique       | `"name": "Alice"`     |
| Mutable         | You can add/change/remove | `dict["key"] = value` |
 
### 🔍 Accessing Dictionary Items
```python
print(my_dict["name"])        # Alice
print(my_dict.get("age"))     # 25
```
### 🧱 Dictionary Methods
| Method               | Description                        | Example                       |
| -------------------- | ---------------------------------- | ----------------------------- |
| `dict.get(key)`      | Returns the value of specified key | `my_dict.get("name")`         |
| `dict.keys()`        | Returns all keys                   | `my_dict.keys()`              |
| `dict.values()`      | Returns all values                 | `my_dict.values()`            |
| `dict.items()`       | Returns all key-value pairs        | `my_dict.items()`             |
| `dict.update({...})` | Updates with another dict          | `my_dict.update({"age": 26})` |
| `dict.pop(key)`      | Removes item by key                | `my_dict.pop("city")`         |
| `dict.clear()`       | Clears the dictionary              | `my_dict.clear()`             |
### ✏️ Updating Values
```python
my_dict["age"] = 30
my_dict["email"] = "alice@example.com"
```
### 🚮 Removing Items
```python
del my_dict["city"]
my_dict.pop("age")
```
### 🔁 Looping Through Dictionary
```python
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(f"{key} => {value}")
```
### 📐 Nested Dictionaries
```python
students = {
  "student1": {"name": "Alice", "age": 25},
  "student2": {"name": "Bob", "age": 22}
}
print(students["student1"]["name"])  # Alice
```
### 🎯 Dictionary Comprehension
```python
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

