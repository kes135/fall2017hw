Exercise 1 - Testing your knowledge of command line programs
What is the benefit of executing a program from the command line as opposed to running it from within an editor like Jupyter or Spyder.
Because a command line interface requires unique commands, this interface is often more difficult to learn because of the need to memorize dozens of different commands. However, a command line operating system can be a very valuable resource and should not be ignored. For example, users who have Microsoft Windows may find trivial tasks, such as renaming 100+ files in a folder, a very difficult task. However, renaming 100+ files in a directory can be done in less than a minute with a command entered into the command line.
Text interface with menus

- A text interface can be made easier to navigate using menus created with text and ASCII extended characters. 
For example, many command line text editors have some type of interface with menus and shortcut keys that make 
navigating the file being edited easier.



Name a Python library that you would use in order to pass arguments from the command line.
import os
class shell_cmd(cmd.Cmd,object):
    def do_shell(self, s):
        os.system(s)
    def help_shell(self):
        print "execute shell commands"

shell.py





Exercise 2 - Creating and executing a command line program
Write a Python program that gets two numbers from the user and displays the sum of the two numbers. Make sure to make this program a .py file, something you can run from the command line.
Note:
You can use the %%writeline magic command in Jupyter to create this file, or you can simply use an external editor to create this file. Please refer to classwork in Github for examples.
In [ ]:
def sum(x,y):
    ans = x+y
    return x+y
    

def avg(x,y):
    avge = sum(x,y)/2
    average = int(avge)
    print("Sum of the given two numbers is:", sum(x,y))
    print("Average of the given numbers is:", average)    
    
num1 = int(input("Enter first number:"))
a = num1
num2 = int(input("Enter second number:"))
b = num2

sum(a,b)
avg(a,b)

avgenum.py







Exercise 3 - Accepting arguments from the command line
Repeat the command line program above, however, this time, instead of accepting the numbers from the user using raw_input, pass in the two numbers as command line arguments.
Note You can use sys.argv or argparse, whichever you are more comfortable with.
In [ ]:
def sum(x,y):
    ans = x+y
    return x+y
    

def avg(x,y):
    avge = sum(x,y)/2
    average = int(avge)
    print("Sum of the given two numbers is:10", sum(x,y))
    print("Average of the given numbers is:20", average)    
    
num1 = int(input("Enter first number:10"))
a = num1
num2 = int(input("Enter second number:20"))
b = num2

sum(a,b)
avg(a,b)


   
### END CODE
Exercise 4 - Command Line programs with multiple modules
This is also an extension to Exercises 2 and 3.
Write a Python program to add two numbers. Your Python program must have a function called add that is placed in a separate module called helper.py. Your main program, which is also a standalone Python program main.py must import helper.py and use this module to add the two numbers.
The numbers to be added must be passed via the command line.
Here is an example of how your program would be invoked assuming the numbers to be added are 3 and 2
python main.py 3 2
In [ ]:

python main.py 3.2

num1 = 1.5

num2 = 6.3



# Add two numbers

sum = float(num1) + float(num2)



# Display the sum

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))











### END CODE
Exercise 5 - Python program with multiple modules to sort a list of numbers
Write a Python program to sort a list of numbers in ascending order. Your Python program must have a function called sortNumbers that is placed in a separate module called sorthelper.py. This function sortNumbers accepts a list of numbers. Your main program, which is also a standalone Python program main.py must import sorthelper.py and use this module to sort the numbers.
The numbers to be sorted must be passed via the command line.
Here is an example of how your program would be invoked assuming the numbers to be sorted are 5 4 3 and 8
python main.py 5 4 3 8
In [ ]:

python main.py 5 4 3 8

data_list = [3,4,5,8]
new_list = [0,0,0,0]

while data_list:
    minimum = data_list[4]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    sort#s()
    new_list.append(minimum)
    data_list.remove(minimum)    

print new_list

