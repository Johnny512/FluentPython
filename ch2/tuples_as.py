# Example 2-7. Tuples used as records
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
data = dict(city=city, year=year, pop=pop, chg=chg, area=area)
print(data)

# tuples with a list can be changed
a=(10, 'alpha', [1,2])
b=(10, 'alpha', [1,2])

print('a=(10, "alpha", [1,2])')
print('b=(10, "alpha", [1,2])')
print('Is a equal to b? ', a==b)
b[-1].append(99)
print(a)
print(b)
print(a==b)