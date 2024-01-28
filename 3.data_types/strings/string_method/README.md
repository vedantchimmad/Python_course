# String Methods

---
## Upper case
The upper() method returns the string in upper case
```python
a = "hello vedant"

print(a.upper())
```

## Lower case
The lower() method returns the string in lower case
```python
a = "hello vedant"

print(a.lower())
```
## Capitalize
The capitalize() method returns the string with first character as upper case and rest all are lower case
```python
a = "hello vedant"

print(a.capitalize())
```
## Casefold
The casefold() method returns the string in lower case
```python
a = "hello vedant"

print(a.casefold())
```
>[!NOTE]
> 
> This method is more effective than lower(),It will convert more characters into lower case 

## Center
The center() method will center align the string, using a specified character (space is default) as the fill character.

>Syntax
> 
>*string.center(length, character)*

| Parameter | Description                                                                            |
|-----------|----------------------------------------------------------------------------------------|
| length    | Required. The length of the returned string                                            |
| character | Optional. The character to fill the missing space on each side. Default is " " (space) |
```python
txt = "banana"

x = txt.center(10, "O")

print(x)
```
## count
The count() method returns the number of times a specified value appears in the string.
>Syntax
>
>*string.count(value, start, end)*

| Parameter | Description                                                                            |
|-----------|----------------------------------------------------------------------------------------|
| value     | Required. A String. The string to value to search for                                  |
| start     | Optional. An Integer. The position to start the search. Default is 0                   |
| end       | Optional. An Integer. The position to end the search. Default is the end of the string |
```python
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)
```
## Endswith
The endswith() method returns True if the string ends with the specified value, otherwise False.
>Syntax
>
>*string.endswith(value, start, end)*

| Parameter | Description                                                           |
|-----------|-----------------------------------------------------------------------|
| value     | Required. The value to check if the string ends with                  |
| start     | Optional. An Integer specifying at which position to start the search |
| end       | Optional. An Integer specifying at which position to end the search   |
```python
txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)
```
## find
* The find() method finds the first occurrence of the specified value.

* The find() method returns -1 if the value is not found.

* The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
>Syntax
>
>*string.find(value, start, end)*

| Parameter | Description                                                            |
|-----------|------------------------------------------------------------------------|
| value     | Required. The value to search for                                      |
| start     | Optional. Where to start the search. Default is 0                      |
| end	      | Optional. Where to end the search. Default is to the end of the string |
```python
txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

y = txt.find("e")

print(x)

print(y)
```
## format
* The format() method formats the specified value(s) and insert them inside the string's placeholder.

* The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

* The format() method returns the formatted string.
* The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
>Syntax
>
>*string.format(value1, value2...)*

| Parameter | Description                                                            |
|-----------|------------------------------------------------------------------------|
|value1, value2...    | Required. One or more values that should be formatted and inserted in the string. The values are either a list of values separated by commas, a key=value list, or a combination of both.The values can be of any data type.|
                       
```python
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
txt4 = 25

print(txt1)

print(txt2)

print(txt3)

print(f"my age is {txt4}")
```
## Index
* The index() method finds the first occurrence of the specified value.

* The index() method raises an exception if the value is not found.

* The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
>Syntax
>
>*string.index(value, start, end)*

| Parameter | Description                                                            |
|-----------|------------------------------------------------------------------------|
| value     | Required. The value to search for                                      |
| start     | Optional. Where to start the search. Default is 0                      |
| end	      | 	Optional. Where to end the search. Default is to the end of the string|
```python
txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

y = txt.index("e")

z = txt.find("q")

print(x)

print(y)

print(z)
```
## isalnum
* The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
>Syntax
>
>*string.isalnum()*
```python
txt = "Company 12"

x = txt.isalnum()

print(x)
```
## isalpha
* The isalpha() method returns True if all the characters are alphabet letters (a-z).
>Syntax
>
>*string.isalpha()*
```python
txt = "Company10"

x = txt.isalpha()

print(x)
```
## isascii
* The isascii() method returns True if all the characters are ascii characters  (a-z).
>Syntax
> 
>*string.isascii()*
```python
txt = "Company123"

x = txt.isascii()

print(x)
```
## isdecimal
* The isdecimal() method returns True if all the characters are decimals (0-9).
>Syntax
>
>*string.isdecimal()*
```python
txt = "1234"

x = txt.isdecimal()

print(x)
```
## isdigit
* The isdigit() method returns True if all the characters are digits, otherwise False.
>Syntax
>
>*string.isdecimal()*
```python
txt = "50800"

x = txt.isdigit()

print(x)
```
## isidentifier
* The isidentifier() method returns True if the string is a valid identifier, otherwise False.

* A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
> Syntax
>
>*string.isdecimal()*
```python
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
```
## islower
* The islower() method returns True if all the characters are in lower case, otherwise False.
* Numbers, symbols and spaces are not checked, only alphabet characters.
> Syntax
>
>*string.islower()*
```python
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())
```
## islower
* The islower() method returns True if all the characters are in lower case, otherwise False.
* Numbers, symbols and spaces are not checked, only alphabet characters.
> Syntax
>
>*string.islower()*
```python
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())
```
## isnumeric
* The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
* Exponents, like ² and ¾ are also considered to be numeric values.
* "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
>Syntax
> 
>*string.isnumeric()*
```python
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
f = "565543"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
print(f.isnumeric())
```
## isprintable
* The isprintable() method returns True if all the characters are printable, otherwise False.
>Syntax
>
>*string.isprintable()*
```python
txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)
```
## isspace
* The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
>Syntax
>
>*string.isspace()*
```python
txt = "   s   "

x = txt.isspace()

print(x)
```
## istitle
* The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
>Syntax
> 
>*string.istitle()*
```python
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
```
## isupper
* The isupper() method returns True if all the characters are in upper case, otherwise False.
>Syntax
>
>*string.isupper()*
```python
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())
```
## join
* The join() method takes all items in an iterable and joins them into one string.
>Syntax
>
>*string.join(iterable)*

| Parameter | Description                                                              |
|-----------|--------------------------------------------------------------------------|
| iterable  | 	Required. Any iterable object where all the returned values are strings |
```python
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
```
## ljust
* The ljust() method will left align the string, using a specified character (space is default) as the fill character.
>Syntax
>
>*string.ljust(length, character)*

| Parameter  | Description                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------|
| length     | 	Required. The length of the returned string                                                          |
| character  | Optional. A character to fill the missing space (to the right of the string). Default is " " (space). |
```python
txt = "banana"
txt1 = "banana"

x = txt.ljust(20)
y = txt1.ljust(20,"0")

print(x, "is my favorite fruit.")
print(y)
```
## lstrip
* The lstrip() method removes any leading characters (space is the default leading character to remove)
>Syntax
>
>*string.lstrip(characters)*

| Parameter  | Description                                                    |
|------------|----------------------------------------------------------------|
| character  | Optional. A set of characters to remove as leading characters  |
```python
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
```
## partition
* The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

* The first element contains the part before the specified string.

* The second element contains the specified string.

* The third element contains the part after the string.
>Syntax
> 
>*string.partition(value)*

| Parameter | Description                         |
|-----------|-------------------------------------|
| value     | Required. The string to search for  |
```python
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
```
## replace
* The replace() method replaces a specified phrase with another specified phrase.
>Syntax
>
>*string.replace(oldvalue, newvalue, count)*

| Parameter | Description                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------|
| value     | Required. The string to search for                                                                                  |
| newvalue  | Required. The string to search for                                                                                  |
| count     | Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences |
```python
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
```
## split
* The split() method splits a string into a list.
>Syntax
>
>*string.split(separator, maxsplit)*

| Parameter | Description                                                                                                      |
|-----------|------------------------------------------------------------------------------------------------------------------|
| separator     | Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator     |                                                                       
| maxsplit  | Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"                       |                                                                             
```python
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)
```
## splitlines
* The splitlines() method splits a string into a list. The splitting is done at line breaks.
>Syntax
>
>*string.splitlines(keeplinebreaks)*

| Parameter      | Description                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------------------|
| keeplinebreaks | Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False |
```python
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
```
## startswith
* The startswith() method returns True if the string starts with the specified value, otherwise False.
>Syntax
>
>*string.startswith(value, start, end)*

| Parameter | Description                                                           |
|-----------|-----------------------------------------------------------------------|
| value     | Required. The value to check if the string starts with                |
| start     | Optional. An Integer specifying at which position to start the search |
| end       | Optional. An Integer specifying at which position to end the search   |
```python
txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)
```
## strip
* The strip() method removes any leading, and trailing whitespaces.
* Leading means at the beginning of the string, trailing means at the end.
* You can specify which character(s) to remove, if not, any whitespaces will be removed.
>Syntax
> 
>*string.strip(characters)*

| Parameter | Description                                                           |
|-----------|-----------------------------------------------------------------------|
| value     | Optional. A set of characters to remove as leading/trailing characters               |
```python
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
```
## swapcase
* The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
>Syntax
>
>*string.swapcase()*
```python
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
```
## title
* The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
>Syntax
>
>*string.title()*
```python
txt = "Welcome to my 2nd world"

x = txt.title()

print(x)
```