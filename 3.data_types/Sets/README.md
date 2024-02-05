# Sets

---
* Sets are used to store multiple items in a single variable.
* A set is a collection which is unordered, unchangeable*,unindexed and do not allow duplicate values.
* A set can contain different data types.
```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```
>[!NOTE]
>
>*  Note: The values True and 1 are considered the same value in sets, and are treated as duplicates
>* The values False and 0 are considered the same value in sets, and are treated as duplicates
## Length of a Set
```python
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
```
## set() Constructor
It is also possible to use the set() constructor to make a set.
```python
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
```
## Access Set Items
* You cannot access items in a set by referring to an index or a key.

* But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```
## Add Set Items
Once a set is created, you cannot change its items, but you can add new items.
* To add one item to a set use the add() method.
```python
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```
* To add items from another set into the current set, use the update() method.
```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```
* The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
```
## Remove Set Items
* To remove an item in a set, use the remove(), or the discard() method.
  ```python
  thisset = {"apple", "banana", "cherry"}

  thisset.remove("banana")

  print(thisset)
  ```
  >[!NOTE]
  >
  > If the item to remove does not exist, remove() will raise an error.
* Remove "banana" by using the discard() method.
  ```python
  thisset = {"apple", "banana", "cherry"}

  thisset.discard("banana")

  print(thisset)
  ```
  >[!NOTE]
  > 
  >If the item to remove does not exist, discard() will NOT raise an error.
* You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
  ```python
  thisset = {"apple", "banana", "cherry"}

  x = thisset.pop()

  print(x)

  print(thisset)
  ```
  >[!NOTE]
  > 
  > Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
* The clear() method empties the set
  ```python
  thisset = {"apple", "banana", "cherry"}

  thisset.clear()

  print(thisset)
  ```
* The del keyword will delete the set completely.
  ```python
  thisset = {"apple", "banana", "cherry"}

  del thisset

  print(thisset)
  ```
## Loop Sets
* You can loop through the set items by using a for loop.
```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```
## Join Sets
* The union() method returns a new set with all items from both sets
  ```python
  set1 = {"a", "b" , "c"}
  set2 = {1, 2, 3}

  set3 = set1.union(set2)
  print(set3)
  ```
* The update() method inserts the items in set2 into set1.
  ```python
  set1 = {"a", "b" , "c"}
  set2 = {1, 2, 3}

  set1.update(set2)
  print(set1)
  ```
  >[!NOTE]
  > 
  >Both union() and update() will exclude any duplicate items.
* The intersection_update() method will keep only the items that are present in both sets.
  ```python
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}

  x.intersection_update(y)

  print(x)
  ```
* The intersection() method will return a new set, that only contains the items that are present in both sets.
  ```python
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}

  z = x.intersection(y)

  print(z)
  ```
* The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
  ```python
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}

  x.symmetric_difference_update(y)

  print(x)
  ```
* The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
  ```python
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}

  z = x.symmetric_difference(y)

  print(z)
  ```