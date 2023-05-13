# Comments

Python comments are programmer-readable explanation or annotations in the Python source code. They are added with the purpose of making the source code easier for humans to understand, and are ignored by Python interpreter. Comments enhance the readability of the code and help the programmers to understand the code very carefully. Just like most modern languages, Python supports single-line (or end-of-line) and multi-line (block) comments. Python comments are very much similar to the comments available in PHP, BASH and Perl Programming languages. There are three types of comments available in Python

    Single line Comments
    Multiline Comments
    Docstring Comments

## Single Line Comments

A hash sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them. Following is an example of a single line comment in Python

```python
# This is a single line comment in python
print ("Hello, World!") # This is again comment
```

This produces the following result

```console
Hello, World!
```

## Multi-Line Comments

Python does not provide a direct way to comment multiple line. Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments. Following is the example to show the usage of multi-line comments

```python
'''
This is a multiline
comment.
'''
print ("Hello, World!")
```

This produces the following result

```console
Hello, World!
```

## Docstring Comments

Python docstrings provide a convenient way to provide a help documentation with Python modules, functions, classes, and methods. The docstring is then made available via the __doc__ attribute.

```python
def add(a, b):
    """Function to add the value of a and b"""
    return a+b

print(add.__doc__)
```

This produces the following result

```console
Function to add the value of a and b
```

## Bibliography

Python - Comments. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_comments.htm