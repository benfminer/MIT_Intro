"""
This program asks user for two numbers (x and y) then returns
x raised to the y power and returns the log of x.
"""
from math import log

x = input("Enter number x: ")
y = input("Enter number y: ")
print(int(x)**int(y))
print(log(int(x), 2))
