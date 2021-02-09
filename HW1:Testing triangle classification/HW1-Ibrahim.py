"""
    HW 01: Testing triangle classification
    Author: Ibrahim Alqarni
    Date: 02/08/2021
    Python version 3.8.1
"""
import unittest

def classify_triangle(a,b,c):
    """ function to classify type of triangles where x, y and z are the lengths of sides """
    if a + b > c and a + c > b and b + c > a:
        if a > 0 and b > 0 and c > 0:
            if a == b == c:
                return 'Equilateral'

            elif a * a + b * b == c * c:
                return 'Right'

            elif a == b != c:
                return 'Isosceles'

            else:
                return 'Scalene'

        else:
            return 'False'
    else:
        return 'False'

class testTriangleTests(unittest.TestCase ):
    def test_triangle(self):
        self.assertEqual(classify_triangle( 2 , 2 , 2 ) , "Equilateral")
        self.assertNotEqual(classify_triangle( 4 , 4 , 4 ) , "Right")
        self.assertEqual(classify_triangle( 3 , 4 , 5 ) , "Right")
        self.assertTrue(classify_triangle( 4 , 3 , 4 ) , "Isosceles")
        self.assertNotEqual(classify_triangle( 2 , 3 , 4 ), "Equilateral")
        self.assertTrue(classify_triangle(3, 4, 6), "Scalene")
        self.assertEqual(classify_triangle( 1 , 2 , 3 ) , "False")
        self.assertEqual(classify_triangle(2, 0, 2), "False")

def main():
    'to demonstrate the result'
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(4, 4, 6))
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(2, 4, 3))

    unittest.main()

if __name__ == '__main__':
    main()