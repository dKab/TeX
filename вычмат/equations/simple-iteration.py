
from math import exp
import unittest

def func(x):
  rez = 0.625 * (exp(0.8 * x) - x**2) + 0.2875
  return rez

def simpleIteration(x, eps, f):
  rez = x
  iter = 0
  while True:
    rez = x
    x = f(x)
    iter += 1
    if not (abs(float(rez) - float(x)) > eps and iter<20000):
        break
  print('{0} iterations'.format(iter))
  return x


class TestSimpleIteration(unittest.TestCase):
	def test_0(self):
		x0 = 1.04668

		self.assertAlmostEqual(simpleIteration(1.5, 1e-4, func), x0, 5)

if __name__ == '__main__':
	unittest.main()

