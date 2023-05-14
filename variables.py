# Creating python variables
counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable

# Printing python variables
print (counter)
print (miles)
print (name)

# Deleting python variables
counter2 = 100
print (counter2)
del counter2
print (counter2)

# Multiple assigment
a = b = c = 100
print (a)
print (b)
print (c)

d,e,f = 1,2,"Zara Ali"
print (d)
print (e)
print (f)

# Local variable
def sum(g,h):
   sum = g + h
   return sum
print(sum(5, 10))

# Global variable
x = 5
y = 10
def sum2():
   sum = x + y
   return sum
print(sum2())

# Python - Variables. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/python_variables.htm