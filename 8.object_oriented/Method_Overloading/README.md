# 🔁 Method Overloading

---

### 📌 Definition

**Method Overloading** refers to the ability to define multiple methods with the same name but different sets of parameters (type or number of arguments).

> **⚠️ Note**  
> Python **does not support** traditional method overloading like some other languages (e.g., Java or C++).

---

### 🔹 Why It Doesn't Work in Python?

In Python, if you define a method multiple times in the same class, only the **last definition** will be used. Earlier ones are overwritten.

---

### ✅ Workaround: Using `multipledispatch`

Python supports **function overloading** using the external package [`multipledispatch`](https://pypi.org/project/multipledispatch/).

#### 🛠 Install the package

```bash
pip install multipledispatch
```
### 💡 Example: Method Overloading with dispatch
```python
from multipledispatch import dispatch

class Example:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

obj = Example()

print(obj.add(10, 20))       # Output: 30
print(obj.add(10, 20, 30))   # Output: 60

```
### 📎 Summary
* ✅ Python supports overloading through multipledispatch.
* ❌ Native Python method overloading is not available.
* 👍 Use @dispatch decorator to create clean, overload-like behavior.