import PyGnuplot as gp
from math import *

def appPoint(x, y, pts):
    f = open(pts, "a")
    f.write(f"{x} {y}\n")
    f.close()

def f_odd(x, k):
    return ((-1)**((k-1)/2)) * k * cos(x) + ((-1)**((k+1)/2)) * x * sin(x)

def f_even(x, k):
    return ((-1)**(k/2)) * k * sin(x) + ((-1)**(k/2)) * x * cos(x)

def taylor(x, a):
    sum = 0

    for k in range (0, 12):
        if k%2 == 0:
            sum += (f_even(a, k)/factorial(k)) * ((x - a)**k)
        else:
            sum += (f_odd(a, k)/factorial(k)) * ((x - a)**k)
    
    return sum

def estimate():
    a = 0
    x = -6
    h = 0.1

    while x <= 6:
        y = taylor (x, a)
        appPoint(x, y, "q2-2.pts")
        x = x + h

def t1q2_2():
    open('q2-2.pts', 'w').close()

    gp.c('set terminal png')
    gp.c('set xrange[-6:6]')
    gp.c('set yrange[-6:6]')
    gp.c('set grid')
    gp.c('set xzeroaxis lw 2')
    gp.c('set yzeroaxis lw 2')
    gp.c('set output "t1q2_2.png"')

    estimate()
    gp.c('plot "q2-2.pts" with lp title "taylor", x*cos(x) + 1')

if __name__ == '__main__':
    t1q2_2()
