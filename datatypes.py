# Numeric data types
# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))
# float variable.
b=20.345
print("The type of variable having value", b, " is ", type(b))
# complex variable.
c=10+3j
print("The type of variable having value", c, " is ", type(c))

# String data type
str = 'Hello World!'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# List data type
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# Tuple data type
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

# Dictionary data type
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# Boolean data type
a = True
# display the value of a
print(a)
# display the data type of a
print(type(a))

# Data type conversion
# conversion to int
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("3")   # c will be 3
print (a)
print (b)
print (c)
## conversion to float
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3
print (a)
print (b)
print (c)
# conversion to string
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"
print (a)
print (b)
print (c)

# Python - Data Types. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_data_types.htm