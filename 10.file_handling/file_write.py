f = open("vedant.txt", "a")
f.write("Now vedant is written !")
f.close()

#open and read the file after the appending:
f = open("vedant.txt", "r")
print(f.read())