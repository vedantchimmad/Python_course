# List Methods

---
## append
The append() method appends an element to the end of the list.

>Syntax
> 
> list.append(elmnt)

| Parameter | Description                                             |
|-----------|---------------------------------------------------------|
|elmnt| Required. An element of any type (string, number, object etc.)|

```python
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
```
## clear
The clear() method removes all the elements from a list.

>Syntax
> 
> list.clear()
```python
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
```
## copy
The copy() method returns a copy of the specified list.
>Syntax
>
> list.copy()
```python
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
```
## count
The count() method returns the number of elements with the specified value.
>Syntax
>
> list.count(value)

| Parameter | Description                                                                      |
|-----------|----------------------------------------------------------------------------------|
| value     | Required. Any type (string, number, list, tuple, etc.). The value to search for. |

```python
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
```
## extend
The extend() method adds the specified list elements (or any iterable) to the end of the current list.
>Syntax
>
> list.extend(iterable)

| Parameter | Description                                     |
|-----------|-------------------------------------------------|
| iterable  | Required. Any iterable (list, set, tuple, etc.) |

```python
fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)
```
## index
The index() method returns the position at the first occurrence of the specified value.
>Syntax
>
> list.index(elmnt)

| Parameter | Description                                                                |
|-----------|----------------------------------------------------------------------------|
| elmnt     | Required. Any type (string, number, list, etc.). The element to search for |

```python
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
```
## insert
The insert() method inserts the specified value at the specified position.
>Syntax
>
> list.insert(pos, elmnt)

| Parameter | Description                                                         |
|-----------|---------------------------------------------------------------------|
| pos       | Required. A number specifying in which position to insert the value |
| elmnt     | Required. An element of any type (string, number, object etc.)      |

```python
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
```
## pop
The pop() method removes the element at the specified position.
>Syntax
>
> list.pop(pos)

| Parameter | Description                                                                                                                    |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|
| pos     | Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item |

```python
fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)
```
>[!NOTE]
> 
> The pop() method returns removed value.

## remove
The remove() method removes the first occurrence of the element with the specified value.
>Syntax
>
> list.remove(elmnt)

| Parameter | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| elmnt     | Required. Any type (string, number, list etc.) The element you want to remove  |
|

```python
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
```
## reverse
The reverse() method reverses the sorting order of the elements.
>Syntax
>
> list.reverse()

```python
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
```
## sort
The sort() method sorts the list ascending by default.
>Syntax
>
> list.sort(reverse=True|False, key=myFunc)

| Parameter | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| reverse   | Optional. reverse=True will sort the list descending. Default is reverse=False |
| key       | Optional. A function to specify the sorting criteria(s)                        |

```python
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
```
```python
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
```
```python
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
```
```python
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
```