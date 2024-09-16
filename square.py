# Aaryan Mori - 1002166689
# Pritesh Sorathia - 1002238997
# Likith Reddy - 1002228347
#
# calculator.py
def add(x, y):
   """Addition"""
   return x + y
 
def subtract(x, y):
   """Subtraction"""
   return x - y
 
def multiply(x, y):
   """Multiplication"""
   return x * y
 
def divide(x, y):
   """Division"""
   if y == 0:
       raise ValueError("Cannot divide by zero!")
   return x / y
