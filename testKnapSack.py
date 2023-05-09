import unittest
from knapsack import bruteForceKnapSack_01, bruteForceKnapSack_Frac, greedyKnapSack_Frac

class KnapSackTestCase(unittest.TestCase):        

    
    def test_bruteForceKnapSack_01(self):
        p1 = [42,30,45,10]
        w1 = [3,4,9,5]
        m1 = 16

        self.assertEqual(bruteForceKnapSack_01(p1,w1,m1), 117)

        p2 = [10,20,13]
        w2 = [1,4]
        m2 = 10
        with self.assertRaises(AssertionError):
            bruteForceKnapSack_01(p2,w2,m2)

    def test_bruteForceKnapSack_fractional(self):
        p1 = [42,30,45,10]
        w1 = [3,5,9,5]
        m1 = 16

        self.assertEqual(bruteForceKnapSack_Frac(p1,w1,m1), 111)
   
    def test_greedyKnapSack_fractional(self):
        p1 = [42,30,45,10]
        w1 = [3,5,9,5]
        m1 = 16

        self.assertEqual(greedyKnapSack_Frac(p1,w1,m1), 122)
       

if __name__ == "__main__":
    unittest.main()    