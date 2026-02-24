import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleType(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")
        self.assertEqual(get_triangle_type(1, 1, 1), "equilateral")
    
    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(3, 3, 4), "isosceles")
        self.assertEqual(get_triangle_type(4, 3, 4), "isosceles")
        self.assertEqual(get_triangle_type(3, 4, 4), "isosceles")
        self.assertEqual(get_triangle_type(1, 1, 1.5), "isosceles")
    
    def test_scalene_triangle(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(5, 7, 9), "nonequilateral")
        self.assertEqual(get_triangle_type(2, 3, 4), "nonequilateral")
    
    def test_negative_side_raises_exception(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, -1, 3)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 3, -1)
    
    def test_zero_side_raises_exception(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 3)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 0, 3)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 3, 0)
    
    def test_triangle_inequality_violation_raises_exception(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 10)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 10, 2)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 1, 2)
        
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)
    
    def test_all_negative_sides_raise_exception(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, -2, -3)


if __name__ == '__main__':
    unittest.main()