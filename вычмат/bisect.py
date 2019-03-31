from math import sin
import unittest
"""
* Variable Description:
*
* f			:	Given function
* f_		:	Derivative of f
* [a, b]	:	End point values
* eps		:	Tolerance
* NMAX		:	Max number of iterations
"""


def bisection(f, a, b, eps=1e-7, NMAX=1e4):
	"""
	Takes a function f, start values [a,b], tolerance value(optional) eps and
	max number of iterations(optional) NMAX and returns the root of the equation
	using the bisection method.
	"""
	n=1
	while n<=NMAX:
		c = (a+b)/2.0
		print('a={0} b={1} c={2} f(c)={3}'.format(a,b,c,f(c)))
		if f(c)==0 or (b-a)/2.0 < eps:
			return c
		else:
			n = n+1
			if f(c)*f(a) > 0:
				a=c
			else:
				b=c
	return False

class TestBisect(unittest.TestCase):
	def test_0(self):
		def f(x: float):
			return x**2 - 20 * sin(x)

		a, b, x_star = 1, 10, 2.7529466338187049383

		self.assertAlmostEqual(bisection(f, a, b), x_star)


if __name__ == '__main__':
	unittest.main()