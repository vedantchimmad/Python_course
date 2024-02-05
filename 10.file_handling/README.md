# File Handling

---
The key function for working with files in Python is the `open()` function.
* The `open()` function takes two parameters; filename, and mode.
   There are four different methods (modes) for opening a file
   * `"r"` - Read - Default value. Opens a file for reading, error if the file does not exist

   * `"a"` - Append - Opens a file for appending, creates the file if it does not exist

   * `"w"` - Write - Opens a file for writing, creates the file if it does not exist

   * `"x" `- Create - Creates the specified file, returns an error if the file exists
  
  In addition you can specify if the file should be handled as binary or text mode
   * `"t"` - Text - Default value. Text mode

   * `"b"` - Binary - Binary mode (e.g. images)
### Open a File
To open a file for reading it is enough to specify the name of the file
```python
f = open("open.txt")
```
If the file is located in a different location, you will have to specify the file path, like this
```python
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
```
### Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return.
```python
f = open("open.txt", "r")
print(f.read(5))
```
### Read Lines
You can return one line by using the `readline()` method
```python
f = open("demofile.txt", "r")
print(f.readline())
```
### Close Files
It is a good practice to always close the file when you are done with it.
```python
f = open("open.txt", "r")
print(f.readline())
f.close()
```
### File Write
To write to an existing file, you must add a parameter to the `open()` function
* `"a"` - Append - will append to the end of the file

* `"w"` - Write - will overwrite any existing content
```python
f = open("vedant.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("vedant.txt", "r")
print(f.read())
```
### Create a New File
To create a new file in Python, use the `open()` method, with one of the following parameters

`"x"` - Create - will create a file, returns an error if the file exist
```python
f = open("myfile.txt", "x")
```
### Delete a File
To delete a file, you must import the `OS` module, and run its `os.remove()` function
```python
import os
os.remove("demofile.txt")
```
```python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```
### Delete Folder
To delete an entire folder, use the `os.rmdir()` method.
```python
import os
os.rmdir("myfolder")
```