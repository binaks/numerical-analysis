import PyGnuplot as gp
from math import *
import numpy as np

def f(x: int) -> float:
    return x**3 - 2*x**2 - x + 2

def fprime(x: int) -> float:
    return 3*x**2 - 4*x - 1 

def find_b(a, x, y):
    return y - a*x

def t1q1(f):
    x = 1

    gp.c('set terminal eps')
    gp.c('set xrange[-1.5:2.5]')
    gp.c('set output "t1q1.eps"')
    gp.c('plot x*x*x - 2*x - x + 2 title "função cúbica"')

    a = fprime(x)
    y = f(x)
    b = find_b(a, x, y)

    gp.c('set output "t1q1.eps"')
    gp.c('replot -2*x + 2 title "reta tangente em x = 1"')

if __name__ == '__main__':
    t1q1(f)
