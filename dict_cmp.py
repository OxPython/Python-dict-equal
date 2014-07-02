'''
Created on Jul 2, 2014

@author: viejoemer

I can compare several dictionaries in Python?

¿Yo puedo comparar varios diccionarios en Python?

== Compares elements of both dict.
'''

#Definition of a dictionary
d = {'three': 3, 'two': 2, 'one': 1}
print(d)


#Definition of a dictionary
d2 = {'three': 3, 'two': 2, 'one': 1}
print(d2)

#comparing elements
print(d == d2)

#Definition of a dictionary
d3 = {'three': 3, 'two': 2,}
print(d3)

#comparing elements
print(d == d2 == d3)