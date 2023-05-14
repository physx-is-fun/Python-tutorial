# Data types

Python Data Types are used to define the type of a variable. It defines what type of data we are going to store in a variable. The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various built-in data types which we will discuss with in this tutorial:

    Numeric - int, float, complex
    String - str
    Sequence - list, tuple, range
    Binary - bytes, bytearray, memoryview
    Mapping - dict
    Boolean - bool
    Set - set, frozenset
    None - NoneType

## Python Numeric Data Type

Python numeric data types store numeric values. Number objects are created when you assign a value to them. Python supports four different numerical types:

    int (signed integers)
    long (long integers, they can also be represented in octal and hexadecimal)
    float (floating point real values)
    complex (complex numbers)

Python allows you to use a lowercase l with long, but it is recommended that you use only an uppercase L to avoid confusion with the number 1. Python displays long integers with an uppercase L. A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are the real numbers and j is the imaginary unit.

## Python String Data Type

Python Strings are identified as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end. The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator in Python.

## Python List Data Type

Python Lists are the most versatile compound data types. A Python list contains items separated by commas and enclosed within square brackets ([]). To some extent, Python lists are similar to arrays in C. One difference between them is that all the items belonging to a Python list can be of different data type where as C array can store elements related to a particular data type. The values stored in a Python list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.

## Python Tuple Data Type

Python tuple is another sequence data type that is similar to a list. A Python tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses. The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

## Python Dictionary

Python dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object. Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). Python dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.

## Python Boolean Data Types

Python boolean type is one of built-in data types which represents one of the two values either True or False. Python bool() function allows you to evaluate the value of any expression and returns either True or False based on the expression.

## Python Data Type Conversion

Sometimes, you may need to perform conversions between the built-in data types. To convert data between different Python data types, you simply use the type name as a function.

## Data Type Conversion Functions

There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

    int(x [,base]) - Converts x to an integer. base specifies the base if x is a string.
    long(x [,base] ) - Converts x to a long integer. base specifies the base if x is a string.
    float(x) - Converts x to a floating-point number.
    complex(real [,imag]) - Creates a complex number.
    str(x) - Converts object x to a string representation.
    repr(x) - Converts object x to an expression string.
    eval(str) - Evaluates a string and returns an object.
    tuple(s) - Converts s to a tuple.
    list(s) - Converts s to a list.
    set(s) - Converts s to a set.
    dict(d) - Creates a dictionary. d must be a sequence of (key,value) tuples.
    frozenset(s) - Converts s to a frozen set.
    chr(x) - Converts an integer to a character.
    unichr(x) - Converts an integer to a Unicode character.
    ord(x) - Converts a single character to its integer value.
    hex(x) - Converts an integer to a hexadecimal string.
    oct(x) - Converts an integer to an octal string.

## Bibliography

Python - Data Types. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_data_types.htm