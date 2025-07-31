## 🧠 Python Bitwise Operators

Bitwise operators perform operations on binary representations of integers.

---

### 🧮 Bitwise Operator Table

| Operator | Name             | Description                                  | Example (`a=10`, `b=4`) | Binary |
|----------|------------------|----------------------------------------------|--------------------------|--------|
| `&`      | AND              | Bits that are 1 in both operands             | `a & b` → `0`            | `1010 & 0100 = 0000` |
| `|`      | OR               | Bits that are 1 in either operand            | `a | b` → `14`           | `1010 | 0100 = 1110` |
| `^`      | XOR              | Bits that are different in operands          | `a ^ b` → `14`           | `1010 ^ 0100 = 1110` |
| `~`      | NOT              | Inverts all bits (1’s to 0’s, 0’s to 1’s)    | `~a` → `-11`             | `~00001010 = 11110101` (2's complement) |
| `<<`     | Left Shift       | Shifts bits to the left                      | `a << 2` → `40`          | `1010 << 2 = 101000` |
| `>>`     | Right Shift      | Shifts bits to the right                     | `a >> 2` → `2`           | `1010 >> 2 = 0010` |

---

## 🔎 Binary Reference

| Decimal | Binary |
|---------|--------|
| 10      | 1010   |
| 4       | 0100   |

---

## ✅ Bitwise Operator Examples

### 1. `&` Bitwise AND
```python
a = 10  # 1010
b = 4   # 0100
print(a & b)  # 0
```
### 2. `|` Bitwise OR
```python
a = 10
b = 4
print(a | b)  # 14
```
### 3. `^` Bitwise XOR
```python
a = 10
b = 4
print(a ^ b)  # 14
```

### 4. `~` Bitwise NOT
```python
a = 10
print(~a)  # -11
```
>    🧠 Note:
> * ~a = -(a + 1)
### 5. `<<` Left Shift
```python
a = 10
print(a << 2)  # 40
```
### 6. `>>` Right Shift
```python
a = 10
print(a >> 2)  # 2
```