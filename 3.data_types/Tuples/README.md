# Tuples

---
Tuples are used to store multiple items in a single variable.
* A tuple is a collection which is ordered and unchangeable.
* Tuple items are ordered, unchangeable, and allow duplicate values.
* Tuple items can be of any data type.
  ```python
  thistuple = ("apple", "banana", "cherry", "apple", "cherry")
  print(thistuple)
  ```
## Tuple length
To determine how many items a tuple has, use the len() function.
```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```
## tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
```python
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```
## Access Tuple Items
* You can access tuple items by referring to the index number, inside square brackets.
  ```python
  thistuple = ("apple", "banana", "cherry")
  print(thistuple[1])
  ```
* Negative indexing means start from the end.
  ```python
  thistuple = ("apple", "banana", "cherry")
  print(thistuple[-1])
  ```
* When specifying a range, the return value will be a new tuple with the specified items.
  ```python
  thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
  print(thistuple[2:5])
  ```
* By leaving out the start value, the range will start at the first item.
  ```python
  thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
  print(thistuple[:4])
  ```
* By leaving out the end value, the range will go on to the end of the tuple.
  ```python
  thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
  print(thistuple[2:])
  ```
## Update Tuples
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
* Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
  But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
  ```python
  x = ("apple", "banana", "cherry")
  y = list(x)
  y[1] = "kiwi"
  x = tuple(y)

  print(x)
  ```
**Convert into a list**: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
   ```python
   thistuple = ("apple", "banana", "cherry")
   y = list(thistuple)
   y.append("orange")
   thistuple = tuple(y)
   ```
## Remove Items
* Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
  ```python
  thistuple = ("apple", "banana", "cherry")
  y = list(thistuple)
  y.remove("apple")
  thistuple = tuple(y)
  ```
* The del keyword can delete the tuple completely.
  ```python
  thistuple = ("apple", "banana", "cherry")
  del thistuple
  print(thistuple) #this will raise an error because the tuple no longer exists
  ```
## Unpack Tuples
When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
*  in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
   ```python
   fruits = ("apple", "banana", "cherry")

   (green, yellow, red) = fruits

   print(green)
   print(yellow)
   print(red)
   ```
* If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
  ```python
  fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

  (green, yellow, *red) = fruits

  print(green)
  print(yellow)
  print(red)
  ```
* If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
  ```python
  fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

  (green, *tropic, red) = fruits

  print(green)
  print(tropic)
  print(red)
  ```
## Loop Tuples
You can loop through the tuple items by using a for loop.
```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```
## Join Tuples
* Join Tuples
  ```python
  tuple1 = ("a", "b" , "c")
  tuple2 = (1, 2, 3)

  tuple3 = tuple1 + tuple2
  print(tuple3)
  ```