from gqconstants import HighPrecisionGaussInt
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp, quad, exp


def trapezoid(f, a, b, n):
    h=(b-a)/n
    sum=(f(a)+f(b))/2
    for i in range(1,n):
        sum+=f(a+h*i)
    return h*sum

def simpsons(f,a,b,n):
    if n % 2 == 1:
        n+=1
    h=(b-a)/n
    sum=(f(a)+f(b))
    for i in range(1,n,2):
        sum+=4*f(a+h*i)
    for i in range(2,n-1,2):
        sum+=2*f(a+h*i)
    return h*sum/3

def gauss(f, a, b, n):
    g = HighPrecisionGaussInt(n)
    return float(g.integ(f,a,b))

def exponentialDecay(t):
    return np.exp(-t)
def sin(t):
    return np.sin(1000*t)

#mp.dps = 50
exact = (1-np.cos(1000))/1000

function = sin

trapN = range(1, 5001)
simpN = range(1, 5001)
gaussN = range(1, 101)

errorsTrap = []
errorsSimp = []
errorsGauss = []

for n in trapN:
    approx = trapezoid(function, 0, 1, n)
    relError = abs((approx - exact) / exact)
    errorsTrap.append(relError)

# simpsons
for n in simpN:
    approx = simpsons(function, 0, 1, n)
    relError = abs((approx - exact) / exact)
    errorsSimp.append(relError)

# gauss
for n in gaussN:
    approx = gauss(function, 0, 1, n)
    relError = abs((approx - exact) / exact)
    errorsGauss.append(relError)
plt.figure(figsize=(8,6))
plt.loglog(trapN, errorsTrap, label="Trapezoid")
plt.loglog(simpN, errorsSimp, label="Simpson's")
plt.loglog(gaussN, errorsGauss, label="Gauss Quadrature")

plt.xlabel("N (number of points)")
plt.ylabel("Relative Error")
plt.title("Relative Error of Integration Methods on $e^{-t}$ from 0 to 1")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.ylim(1e-8, 1000)
plt.show()


    
