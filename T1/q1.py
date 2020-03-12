import PyGnuplot as gp
from math import *

def f(x):
    return x**3 - 2*x**2 - x + 2

def fprime(x):
    return 3*x**2 - 4*x - 1 

def find_b(a, x, y):
    return y - a*x

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    root_1 = (-b + sqrt(delta))/(2*a)
    root_2 = (-b - sqrt(delta))/(2*a)
    return [root_1, root_2]

def appPoint(x, y):
    f = open("points.pts", "a")
    f.write(f"{x} {y}\n")
    f.close()

def t1q1(f):
    open('points.pts', 'w').close()

    x = 1

    gp.c('set terminal png')
    gp.c('set xrange[-1.5:2.5]')
    gp.c('set yrange[-3:5]')
    gp.c('set xtics 0.5')
    gp.c('set ytics 1')
    gp.c('set grid')
    gp.c('set xzeroaxis lw 2')
    gp.c('set yzeroaxis lw 2')
    gp.c('set output "t1q1.png"')
    gp.c('plot x*x*x - 2*x*x - x + 2 title "função cúbica"')

    a = fprime(x)
    y = f(x)
    b = find_b(a, x, y)

    appPoint(x, f(x))

    gp.c('set output "t1q1.png"')
    gp.c(f'replot {a}*x + {b} title "reta tangente em x = 1"')

    roots = bhaskara(3, -4, -1)
    
    for root in roots:
        x = root
        a = fprime(x)
        y = f(x)
        b = find_b(a, x, y)

        gp.c('set output "t1q1.png"')
        gp.c(f'replot {a}*x + {b} title "reta tangente em x = {root}"')

        appPoint(x, y)
        
    gp.c('set output "t1q1.png"')
    gp.c('replot "points.pts" title "pontos"')
    
if __name__ == '__main__':
    t1q1(f)
