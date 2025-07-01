# Python

---

## 💻 What is Software?

### 🧠 Definition

**Software** is a set of **instructions, programs, or data** used to operate computers and perform specific tasks.

It tells the hardware **what to do and how to do it**.

---

### 🧩 Types of Software

#### 1. **System Software**
- Controls and manages computer hardware
- Acts as a bridge between hardware and user applications

| Example              | Description                         |
|----------------------|-------------------------------------|
| Operating System     | Manages hardware and system tasks   |
| Device Drivers       | Enables communication with devices  |
| Utilities            | Performs maintenance tasks          |

---

#### 2. **Application Software**
- Performs specific tasks for the user

| Example              | Description                         |
|----------------------|-------------------------------------|
| MS Word, Excel       | Document creation and editing       |
| Browsers (Chrome)    | Internet browsing                   |
| Games, Media Players | Entertainment                       |

---

#### 3. **Programming Software**
- Tools used by developers to write and test code

| Example              | Description                         |
|----------------------|-------------------------------------|
| Compilers            | Convert code to machine language    |
| Text Editors         | Write source code (e.g. VS Code)    |
| Debuggers            | Help fix code issues                |

---

#### 4. **Middleware**
- Connects different software applications or systems
- Example: Communication between database and web server

---

### 🏗️ Software vs Hardware

| Feature        | Software                       | Hardware                       |
|----------------|--------------------------------|--------------------------------|
| Nature         | Intangible (not physical)      | Tangible (physical parts)      |
| Function       | Provides instructions          | Executes instructions          |
| Examples       | OS, Apps, Games                | CPU, RAM, Keyboard, Monitor    |

---

### 🔄 How Software Works

1. User interacts with **Application Software**
2. Application talks to **System Software**
3. System Software controls the **Hardware**
4. Output is delivered back to the user

---

### 🛠️ Examples of Software

| Category             | Software Name              |
|----------------------|----------------------------|
| Operating System     | Windows, Linux, macOS      |
| Office Suite         | MS Office, Google Docs     |
| Web Browsers         | Chrome, Firefox            |
| Development Tools    | Python, Git, Visual Studio |
| Database Software    | MySQL, PostgreSQL          |

---
## 🧾 What is a Program?

### 📘 Definition

A **program** is a **sequence of instructions written in a programming language** that a computer can understand and execute to perform a specific task or solve a problem.

It acts as a **communication bridge** between the user and the computer hardware.



### 🧠 Key Features

| Feature         | Description                                             |
|-----------------|---------------------------------------------------------|
| Language        | Written in languages like Python, Java, C++, etc.       |
| Execution       | Can be compiled or interpreted to run on a machine      |
| Purpose         | Automate tasks, solve problems, control hardware        |
| Structure       | Includes variables, logic, loops, conditions, and I/O   |

---

## 🧰 Example: Python Program

```python
# Program to calculate the sum of two numbers
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)  # Output: Sum: 15
```

## 💻 What is Programming?

### 📘 Definition

**Programming** is the process of **writing instructions (code)** that a computer can understand and execute to perform a specific task.

It involves using a **programming language** to create **software, applications, scripts**, or systems that solve problems or automate processes.

### 🔑 Key Concepts in Programming

| Concept                  | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| **Code**                 | Instructions written by the programmer                       |
| **Syntax**               | Rules of the programming language                            |
| **Logic**                | Sequence of operations that define what the program does     |
| **Compiler/Interpreter** | Translates code into machine-readable form                   |
| **Bug**                  | An error or flaw in the program                              |

---

## 🧰 Example: A Simple Python Program

```python
# Program to check if a number is even or odd
num = 6
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
    
## History
The implementation of Python was started in the December 1989 by Guido Van Rossum at CWI in
Netherland.
* In February 1991, van Rossum published the code (labeled version 0.9.0).
* In 1994, Python 1.0 was released with new features like: lambda, map, filter, and reduce.
* Python 2.0 added new features like: list comprehensions, garbage collection system.
* On December 3, 2008, Python 3.0 (also called "Py3K") was released.

## What is Python
Python is high level,general-purpose,Structure and object-oriented, simple,dynamic type programming language

## What can python do
* TO create desktop application
* Web application
* Data science
* Game development
* Machine learning
* AI

## Features of python
* Python works on different platforms
* open source and free
* Python has simple syntax similar to the english language,easy to code and easy to understand
* Python runs on **interpreter system** meaning code can be executed as soon as it is written
* Object-oriented approach
* Highly portable
* Large standard library 
* dynamically-typed

## Python Indentation
* space at the beginning of a code line 
* Python uses indentation to indicate block of code

  >[!NOTE]
  >
  > In other language indentation is just for readability but in python it's important

## Comments in python
 
### Uses
* Comments can be used to explain code
* Used to make code more readable
* Used to prevent when execution

  ### 1.Single line comment
  * Comments start with A #
  ```python
   # this is single line comment
   print("Hello world!")
  ```
  ### 2.Multi line comment
  * Python really doesn't have a syntax for multiline comment
  * To add a multiline need to insert # for each line
  ```python
  '''
  This is multi line comment
  '''
  print("Hello world!")
  ```

  >[!NOTE]
  >
  > Since python will ignore string literals that are not assigned to a variable
## keywords
Reserved words in python Language that can not be used as a variable name, function name, or any other identifier.

Example : and, as, or, false etc
```python
import keyword

print(keyword.kwlist)
```

# User Input

---
* In python we can ask the user for input.

* uses the `input()` method.
```python
username = input("Enter username:")
print("Username is: " + username)
```
* Python stops executing when it comes to the input() function, and continues when the user has given some input.