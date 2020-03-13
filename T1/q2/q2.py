import PyGnuplot as gp
from math import *

def appPoint(x, y, pts):
    f = open(pts, "a")
    f.write(f"{x} {y}\n")
    f.close()

def conc_files(f1, f2):
    data = data2 = "" 
  
    with open(f1) as fp: 
        data = fp.read() 
  
    with open(f2) as fp: 
        data2 = fp.read() 

    data += "\n"
    data += data2 
  
    with open ('arquivos.pts', 'w') as fp: 
        fp.write(data)

def f(x, h):
    if x == 0:
        return 1
    else:
        x = x - h
        fx = f(x, h) + h * fprime(x)
        return fx

def fprime(x):
    return cos(x) - x*sin(x)

def estimate():
    x = 0
    h = 0.5

    while x <= 6:
        y = f(x, h) 
        appPoint(x, y, "sorted.pts")
        x = x + h
    
    x = -0.5
    h = -h

    while x >= -6:
        y = f(x, h) 
        appPoint(x, y, "unsorted.pts")
        x = x + h

    p = open('unsorted.pts')
    points = p.readlines()
    points.reverse() 
    p.close()

    conc_files('sorted.pts', 'unsorted.pts')

def t1q2():
    open('arquivos.pts', 'w').close()
    open('sorted.pts', 'w').close()
    open('unsorted.pts', 'w').close()

    estimate()

    gp.c('set terminal png')
    gp.c('set xrange[-6:6]')
    gp.c('set yrange[-6:6]')
    gp.c('set grid')
    gp.c('set xzeroaxis lw 2')
    gp.c('set yzeroaxis lw 2')
    gp.c('set output "t1q2.png"')
    gp.c('plot "arquivos.pts" with lp title "aproximação", x*cos(x) + 1')

if __name__ == '__main__':
    t1q2()
