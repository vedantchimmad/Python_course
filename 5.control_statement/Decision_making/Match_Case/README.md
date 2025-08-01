# 🎯 Python `match-case` Statement (Structural Pattern Matching)

---

Introduced in **Python 3.10**, the `match-case` statement is similar to `switch-case` found in other languages like C, Java, etc. It provides a more readable way to handle **multiple conditional branches**.

---

## 🧾 Syntax

```python
match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default block (like else)
```
### ✅ Example: Grade Evaluator
```python
grade = 'B'

match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case _:
        print("Fail or Invalid grade")
```
### 🧠 Summary Table
| Value   | Matches Case | Output       |
| ------- | ------------ | ------------ |
| 3       | case 3       | "Three"      |
| 'B'     | case 'B'     | "Good"       |
| 75      | if >= 75     | "Grade B"    |
| Unknown | case \_      | Default case |
