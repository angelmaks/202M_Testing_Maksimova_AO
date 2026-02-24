import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return []
            else:
                return []
        else:
            return [-c / b]
    
    discriminant = b*b - 4*a*c
    
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        
        if x1 < x2:
            return [x1, x2]
        else:
            return [x2, x1]