# Tuple Methods

---
## Count
The count() method returns the number of times a specified value appears in the tuple.

>Syntax
>
> tuple.count(value)

| Parameter | Description                      |
|-----------|----------------------------------|
| value   | Required. The item to search for |

```python
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
```
## Index
* The index() method finds the first occurrence of the specified value.
* The index() method raises an exception if the value is not found.
>Syntax
>
> tuple.index(value)

| Parameter | Description                      |
|-----------|----------------------------------|
| value     | Required. The item to search for |

```python
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
```