# List

---
* Lists are used to store multiple items in a single variable.
* Lists are created using square brackets.
  ```python
  thislist = ["apple", "banana", "cherry"]

  print(type(thislist))
  ```
## Behavior
* List items are ordered, changeable, and allow duplicate values.
* List items are indexed, the first item has index [0], the second item has index [1] etc.
  ```python
  thislist = ["apple", "banana", "cherry"]
  print(thislist[1])
  ```
* To determine how many items a list has, use the len() function.
* List items can be of any data type
  ```python
  thislist = ["apple", "banana", "cherry", "apple", "cherry"]
  print(thislist)
  ```
* It is also possible to use the list() constructor when creating a new list.
  ```python
  thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
  print(thislist)
  ```
## Python Collections
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
*  Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.

## Access List Items
* List items are indexed and you can access them by referring to the index number:
  ```python
  thislist = ["apple", "banana", "cherry"]
  print(thislist[1])
  ```
* Negative indexing means start from the end,-1 refers to the last item, -2 refers to the second last item etc.
  ```python
  thislist = ["apple", "banana", "cherry"]
  print(thislist[-1])
  ```
* You can specify a range of indexes by specifying where to start and where to end the range.
  ```python
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
  print(thislist[2:5])
  ```
* To determine if a specified item is present in a list use the in keyword
  ```python
  thislist = ["apple", "banana", "cherry"]
  if "apple" in thislist:
     print("Yes, 'apple' is in the fruits list")
  ```
## Change List Items
* To change the value of a specific item, refer to the index number
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist[1] = "blackcurrant"
  print(thislist)
  ```
* Change a Range of Item Values
  ```python
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
  thislist[1:3] = ["blackcurrant", "watermelon"]
  
  print(thislist)
  ```
* To insert a new list item, without replacing any of the existing values, we can use the insert() method.
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.insert(2, "watermelon")
  print(thislist)
  ```
## Add List Items
* To add an item to the end of the list, use the append() method.
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.append("orange")
  print(thislist)
  ```
* To insert a list item at a specified index, use the insert() method
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.insert(1, "orange")
  print(thislist)
  ```
* To append elements from another list to the current list, use the extend() method
  ```python
  thislist = ["apple", "banana", "cherry"]
  tropical = ["mango", "pineapple", "papaya"]
  thislist.extend(tropical)
  print(thislist)
  ```
* The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
  ```python
  thislist = ["apple", "banana", "cherry"]
  thistuple = ("kiwi", "orange")
  thislist.extend(thistuple)
  print(thislist)
  ```
## Remove List Items
* The remove() method removes the specified item.
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.remove("banana")
  print(thislist)
  ```
* If there are more than one item with the specified value, the remove() method removes the first occurance.
  ```python
  thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
  thislist.remove("banana")
  print(thislist)
  ```
* The pop() method removes the specified index.
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.pop(1)
  print(thislist)
  ```
* If you do not specify the index, the pop() method removes the last item.
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.pop()
  print(thislist)
  ```
* The del keyword also removes the specified index.
  ```python
  thislist = ["apple", "banana", "cherry"]
  del thislist[0]
  print(thislist)
  ```
* The del keyword can also delete the list completely.
  ```python
  thislist = ["apple", "banana", "cherry"]
  del thislist
  ```
* The clear() method empties the list.The list still remains, but it has no content.
  ```python
  thislist = ["apple", "banana", "cherry"]
  thislist.clear()
  print(thislist)
  ```
## Loop Lists
* You can loop through the list items by using a for loop
  ```python
  thislist = ["apple", "banana", "cherry"]
  for x in thislist:
  print(x)
  ```
* Use the range() and len() functions to create a suitable iterable.
  ```python
  thislist = ["apple", "banana", "cherry"]
  for i in range(len(thislist)):
  print(thislist[i])
  ```
* You can loop through the list items by using a while loop
  ```python
  thislist = ["apple", "banana", "cherry"]
  i = 0
  while i < len(thislist):
    print(thislist[i])
    i = i + 1
  ```
* List Comprehension offers the shortest syntax for looping through lists
  ```python
  thislist = ["apple", "banana", "cherry"]
  [print(x) for x in thislist]
  ```
## List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
>Syntax
> 
> newlist = [expression for item in iterable if condition == True]

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```
## Sort Lists
* List objects have a sort() method that will sort the list alphanumerically, ascending, by default
  ```python
  thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
  thislist.sort()
  print(thislist)
  ```
* Sort the list numerically.
  ```python
  thislist = [100, 50, 65, 82, 23]
  thislist.sort()
  print(thislist)
  ```
* To sort descending, use the keyword argument reverse = True.
  ```python
  thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
  thislist.sort(reverse = True)
  print(thislist)
  ```
* You can also customize your own function by using the keyword argument key = function.
  ```python
  def myfunc(n):
     return abs(n - 50)

  thislist = [100, 50, 65, 82, 23]
  thislist.sort(key = myfunc)
  print(thislist)
  ```
* By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
  ```python
  thislist = ["banana", "Orange", "Kiwi", "cherry"]
  thislist.sort()
  print(thislist)
  ```
* The reverse() method reverses the current sorting order of the elements.
  ```python
  thislist = ["banana", "Orange", "Kiwi", "cherry"]
  thislist.reverse()
  print(thislist)
  ```
## Copy Lists
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
* There are ways to make a copy, one way is to use the built-in List method copy().
  ```python
  thislist = ["apple", "banana", "cherry"]
  mylist = thislist.copy()
  print(mylist)
  ```
* Another way to make a copy is to use the built-in method list().
  ```python
  thislist = ["apple", "banana", "cherry"]
  mylist = list(thislist)
  print(mylist)
  ```
## Join Lists
* the easiest ways are by using the + operator.
  ```python
  list1 = ["a", "b", "c"]
  list2 = [1, 2, 3]

  list3 = list1 + list2
  print(list3)
  ```
* Another way to join two lists is by appending all the items from list2 into list1, one by one.
  ```python
  list1 = ["a", "b" , "c"]
  list2 = [1, 2, 3]

  for x in list2:
    list1.append(x)

  print(list1)
  ```
* you can use the extend() method, where the purpose is to add elements from one list to another list
  ```python
  list1 = ["a", "b" , "c"]
  list2 = [1, 2, 3]

  list1.extend(list2)
  print(list1)
  ```