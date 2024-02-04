# Built-in functions

---
## abs
The abs() function returns the absolute value of the specified number.

>Syntax
> 
>*abs(n)*

| Parameter | Description                  |
|-----------|------------------------------|
| n         | Required. A number           |

```python
x = abs(-7.25)
```
## all
* The all() function returns True if all items in an iterable are true, otherwise it returns False.
* If the iterable object is empty, the all() function also returns True.

>Syntax
> 
>*all(iterable)*

| Parameter | Description                                  |
|-----------|----------------------------------------------|
| iterable  | An iterable object (list, tuple, dictionary) |

```python
mylist = [0, 1, 1]
x = all(mylist)
```
## any
* The any() function returns True if any item in an iterable are true, otherwise it returns False.

* If the iterable object is empty, the any() function will return False.
>Syntax
> 
>*any(iterable)*

| Parameter | Description                                  |
|-----------|----------------------------------------------|
| iterable  | An iterable object (list, tuple, dictionary) |

```python
mytuple = (0, 1, False)
x = any(mytuple)

print(x)
```
## bin
* The bin() function returns the binary version of a specified integer.

* The result will always start with the prefix 0b.
>Syntax
> 
>*bin(n)*

| Parameter | Description            |
|-----------|------------------------|
| n         | Required. An integer   |

```python
x = bin(36)

print(x)
```
## chr
* The chr() function returns the character that represents the specified unicode.

>Syntax
> 
>*chr(number)*

| Parameter | Description                                        |
|-----------|----------------------------------------------------|
| number    | An integer representing a valid Unicode code point |

```python
x = chr(97)

print(x)
```
## filter
The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

>Syntax
> 
>*filter(function, iterable)*

| Parameter | Description                                        |
|-----------|----------------------------------------------------|
| function  | A Function to be run for each item in the iterable |
| iterable  | The iterable to be filtered                        |
```python
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
```
## input
The input() function allows user input.

>Syntax
> 
>*input(prompt)*

| Parameter | Description                                                |
|-----------|------------------------------------------------------------|
| prompt    | A String, representing a default message before the input. |

```python
print('Enter your name:')
x = input()
print('Hello, ' + x)
```
## len
* The len() function returns the number of items in an object.

* When the object is a string, the len() function returns the number of characters in the string.
>Syntax
> 
>*len(object)*

| Parameter | Description                                               |
|-----------|-----------------------------------------------------------|
| object    | Required. An object. Must be a sequence or a collection   |

```python
mylist = ["apple", "orange", "cherry"]

x = len(mylist)

print(x)
```
## map
* The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

>Syntax
> 
>*map(function, iterables)*

| Parameter  | Description                                                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| function   | Required. The function to execute for each item                                                                                                                      |
| iterables  | Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable. |

```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
```
## max
* The max() function returns the item with the highest value, or the item with the highest value in an iterable.
* If the values are strings, an alpha betically comparison is done.
>Syntax
> 
>*max(iterable)*

| Parameter  | Description                                   |
|------------|-----------------------------------------------|
| iterable   | An iterable, with one or more items to compare|

```python
a = (1, 5, 3, 9)
x = max(a)

print(x)
```
## min
* The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
* If the values are strings, an alpha betically comparison is done.
>Syntax
> 
>*min(iterable)*

| Parameter  | Description                                   |
|------------|-----------------------------------------------|
| iterable   | An iterable, with one or more items to compare|

```python
a = (1, 5, 3, 9)
x = min(a)

print(x)
```
## iter
* The iter() function returns an iterator object.

>Syntax
> 
>*iter(object, sentinel)*

| Parameter | Description                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------|
| object    | Required. An iterable object                                                                                              |
| sentinel  | Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel  |

```python
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
```
## next
* The next() function returns the next item in an iterator.
* You can add a default return value, to return if the iterable has reached to its end.

>Syntax
> 
>*next(iterable, default)*

| Parameter | Description                                                                   |
|-----------|-------------------------------------------------------------------------------|
| iterable  | Required. An iterable object.                                                 |
| default   | Optional. An default value to return if the iterable has reached to its end.  |

```python
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
```
## open
* The open() function opens a file, and returns it as a file object.
* Read more about file handling in our chapters about File Handling.

>Syntax
> 
>*open(file, mode)*

| Parameter                                                                                 | Description                                                                   |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| file                                                                                      | The path and name of the file                                                |
| mode                                                                                      | A string, define which mode you want to open the file in : |

```
"r" - Read - Default value. Opens a file for reading, error if the file does not exist 

"a" - Append - Opens a file for appending, creates the file if it does not exist|

"w" - Write - Opens a file for writing, creates the file if it does not exist|

"x" - Create - Creates the specified file, returns an error if the file exist```|

In addition you can specify if the file should be handled as binary or text mode|

"t" - Text - Default value. Text mode|

"b" - Binary - Binary mode (e.g. images)
```

```python
f = open("vedant.txt", "r")
print(f.read())
```
## power
* The pow() function returns the value of x to the power of y (xy).

* If a third parameter is present, it returns x to the power of y, modulus z.
>Syntax
> 
>*pow(x, y, z)*

| Parameter | Description                     |
|-----------|---------------------------------|
| x         | A number, the base              |
| y         | A number, the exponent.         |
| z         | Optional. A number, the modulus |

```python
# Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5)
x = pow(4, 3, 5)

print(x)
```
## range
* The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
>Syntax
> 
>*range(start, stop, step)*

| Parameter | Description                                                                      |
|-----------|----------------------------------------------------------------------------------|
| start     | Optional. An integer number specifying at which position to start. Default is 0  |
| stop      | Required. An integer number specifying at which position to stop (not included). |
| step      | Optional. An integer number specifying the incrementation. Default is 1          |

```python
x = range(3, 20, 2)

for n in x:
  print(n)
```
## reversed
* TThe reversed() function returns a reversed iterator object.
>Syntax
> 
>*reversed(sequence)*

| Parameter | Description                    |
|-----------|--------------------------------|
| sequence  | Required. Any iterable object  |


```python
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)
```
## round
* The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
* The default number of decimals is 0, meaning that the function will return the nearest integer.
>Syntax
> 
>*round(number, digits)*

| Parameter  | Description                                                                    |
|------------|--------------------------------------------------------------------------------|
| number     | Required. The number to be rounded                                             |
| digits     | Optional. The number of decimals to use when rounding the number. Default is 0 |

```python
x = round(5.76543, 2)
print(x)
```
## slice
* The slice() function returns a slice object.
* A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.

>Syntax
> 
>*slice(start, stop, step)*

| Parameter | Description                                                                                 |
|-----------|---------------------------------------------------------------------------------------------|
| start     | Optional. An integer number specifying at which position to start the slicing. Default is 0 |
| stop      | An integer number specifying at which position to end the slicing                           |
| step      | Optional. An integer number specifying the step of the slicing. Default is 1                |

```python
a = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(0, 8, 3)

print(a[x])
```
## sorted
* The sorted() function returns a sorted list of the specified iterable object.
* You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
>[!NOTE]
> 
> You cannot sort a list that contains BOTH string values AND numeric values.

>Syntax
> 
>*sorted(iterable, key=key, reverse=reverse)*

| Parameter  | Description                                                                                 |
|------------|---------------------------------------------------------------------------------------------|
| iterable   | Required. The sequence to sort, list, dictionary, tuple etc.                                |
| key        | Optional. A Function to execute to decide the order. Default is None                        |
| reverse    | Optional. A Boolean. False will sort ascending, True will sort descending. Default is False |

```python
a = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(0, 8, 3)

print(a[x])
```
## sum
* The sum() function returns a number, the sum of all items in an iterable.
>Syntax
> 
>*sum(iterable, start)

| Parameter | Description                                         |
|-----------|-----------------------------------------------------|
| iterable  | Required. The sequence to sum                       |
| start     | Optional. A value that is added to the return value |


```python
a = (1, 2, 3, 4, 5)
x = sum(a)

print(x)
```
## Super
* The super() function is used to give access to methods and properties of a parent or sibling class.
* The super() function returns an object that represents the parent class.
>Syntax
> 
>*super()*

```python
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()
```
## zip
* The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
* If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.

>Syntax
> 
>*zip(iterator1, iterator2, iterator3 ...)*

| Parameter                           | Description                                          |
|-------------------------------------|------------------------------------------------------|
| iterable1, iterable2, iterable3 ... | Iterable objects that will be joined together        |
```python
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))
```