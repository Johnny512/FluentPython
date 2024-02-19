# Example 2-5. Initialize a tuple and array using generator expressions
symbols = '@#$%^&*'
tupleGenExp = tuple(ord(symbol) for symbol in symbols)
print(tupleGenExp)
for i in tupleGenExp:
    print(i)

import array
arrGenExp = array.array('I', (ord(symbol) for symbol in symbols))
print(arrGenExp)
for i in arrGenExp:
    print(i)


# Example 2-6 Cartesian product using generator expression
colors = 'black white'.split()
sizes = 'S M L'.split()
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)