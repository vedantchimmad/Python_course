# 🔄 Python Nested `if` Statement

---

Nested `if` statements mean using an `if` or `if...else` block **inside another `if` or `else` block**. This allows for more complex decision-making.

## 🧾 Syntax

```python
if condition1:
    if condition2:
        # Code block if both condition1 and condition2 are True
    else:
        # Code block if condition1 is True but condition2 is False
else:
    # Code block if condition1 is False
```
### ✅ Example : Grade Evaluator
```python
marks = 85

if marks >= 50:
    print("You passed!")
    if marks >= 80:
        print("Grade: A")
    else:
        print("Grade: B")
else:
    print("You failed.")
```
### 📋 Summary Table
| Outer `if` | Inner `if` | Outcome                    |
| ---------- | ---------- | -------------------------- |
| True       | True       | Execute inner `if` block   |
| True       | False      | Execute inner `else` block |
| False      | -          | Execute outer `else` block |

