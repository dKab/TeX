from math import sin, exp, sqrt
import unittest

def function(x):
  return sin(exp(-x)) + sqrt(x)


def trapezoidIntegral(f, a, b, n):
  result = 0

  h = (b - a) / n
  
  for i in range(n):
    result += f(a + (h * (i + 1))) + f (a + (h * i))

  result *= h / 2

  return result

class TestNewton(unittest.TestCase):
    def test_0(self):
        
        a = 2
        b = 2.7
        n = 18
        result = 1.14009

        self.assertAlmostEqual(trapezoidIntegral(function, a, b, n), result, 5)

if __name__ == '__main__':
    unittest.main()