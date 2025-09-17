# Compare different quadrature rules for integration

There are two examples provided for calculating the weights and abscissas for gaussian quadrature rules, try:

```
make
./gqconstants
```

or

```
python gqconstants.py
```

You can also use the C++ example as a guide to build your own executable

There is no need to look at rules >~25 for Gaussian quadrature.  And you can also stop at ~ 1000 divisions for the trapezoidal and Simpson's rules.  If you run much longer you'll see the numerical errors bevome visible for the trapezoidal, but hyou'll need to think about how to code efficiently or the running time may be very long.

Notes:
The gaussian quadrature algorithm that was given is so accurate that after about n=5 it hits machine precision and the error is calculated as 0. The slopes of the trapezoid and simpsons methods are -2 and -4 repsectively on the log log plot, so the error is O(1/N^2) and O(1/N^4) respectively. Simpsons hits machine precision at about 10^3 points and trapezoid would hit it at about 10^6 points.

To create the worst errors, I thought that I would need a function that changes very sharply and rapidly, with tons of changes, so that it is extremely difficult to approximate it as a polynomial for the gaussian algorithm, and so that the very large derivatives of many orders deep will give trouble to the simpsons and trapezoid algorithms. I tested the function sin(1000x), which fluctuates a ton in a short period and can have very high magnitude derivavtives of any order. The algorithms had a lot of difficulty because the function changes so much and so sharply. 

One strategy that may help a lot in approximating the integral for sin(kx) where k is some large number is to have the number of points based on k, so the points are aligned in some way with the frequency of the function. This can allow a much more consistent approximation. Also, you can realize that over an interval of 2pi/k the integral is 0 and you can use this to help with the error. Lastly, we can see that in the plot it seems like the errors of trapezoid and simpsons algorithms fall into their power law relationship when N=500 or so, so it seems that if N is much bigger than k then the error will be small. For gaussian algorithm, it is based on approximating the function with a polynomial, which is very difficult for a function that oscillates so much.

