# File: homework1.py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters in quotation marks

e = [1,2,3]
print(e)
print(type(e)) # e is a list, a sequence of characters separated by commas enclosed in brackets

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a data structure that holds a key which corresponds to a value

g = (1, 2)
print(g)
print(type(f)) # g is a tuple, an immutable list

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a dictionary, the same as e

i = True
print(i)
print(type(i)) # i is a boolean, a True or False value

j = None
print(j)
print(type(j)) # j is a NoneType, an object that has no value

k = ["True", "blue", 12]
print(k)
print(type(k)) # k is a list

l = str(14)
print(l)
print(type(l)) # l is a list

m = 1e4
print(m)
print(type(m)) # m is a float

# Questions #

# 1) There are 8 different data types

# 2) Integer, Float, Complex, String, List, Dictionary, Tuple, Boolean, NoneType

# 3) String: d, l | List: e, h, k | Float: b, m

# 4) l is a string because str() converts anything inside the paranthesis into a string

q5 = range(5)
print(q5)
print(type(q5)) # q5 is a range, which outputs a list from 0 to n-1 (where n is the number inside the paranthesis)

# --- Booleans ---

10 > 9 # True
10 == 9 # False
10 <= 9 # False
bool("abc") # True
bool(123) # True
bool(["apple", "cherry", "banana"]) # True
bool(True) # True
bool(False) # False
bool(0) # False
bool("") # False
bool(" ") # True
bool(()) # False
bool([]) # False
bool({}) # False
bool(True and False) # False
bool(True and True) # True
bool(False and False) # False
bool(True or False) # True
bool(True or True) # True
bool(False or False) # False
bool(not(False)) # True
bool(not(True)) # False

# Questions #

# 1) I noticed that if there's a value (besides 0) then it's True

# 2) False and False

# 3) bool(-1) is True because -1 is a value

# 4) bool({}) is False because it's an empty dictionary, which has no value

# --- Operators ---

10 + 5 # 15, + performs addition
10 - 5 # 5, - performs subtraction
2 * 4 # 8, * performs multiplication
6 / 3 # 2.0, / performs division (returns a float)
5 % 2 # 1, % performs modulo
3 ** 2 # 9, ** performs exponentiation
15 // 2 # 7, // performs floor division

5 == 2 # False, == performs equality comparison
10 != 10 # False, != performs inequality comparison
2 < 5 # True, < performs less than comparison
12 > 5 # True, > performs greater than comparison
5 <= 6 # True, <= performs less than or equal to comparison
1 >= 10 # False, >= performs greater than or equal to comparison

x = 5
x += 5 # x is now 10, += adds the value to the variable and assigns it to the variable
x -= 4 # x is now 6, -= subtracts the value from the variable and assigns it to the variable
x *= 3 # x is now 18, *= multiplies the variable by the value and assigns it to the variable

# Questions #

# 1) The and operator returns True if both statements are true
    #For example, 5 > 3 and 10 > 7 is True because both statements are true
    #However, 5 > 3 and 10 < 7 is False because the second statement is false

# 2)The or operator returns True if at least one statement is true
    #For example, 5 > 3 or 10 < 7 is True because the first statement is true
    #However, 5 < 3 or 10 < 7 is False because both statements are false

# 3) The not operator returns the opposite of the statement
    #For example, not(5 > 3) is False because 5 > 3 is True, so the opposite is False
    #However, not(5 < 3) is True because 5 < 3 is False, so the opposite is True

# More Questions #

# 1) The difference between / and // is that / returns a float while // returns an integer (the floor of the division)

# 2) The difference between % and // is that % returns the remainder of the division while // returns the floor of the division

# 3) I would use the % operator, for example 10%3 would return 1, which is the remainder of the division of 10 by 3

# 4) Assignment operators are used to assign values to variables

# --- Strings ---

my_string = "hello"
print(my_string) # prints the string "hello"
print(my_string[0]) # prints the first character of the string, which is "h"
print(my_string[1]) # prints the second character of the string, which is "e"
print(my_string[2]) # prints the third character of the string, which is "l
print(my_string[3]) # prints the fourth character of the string, which is "l"
print(my_string[4]) # prints the fifth character of the string, which is "o"
print(my_string[-1]) # prints the last character of the string, which is "o"
print(my_string[1:3]) # prints the characters from index 1 to index 2 (not including index 3), which is "el"
print(my_string[0:5:2]) # prints the characters from index 0 to index 4 (not including index 5) with a step of 2, which is "hlo"
print(len(my_string)) # prints the length of the string, which is 5
print(my_string + "goodbye") # concatenates the string "hello" with the string "goodbye", which is "hellogoodbye"
print(my_string * 7) # repeats the string "hello" 7 times, which is "hellohellohello"

# Questions #

# 1) Slicing is a way to extract a portion of a string by specifying the start and end indices. We sliced the string in mutations 8 and 9

# 2)
name = "Oski"
print("Hello, my name is", name) # prints "Hello, my name is Oski"

# 3)
name = "Oski"
print(f"Hello, my name is {name}") # prints "Hello, my name is Oski" using an f-string

# 4) The difference bewteen examples 2 and 3 is that example 2 uses string concatenation to combine the string "Hello, my name is" with the variable name, while example 3 uses an f-string to embed the variable name directly into the string. The f-string is more concise and easier to read.

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another.
# Example: cd Desktop

# ls
# Lists the contents of the current directory. Use it to see what files and folders are in the current directory.
# Example: ls

# ls -a
# Lists all the contents of the current directory, including hidden files. Use it to see all files and folders in the current directory, including those that are hidden.
# Example: ls -a

# mkdir
# Makes a new directory. Use it to create a new folder.
# Example: mkdir new_folder

# cat
# Concatenates and prints the contents of a file. Use it to read the contents of a file.
# Example: cat file.txt

# pwd
# Prints the current working directory. Use it to see where you are in the file system.
# Example: pwd

# cd ..
# Changes to the parent directory. Use it to move up one level in the directory structure.
# Example: cd ..

# cd .
# Changes to the current directory. Use it to stay in the same directory.
# Example: cd .

# cd ~
# Changes to the home directory. Use it to quickly navigate to your home directory.
# Example: cd ~

# cp
# Copies a file or directory. Use it to create a copy of a file or folder.
# Example: cp file.txt copy_of_file.txt

# mv
# Moves a file or directory. Use it to move a file or folder to a new location
# Example: mv file.txt new_folder/file.txt

# rm
# Removes a file or directory. Use it to delete a file or folder.
# Example: rm file.txt

# clear
# Clears the terminal screen. Use it to clear the terminal of all previous commands and outputs.
# Example: clear

# grep
# Searches for a specific pattern in a file. Use it to find specific text within a file.
# Example: grep "search term" file.txt

# Questions #

# 1) 3 commands not present are touch (creates a new empty file), rmdir (removes an empty directory), and echo (prints a line of text to the terminal).

# 2) The difference between ls and ls -a is that ls lists only the visible files and directories in the current directory, while ls -a lists all files and directories, including hidden ones (those that start with a dot).

# 3) A hidden file is a file that is not visible in the terminal by default. Hidden files typically start with a dot (.) in their name, which is why they are not shown when using the ls command without the -a option.

# 4) 3 other flags are -l (long listing format, which shows detailed information about each file), -h (human-readable file sizes, which makes it easier to understand the size of files), and -R (recursive listing, which lists all files and directories in the current directory and all subdirectories).
