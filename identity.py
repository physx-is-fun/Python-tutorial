a = 20
b = 20

if ( a is b ):
   print("Line 1 - a and b have same identity") 
else:
   print("Line 1 - a and b do not have same identity") 

if ( id(a) == id(b) ):
   print("Line 2 - a and b have same identity") 
else:
   print("Line 2 - a and b do not have same identity") 

b = 30
if ( a is b ):
   print("Line 3 - a and b have same identity") 
else:
   print("Line 3 - a and b do not have same identity") 

if ( a is not b ):
   print("Line 4 - a and b do not have same identity") 
else:
   print("Line 4 - a and b have same identity") 

# Python Identity Operators Example. (2012, June 10). Tutorials Point. Retrieved May 13, 2023, from https://www.tutorialspoint.com/python/identity_operators_example.htm