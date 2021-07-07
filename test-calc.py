import unittest
import calc

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-10,-5),-15)
        self.assertEqual(calc.add(10,-5),5)
        self.assertEqual(calc.add(-10,5),-5)
    def test_subs(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-10,-5),-5)
        self.assertEqual(calc.subtract(10,-5),15)
        self.assertEqual(calc.subtract(-10,5),-15)
    def test_mul(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-10,-5),50)
        self.assertEqual(calc.multiply(10,-5),-50)
        self.assertEqual(calc.multiply(-10,5),-50)
    def test_div(self):
        self.assertEqual(calc.divide(10,5),2) 
        self.assertEqual(calc.divide(-10,-5),2) 
        self.assertEqual(calc.divide(10,-5),-2) 
        self.assertEqual(calc.divide(-10,5),-2)   

        with self.assertRaises(ValueError):
            calc.divide(10,0)

#print(__name__) #test_calc __main__


if __name__=='__main__':
    unittest.main()

