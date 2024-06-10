# RegEx 

---
RegEx can be used to check if a string contains the specified search pattern.

## RegEx Functions
* ### findall
  The findall() function returns a list containing all matches.
  ```python
  import re

  txt = "The rain in Spain"
  x = re.findall("ai", txt)
  print(x)
  ```
  >[!NOTE]
  > 
  > If no matches are found, an empty list is returned:

* ### search
  The search() function searches the string for a match, and returns a Match object if there is a match.
  ```python
  import re

  txt = "The rain in Spain"
  x = re.search("The", txt)
  print(x)
  ```
  >[!NOTE]
  >
  > f there is more than one match, only the first occurrence of the match will be returned

* ### split
  The split() function returns a list where the string has been split at each match
  ```python
  import re

  txt = "The rain in Spain"
  x = re.split(" ", txt)
  print(x)
  ```
* ### sub
  The sub() function replaces the matches with the text of your choice
  ```python
  import re

  #Replace all white-space characters with the digit "9":

  txt = "The rain in Spain"
  x = re.sub(" ", "9", txt)
  print(x)
  ```
### Match Object
A Match Object is an object containing information about the search and the result.
* #### span
  returns a tuple containing the start-, and end positions of the match.
  ```python
  import re

  #Search for an upper case "S" character in the beginning of a word, and print its position:

  txt = "The rain in Spain"
  x = re.search(r"\bS\w+", txt)
  print(x.span())
  ```
* #### string
   returns the string passed into the function
  ```python
  import re

  txt = "The rain in Spain"
  x = re.search(r"\bS\w+", txt)
  print(x.string)
  ```
* #### group
  returns the part of the string where there was a match
  ```python
  import re

  txt = "The rain in Spain"
  x = re.search("The", txt)
  print(x.group())
  ```
## Metacharacters
Metacharacters are characters with a special meaning

| Character | 	Description                                                            | 	Example       |
|-----------|-------------------------------------------------------------------------|----------------|
| []        | 	A set of characters                                                    | 	"[a-m]"       |   
| \         | Signals a special sequence (can also be used to escape special characters) | 	"\d"          |
| .	        | Any character (except newline character)                                | 	"he..o"       |  
| ^	        | Starts with                                                             | 	"^hello"      |  
| $	        | Ends with                                                               | 	"planet$"     |
| *	        | Zero or more occurrences	                                               | "he.*o"        |
| +	        | One or more occurrences	                                                | "he.+o"        |
| ?	        | Zero or one occurrences	                                                | "he.?o"        |
| {}        | 	Exactly the specified number of occurrences                            | 	"he.{2}o"     |
| or        | 	Either or	"falls                                                       | stays"         | 

## Special Sequences
A special sequence is a \ followed by one of the characters in the list below

| Character | 	Description                                                                                                                                                                                                 | 	Example	          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| \A	       | Returns a match if the specified characters are at the beginning of the string                                                                                                                               | 	"\AThe"           |
| \b        | 	Returns a match where the specified characters are at the beginning or at the end of a word(the "r" in the beginning is making sure that the string is being treated as a "raw string")                     | 	r"\bain",r"ain\b" |
| \B        | 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word(the "r" in the beginning is making sure that the string is being treated as a "raw string")	 | r"\Bain",r"ain\B"  |
| \d	       | Returns a match where the string contains digits (numbers from 0-9)                                                                                                                                          | 	"\d"              |
| \D	       | Returns a match where the string DOES NOT contain digits                                                                                                                                                     | 	"\D"              |
| \s	       | Returns a match where the string contains a white space character                                                                                                                                            | 	"\s"              |
| \S	       | Returns a match where the string DOES NOT contain a white space character                                                                                                                                    | 	"\S"              |
| \w	       | Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)                                                                      |	"\w"|
| \W	       | Returns a match where the string DOES NOT contain any word characters	                                                                                                                                       | "\W"               |
| \Z        | 	Returns a match if the specified characters are at the end of the string                                                                                                                                    |	"Spain\Z"|

## Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning

| Set        | 	Description	                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [arn]      | 	Returns a match where one of the specified characters (a, r, or n) is present                                                         |
| [a-n]      | 	Returns a match for any lower case character, alphabetically between a and n                                                          |
| [^arn]     | 	Returns a match for any character EXCEPT a, r, and n                                                                                  |
| [0123]     | 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present                                                         |
| [0-9]      | 	Returns a match for any digit between 0 and 9                                                                                         |
| [0-5][0-9] | 	Returns a match for any two-digit numbers from 00 and 59                                                                              |
|  [a-zA-Z]  | 	Returns a match for any character alphabetically between a and z, lower case OR upper case                                            |
| [+]        | 	In sets, +, *, .,or, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string |