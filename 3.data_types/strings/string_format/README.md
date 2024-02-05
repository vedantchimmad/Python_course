# String format

---
* To make sure a string will display as expected, we can format the result with the `format()` method.
* The `format()` method allows you to format selected parts of a string.
```python
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
```
### Multiple Values
If you want to use more values, just add more values to the format() method.
```python
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```
### Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders
```python
age = 25
name = "Vedant"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
```
### Named Indexes
You can also use named indexes by entering a name inside the curly brackets `{carname}`, but then you must use names when you pass the parameter values `txt.format(carname = "Ford")`
```python
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
```


