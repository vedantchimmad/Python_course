# Set Methods

---
## Add
* The add() method adds an element to the set.
* If the element already exists, the add() method does not add the element.
>Syntax
>
> set.add(elmnt)

| Parameter | Description                             |
|-----------|-----------------------------------------|
| elmnt     | Required. The element to add to the set |

```python
fruits = {"apple", "banana", "cherry"}

fruits.add("apple")

print(fruits)
```
## clear
The clear() method removes all elements in a set.
>Syntax
> 
> set.clear()
```python
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)
```
## copy
The copy() method copies the set.
>Syntax
> 
> set.copy()
```python
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
```
## difference
* The difference() method returns a set that contains the difference between two sets
* he returned set contains items that exist only in the first set, and not in both sets.
>Syntax
>
> set.difference(set)

| Parameter | Description                                   |
|-----------|-----------------------------------------------|
| set       | Required. The set to check for differences in |

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z)
```
## difference_update
* The difference_update() method removes the items that exist in both sets.
* The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
>Syntax
>
> set.difference_update(set)

| Parameter | Description                                   |
|-----------|-----------------------------------------------|
| set       | Required. The set to check for differences in |

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
```
## discard
* The discard() method removes the specified item from the set.
* This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
>Syntax
>
> set.discard(value)

| Parameter | Description                                   |
|-----------|-----------------------------------------------|
| value     | 	Required. The item to search for, and remove |

```python
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
```
## intersection
* The intersection() method returns a set that contains the similarity between two or more sets.
* The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
>Syntax
>
> set.intersection(set1, set2 ... etc)

| Parameter | Description                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------|
| set1      | 	Required. The set to search for equal items in                                                                           |
| set2      | Optional. The other set to search for equal items in.You can compare as many sets you like.Separate the sets with a comma |
```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
```
## intersection_update
* The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
* The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
>Syntax
>
> set.intersection_update(set1, set2 ... etc)

| Parameter | Description                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------|
| set1      | 	Required. The set to search for equal items in                                                                           |
| set2      | Optional. The other set to search for equal items in.You can compare as many sets you like.Separate the sets with a comma |
```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
```
## isdisjoint
* The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
>Syntax
>
> set.isdisjoint(set)

| Parameter | Description                                     |
|-----------|-------------------------------------------------|
| set       | 	Required. The set to search for equal items in |

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

print(z)
```
## issubset
* The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
>Syntax
>
> set.issubset(set)

| Parameter | Description                                     |
|-----------|-------------------------------------------------|
| set       | 	Required. The set to search for equal items in |

```python
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)
```
## issuperset
* The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.
>Syntax
>
> set.issuperset(set)

| Parameter | Description                                     |
|-----------|-------------------------------------------------|
| set       | 	Required. The set to search for equal items in |

```python
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
```
## pop
The pop() method removes a random item from the set.
>Syntax
>
> set.pop()
```python
fruits = {"apple", "banana", "cherry"}

x = fruits.pop()

print(x)
```
## remove
* The remove() method removes the specified element from the set.
* This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
>Syntax
>
> set.remove(item)

| Parameter | Description                                    |
|-----------|------------------------------------------------|
| item      | Required. The item to search for, and remove   |

```python
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
```
## symmetric_difference
* The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
* The returned set contains a mix of items that are not present in both sets.
>Syntax
>
> set.symmetric_difference(set)

| Parameter  | Description                                   |
|------------|-----------------------------------------------|
| set        | 	Required. The set to check for matches in  |

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
```
## symmetric_difference_update
*The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
>Syntax
>
> set.symmetric_difference_update(set)

| Parameter  | Description                                   |
|------------|-----------------------------------------------|
| set        | 	Required. The set to check for matches in  |

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
```
## union
* The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
>Syntax
>
> set.union(set1, set2...)

| Parameter | Description                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------|
| set1      | 	Required. The iterable to unify with                                                                                        |
| set2      | Optional. The other iterable to unify with.You can compare as many iterables as you like.Separate each iterable with a comma |

```python
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)
```
## update
* The update() method updates the current set, by adding items from another set (or any other iterable).
* If an item is present in both sets, only one appearance of this item will be present in the updated set.
>Syntax
>
> set.update(set)

| Parameter | Description                                            |
|----------|--------------------------------------------------------|
| set      | 	Required. The iterable insert into the current set    |

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)
```
