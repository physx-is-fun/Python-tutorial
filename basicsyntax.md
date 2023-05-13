# Basic syntax

The Python syntax defines a set of rules that are used to create Python statements while writing a Python Program. The Python Programming Language Syntax has many similarities to Perl, C, and Java Programming Languages. However, there are some definite differences between the languages.

Python - Interactive Mode Programming: We can invoke a Python interpreter from command line by typing python at the command prompt as following

```console
$ python
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Here >>> denotes a Python Command Prompt where you can type your commands. Let's type the following text at the Python prompt and press the Enter

```console
>>> print ("Hello, World!")
```

If you are running older version of Python, like Python 2.4.x, then you would need to use print statement without parenthesis as in print "Hello, World!". However in Python version 3.x, this produces the following result

```console
Hello, World!
```

Python - Script Mode Programming: We can invoke the Python interpreter with a script parameter which begins the execution of the script and continues until the script is finished. When the script is finished, the interpreter is no longer active. Let us write a simple Python program in a script which is simple text file. Python files have extension .py. Type the following source code in a test.py file

```python
print ("Hello, World!")
```

We assume that you have Python interpreter path set in PATH variable. Now, let's try to run this program as follows

```console
$ python test.py
```

This produces the following result

```console
Hello, World!
```

Let us try another way to execute a Python script. Here is the modified test.py file

```python
#!/usr/bin/python

print ("Hello, World!")
```

We assume that you have Python interpreter available in /usr/bin directory. Now, try to run this program as follows

```console
$ chmod +x test.py     # This is to make file executable
$./test.py
```

This produces the following result

```console
Hello, World!
```

Python Identifiers: A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9). Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, Manpower and manpower are two different identifiers in Python. Here are naming conventions for Python identifiers
    * Python Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
    * Starting an identifier with a single leading underscore indicates that the identifier is private identifier.
    * Starting an identifier with two leading underscores indicates a strongly private identifier.
    If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

Python Reserved Words: The following list shows the Python keywords. These are reserved words and you cannot use them as constant or variable or any other identifier names. All the Python keywords contain lowercase letters only.
    * and
    * as
    * assert
    * break
    * class
    * continue
    * def
    * del
    * elif
    * else
    * except
    * False
    * finally
    * for
    * from
    * global
    * if
    * import
    * in
    * is
    * lambda
    * None
    * nonlocal
    * not
    * or
    * pass
    * raise
    * return
    * True
    * try
    * while
    * with
    * yeld

## Bibliography

Python - Basic Syntax. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_basic_syntax.htm#