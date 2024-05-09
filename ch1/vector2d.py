import math

class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f'Vector({self.x!r} , {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Adding Vectors
v1 = Vector(2,3)
v2 = Vector(1,1)
print(v1 + v2)

# Get absolute value of Vector
v3 = v1 + v2
print(abs(v3))

# Scalar multiplication of Vectors
v4 = v3 * 3
print(v4)
print(abs(v4))

# Print the bool truthy
print(bool(v4.x))
print(bool(v4.y))