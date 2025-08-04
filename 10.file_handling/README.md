# 📁 File Handling in Python

---

Python provides built-in functions and methods to handle files, allowing you to **create**, **read**, **write**, and **append** files easily.

---

## 🔹 File Modes

| Mode  | Description                      |
| ----- | -------------------------------- |
| `'r'` | Read (default mode)              |
| `'w'` | Write (overwrites existing file) |
| `'x'` | Create (fails if file exists)    |
| `'a'` | Append to the end of file        |
| `'b'` | Binary mode                      |
| `'t'` | Text mode (default)              |
| `'+'` | Read and write                   |

---

## 🔸 Open a File

```python
f = open("open.txt")
```

If the file is located in a different location:

```python
f = open("D:\\myfiles\\welcome.txt", "r")
print(f.read())
```

---

## 📖 Read from File

```python
f = open("open.txt", "r")
print(f.read(5))  # Read first 5 characters
```

```python
f = open("demofile.txt", "r")
print(f.readline())  # Read one line
```

---

## ❌ Close a File

```python
f = open("open.txt", "r")
print(f.readline())
f.close()
```

---

## ✍️ Write to a File

```python
f = open("vedant.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("vedant.txt", "r")
print(f.read())
```

---

## 🆕 Create a New File

```python
f = open("myfile.txt", "x")
```

---

## 🗑️ Delete a File

```python
import os
os.remove("demofile.txt")
```

```python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

---

## 📂 Delete Folder

```python
import os
os.rmdir("myfolder")
```

> \[!NOTE]
> Always close the file after you're done, or use the `with` statement which handles it automatically.

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```
