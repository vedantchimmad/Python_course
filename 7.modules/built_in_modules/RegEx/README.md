# 🔎 `re` — Regular Expressions in Python

The `re` module provides support for working with **Regular Expressions** in Python. It allows pattern matching, searching, substitution, and splitting based on patterns.

---

## ✅ Common Functions

| Function           | Description                              |
|--------------------|------------------------------------------|
| `re.search()`      | Searches for a pattern in a string       |
| `re.match()`       | Matches pattern only at the beginning    |
| `re.findall()`     | Returns all non-overlapping matches      |
| `re.finditer()`    | Returns an iterator yielding match objs  |
| `re.sub()`         | Substitutes pattern with replacement     |
| `re.split()`       | Splits string by pattern                 |
| `re.compile()`     | Compiles regex pattern for reuse         |

---

## 🧪 Example 1: `re.search()`

```python
import re

text = "The rain in Spain"
match = re.search("rain", text)
if match:
    print("Found:", match.group())  # Found: rain
```

---

## 🧪 Example 2: `re.findall()`

```python
text = "apple, banana, apple"
matches = re.findall("apple", text)
print(matches)  # ['apple', 'apple']
```

---

## 🧪 Example 3: `re.sub()`

```python
text = "cat sat on the mat"
result = re.sub("cat", "dog", text)
print(result)  # dog sat on the mat
```

---

## 🧪 Example 4: `re.split()`

```python
text = "apple1banana2cherry"
result = re.split(r"\d", text)
print(result)  # ['apple', 'banana', 'cherry']
```

---

## 🧪 Example 5: `re.compile()`

```python
pattern = re.compile(r"\d+")
matches = pattern.findall("Item 123, code 456")
print(matches)  # ['123', '456']
```

---

## 🧪 Example 6: `re.match()`

```python
text = "hello world"
match = re.match("hello", text)
if match:
    print("Match at start:", match.group())  # Match at start: hello
```

---

## 🧾 Common Regex Metacharacters

| Symbol | Description                 |
|--------|-----------------------------|
| `.`    | Any character (except newline) |
| `^`    | Start of string              |
| `$`    | End of string                |
| `*`    | 0 or more repetitions        |
| `+`    | 1 or more repetitions        |
| `?`    | 0 or 1 repetition            |
| `{n}`  | Exactly n repetitions        |
| `[]`   | Set of characters            |
| `|`    | Either/or                    |
| `\d`   | Digit                        |
| `\w`   | Alphanumeric character       |
| `\s`   | Whitespace                   |

---

> 📘 **Note**: Always use raw strings (`r"..."`) to avoid issues with backslashes in regex patterns.
