# -*- coding: utf-8 -*-
"""t02q04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nGEFJYdTsO36m4QyGZILfwSyteRAjxo8
"""

from math import *

A = 8
x1 = 20
x2 = 30

epsilon = 0.000001

def f(u):
  return u**4 - 2 * A * u**3 + (A - u)**2 * (x2**2 - x1**2)

def secant(a, b):
  if f(a) > -epsilon and f(a) < epsilon:
    return a
  b = a - (f(a) * (a - b))/(f(a) - f(b))
  return secant(b, a)

def pit(u):
  print(sqrt(x1**2 - u**2))

if __name__ == '__main__':
  u = secant(0, 50)
  pit(u)