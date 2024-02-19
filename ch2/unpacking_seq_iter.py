
coordinates=(33.9425, -118.408056)
latitude, longitude = coordinates # tuple unpacking
print(latitude)
print(longitude)

# using *args to grab excess items
# the first two variables unpack 0 and 1
a, b, *rest=range(5)
print(a,b,rest)
a, b, *rest=range(3)
print(a,b,rest)
a, b, *rest=range(2)
print(a,b,rest)

# '*' prefix can appear in any position
a, *body, c, d=range(5)
print(a,body,c,d)
*body, b, c, d=range(5)
print(body, b, c, d)

# unpacking with '*' in function calls
def fun(a,b,c,d,*rest):
    return a,b,c,d,rest

print(fun(*[1,2], 3, *range(4,7)))
