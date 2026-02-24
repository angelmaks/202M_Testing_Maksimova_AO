class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    """
    Функция для определения типа треугольника по длинам его сторон.
    
    Аргументы:
    a, b, c -- длины сторон треугольника
    
    Возвращает:
    Строку с типом треугольника: "nonequilateral", "isosceles", "equilateral"
    
    Выбрасывает:
    IncorrectTriangleSides -- если стороны некорректны
    
    Примеры:
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 4)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(-1, 2, 3)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны треугольника должны быть положительными
    >>> get_triangle_type(1, 2, 10)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны не удовлетворяют неравенству треугольника
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны треугольника должны быть положительными")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника")
    
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
