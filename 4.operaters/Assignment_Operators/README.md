## 🧷 Python Assignment Operators

Assignment operators in Python are used to assign values to variables. They can also combine an arithmetic operation with assignment.

---

### 📋 Table: Assignment Operators

| Operator | Description                           | Example   | Equivalent To |
|----------|---------------------------------------|-----------|---------------|
| `=`      | Assigns value                         | `x = 5`   | `x = 5`       |
| `+=`     | Add and assign                        | `x += 3`  | `x = x + 3`   |
| `-=`     | Subtract and assign                   | `x -= 2`  | `x = x - 2`   |
| `*=`     | Multiply and assign                   | `x *= 4`  | `x = x * 4`   |
| `/=`     | Divide and assign                     | `x /= 2`  | `x = x / 2`   |
| `//=`    | Floor divide and assign               | `x //= 2` | `x = x // 2`  |
| `%=`     | Modulus and assign                    | `x %= 3`  | `x = x % 3`   |
| `**=`    | Exponentiate and assign               | `x **= 2` | `x = x ** 2`  |
| `&=`     | Bitwise AND and assign                | `x &= 2`  | `x = x & 2`   |
| `\|=`    | Bitwise OR and assign                 | `x \|= 2` | `x = x \| 2`  |
| `^=`     | Bitwise XOR and assign                | `x ^= 2`  | `x = x ^ 2`   |
| `>>=`    | Bitwise right shift and assign        | `x >>= 2` | `x = x >> 2`  |
| `<<=`    | Bitwise left shift and assign         | `x <<= 2` | `x = x << 2`  |

---

## 🧪 Examples

### 1. `=` Assignment
```python
x = 10
print(x)  # 10
```
### 2. `+=` Add and assign
```python
x = 5
x += 3
print(x)  # 8
```
### 3. `-=` Subtract and assign
```python
x = 5
x -= 2
print(x)  # 3
```
### 4. `*=` Multiply and assign
```python
x = 4
x *= 3
print(x)  # 12
```
### 5. `/=` Divide and assign
```python
x = 10
x /= 2
print(x)  # 5.0
```
### 6. `//=` Floor divide and assign
```python
x = 9
x //= 2
print(x)  # 4
```
### 7. `%=` Modulus and assign
```python
x = 7
x %= 4
print(x)  # 3
```
### 8. `**=` Power and assign
```python
x = 2
x **= 3
print(x)  # 8
```
### 9. `&=` Bitwise AND and assign
```python
x = 5  # 0101
x &= 3  # 0011
print(x)  # 1
```
### 10. `|=` Bitwise OR and assign
```python
x = 5  # 0101
x |= 3  # 0011
print(x)  # 7
```
### 11. `^=` Bitwise XOR and assign
```python
x = 5  # 0101
x ^= 3  # 0011
print(x)  # 6
```
### 12. `>>=` Right shift and assign
```python
x = 8  # 1000
x >>= 2
print(x)  # 2
```
### 13. `<<=` Left shift and assign
```python
x = 3  # 0011
x <<= 2
print(x)  # 12
```