x = 5

# returns True because 5 is greater than 3 AND 5 is less than 10
print(x > 3 and x < 10)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print(x > 3 or x < 4)

# returns False because not is used to reverse the result
print(not(x > 3 and x < 10))