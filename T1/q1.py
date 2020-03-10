import sys
import PyGnuplot as gp
from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fmin

def f(x: int) -> float:
    return x**3 - 2*x**2 - x + 2

def t1q1(f):
    gp.c('set terminal png')
    gp.c('set output "t1q1.png"')
    gp.c('set xrange[-1.5:2.5]')
    gp.c('plot x*x*x - 2*x - x + 2 title "função cúbica"')

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 2 else None
    t1q1(f)
