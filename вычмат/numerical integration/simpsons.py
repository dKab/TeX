from math import sin, exp, sqrt
import unittest

def function(x):
  return sin(exp(-x)) + sqrt(x)


def simpsonsIntegral(f, a, b, n):
  result = 0

  h = (b - a) / n
  
  for i in range(n):
    x1 = a + (i * h)
    x2 = a + ((i + 1) * h)
    mid = (x1 + x2) / 2
    result += f(x1) + (4 * f(mid)) + f(x2)

  result *= h / 6

  return result

class TestNewton(unittest.TestCase):
    def test_0(self):
        
        a = 2
        b = 2.7
        n = 18
        result = 1.14009

        self.assertAlmostEqual(simpsonsIntegral(function, a, b, n), result, 5)

if __name__ == '__main__':
    unittest.main()