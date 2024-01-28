x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns True because z is the same object as x
print(x is z)

# returns False because x is not the same object as y, even if they have the same content
print(x is y)

print(x is not y)