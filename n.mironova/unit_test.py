import unittest
import math

class geometry_shape:
    def get_surface():
        return 0

class rectangle(geometry_shape):
    a: float
    b: float

    def __init__(self, side_a: float, side_b: float):
        self.a = side_a
        self.b = side_b

    def get_surface(self):
        return self.a * self.b

class triangle(geometry_shape):
    a: float
    b: float
    c: float

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def get_surface(self):

        if self.a + self.b <= self.c:
            return "invalid set of sides"
        if self.c + self.b <= self.a:
            return "invalid set of sides"
        if self.a + self.c <= self.b:
            return "invalid set of sides"
        
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))

class TestGeometryShapeChildren(unittest.TestCase):
    tri_shape: triangle
    rect_shape: rectangle

    def setUp(self):
        self.tri_shape = triangle(3, 4, 5)
        self.rect_shape = rectangle(3, 4)
    
    def test_get_tri_surface(self):
        self.assertEqual(self.tri_shape.get_surface(), 6)
    def test_get_rect_surface(self):
        self.assertEqual(self.rect_shape.get_surface(), 12)

shape_1 = rectangle(10, 3)
print("s_rect = ", shape_1.get_surface())

shape_2 = triangle(4, 5, 3)
print("s_tri = ", shape_2.get_surface())

if __name__ == "__main__":
    unittest.main()