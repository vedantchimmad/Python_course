# A function that returns the length of the value:
def myFunc(e):
    return len(e)

cars = ['Ford','h','Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
