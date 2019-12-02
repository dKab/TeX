
from math import exp
import unittest

def secant(a, b, f):
    return a - f(a)/(f(b) - f(a)) * (b - a)

def tangent(a, f, df):
    return a - f(a)/df(a)

def combinedMethod(a, b, f, df, eps: float=1e-4, kmax: int=1e3):
    x, x_prev, i = b, a, 0
    while abs(x_prev - x) > eps and i < kmax:
        x, x_prev, i = secant(x_prev, x, f), tangent(x_prev, f, df), i + 1
    print('{0} iterations'.format(i))
    return (x + x_prev) / 2 

def function(x):
    return exp(0.8 * x)  - (x + 0.8) ** 2 + 1.1

def derivative(x):
    return -2 * x + 0.8 * exp(0.8 * x) - 1.6

class TestCombined(unittest.TestCase):
	def test_0(self):
		x0 = -1.94498

		self.assertAlmostEqual(combinedMethod(-2.1, -1.5, function, derivative), x0, 5)

if __name__ == '__main__':
	unittest.main()