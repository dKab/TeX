from math import exp
from typing import Callable
import unittest

def newton(f: Callable[[float], float], f_prime: Callable[[float], float], x0: float, 
	eps: float=1e-4, kmax: int=1e3) -> float:
	"""
	solves f(x) = 0 by Newton's method with precision eps
	:param f: f
	:param f_prime: f'
	:param x0: starting point
	:param eps: precision wanted
	:return: root of f(x) = 0
	"""
	x, x_prev, i = x0, x0 + 2 * eps, 0
	
	while abs(x - x_prev) >= eps and i < kmax:
		x, x_prev, i = x - f(x) / f_prime(x), x, i + 1

	print('{0} iterations'.format(i))

	return x

def function(x):
	return exp(0.8 * x) - (x + 0.8) ** 2 + 1.1

def derivative(x):
	return -2 * x + 0.8 * exp(0.8 * x) - 1.6

class TestNewton(unittest.TestCase):
	def test_0(self):
		
		x0, x = 3.67658, 3

		self.assertAlmostEqual(newton(function, derivative, x), x0, 5)

if __name__ == '__main__':
	unittest.main()