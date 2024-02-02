# Dictionary Metho

---
## clear
The clear() method removes all the elements from a dictionary.
> Syntax
>
> dictionary.clear()

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.clear()

print(car)
```
## copy
The copy() method returns a copy of the specified dictionary.
> Syntax
>
> dictionary.copy()

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.copy()

print(x)
```
## fromkeys
The fromkeys() method returns a dictionary with the specified keys and the specified value.
>Syntax
>
> dict.fromkeys(keys, value)

| Parameter | Description                                                      |
|-----------|------------------------------------------------------------------|
| keys      | Required. An iterable specifying the keys of the new dictionary  |
| value     | Optional. The value for all keys. Default value is None          |

```python
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
```
## get
The get() method returns the value of the item with the specified key.
>Syntax
>
> dictionary.get(keyname, value)

| Parameter | Description                                                      |
|-----------|------------------------------------------------------------------|
| keyname   | Required. The keyname of the item you want to return the value from |
| value     | Optional. A value to return if the specified key does not exist.Default value None         |

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)
```
## items
The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
>Syntax
>
> dictionary.items()

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)
```
## keys
TThe keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
>Syntax
>
> dictionary.keys()

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)
```
## pop
The pop() method removes the specified item from the dictionary.
>Syntax
>
> dictionary.pop(keyname, defaultvalue)

| Parameter | Description                                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| keyname   | Required. The keyname of the item you want to remove                                                                                                                  |
| value     | Optional. A value to return if the specified key do not exist.If this parameter is not specified, and the no item with the specified key is found, an error is raised |
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.pop("model")

print(x)
```
## popitem
The popitem() method removes the item that was last inserted into the dictionary.
>Syntax
>
> dictionary.popitem()

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.popitem()

print(x)
```
## setdefault
The setdefault() method returns the value of the item with the specified key.
>Syntax
>
> dictionary.setdefault(keyname, value)

| Parameter | Description                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| keyname   | Required. The keyname of the item you want to return the value from                                                                      |
| value     | Optional.If the key exist, this parameter has no effect.If the key does not exist, this value becomes the key's valueDefault value None  |
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("color", "white")

print(x)
```
## update
The update() method inserts the specified items to the dictionary.
>Syntax
>
>dictionary.update(iterable)

| Parameter | Description                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| keyname   | A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary                                         |
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.update({"color": "White"})

print(car)
```
## values
The values() method returns a view object. The view object contains the values of the dictionary, as a list.
>Syntax
>
> dictionary.values()

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)
```