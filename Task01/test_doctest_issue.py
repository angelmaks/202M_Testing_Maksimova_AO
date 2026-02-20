from triangle_func import get_triangle_type, IncorrectTriangleSides

try:
    get_triangle_type(-1, 2, 3)
except IncorrectTriangleSides as e:
    print(f"Exception type: {type(e)}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

try:
    get_triangle_type(1, 2, 10)
except IncorrectTriangleSides as e:
    print(f"Exception type: {type(e)}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")