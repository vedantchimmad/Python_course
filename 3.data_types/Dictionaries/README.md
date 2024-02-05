# Dictionaries

---
* Dictionaries are used to store data values in key:value pairs.
* A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
* The values in dictionary items can be of any data type.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
## Dictionary Items
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
## The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.
```python
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
## Access Dictionary Items
* You can access the items of a dictionary by referring to its key name, inside square brackets.
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  x = thisdict["model"]
  ```
* There is also a method called get() that will give you the same result.
  ```python
  x = thisdict.get("model")
  ```
## Get Keys
* The keys() method will return a list of all the keys in the dictionary.
  ```python
  x = thisdict.keys()
  ```
* The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
  ```python
  car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }

  x = car.keys()

  print(x) #before the change

  car["color"] = "white"

  print(x) #after the change
  ```
## Get Values
* The values() method will return a list of all the values in the dictionary.
  ```python
  x = thisdict.values()
  ```
* The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
  ```python
  car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }

  x = car.values()

  print(x) #before the change

  car["year"] = 2020

  print(x) #after the change

  ```
## Get Items
* The items() method will return each item in a dictionary, as tuples in a list.
  ```python
  x = thisdict.items()
  ```
* The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
  ```python
  car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }

  x = car.items()

  print(x) #before the change

  car["year"] = 2020

  print(x) #after the change
  ```
## Change Dictionary Items
* You can change the value of a specific item by referring to its key name
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict["year"] = 2018
  ```
## Update Dictionary
The update() method will update the dictionary with the items from the given argument.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```
## Add Dictionary Items
* Adding an item to the dictionary is done by using a new index key and assigning a value to it.
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict["color"] = "red"
  print(thisdict)
  ```
* The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict.update({"color": "red"})
  ```
## Remove Dictionary Items
* The pop() method removes the item with the specified key name
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict.pop("model")
  print(thisdict)
  ```
* The popitem() method removes the last inserted item 
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict.popitem()
  print(thisdict)
  ```
* The del keyword removes the item with the specified key name.
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  del thisdict["model"]
  print(thisdict)
  ```
* The clear() method empties the dictionary.
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict.clear()
  print(thisdict)
  ```
## Loop Dictionaries
* You can loop through a dictionary by using a for loop.
  ```python
  for x in thisdict:
  print(x)
  ```
* You can also use the values() method to return values of a dictionary.
  ```python
  for x in thisdict.values():
  print(x)
  ```
* You can use the keys() method to return the keys of a dictionary.
  ```python
  for x in thisdict.keys():
  print(x)
  ```
* Loop through both keys and values, by using the items() method.
  ```python
  for x, y in thisdict.items():
  print(x, y)
  ```
## Copy Dictionaries
* Make a copy of a dictionary with the copy() method.
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  mydict = thisdict.copy()
  print(mydict)
  ```
* Another way to make a copy is to use the built-in function dict().
  ```python
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  mydict = dict(thisdict)
  print(mydict)
  ```
## Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
```python
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
```
