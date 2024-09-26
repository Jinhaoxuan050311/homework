import cmath
a = 1
b = -2
c = -8
discriminant = (b**2) - (4*a*c)
x1 = (-b - cmath.sqrt(discriminant)) / (2*a)
x2 = (-b + cmath.sqrt(discriminant)) / (2*a)
print(f"The solutions of the equation are: x1 = {x1}, x2 = {x2}")
