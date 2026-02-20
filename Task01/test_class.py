import pytest
from triangle_class import Triangle, IncorrectTriangleSides


def test_create_equilateral_triangle():
    triangle = Triangle(3, 3, 3)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 9


def test_create_isosceles_triangle():
    triangle = Triangle(3, 3, 4)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 10


def test_create_scalene_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12


def test_negative_side_raises_exception():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, -1, 3)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, 3, -1)


def test_zero_side_raises_exception():
    """Негативный тест: нулевая сторона должна вызвать исключение"""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 3)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, 0, 3)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, 3, 0)


def test_triangle_inequality_violation_raises_exception():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 10)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 10, 2)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 1, 2)
    
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)


def test_all_negative_sides_raise_exception():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, -2, -3)


def test_triangle_methods_for_various_triangles():
    t1 = Triangle(5, 5, 5)
    assert t1.triangle_type() == "equilateral"
    assert t1.perimeter() == 15
    
    t2 = Triangle(4, 4, 6)
    assert t2.triangle_type() == "isosceles"
    assert t2.perimeter() == 14
    
    t3 = Triangle(6, 8, 10)
    assert t3.triangle_type() == "nonequilateral"
    assert t3.perimeter() == 24