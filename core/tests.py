from django.test import TestCase
from functools import reduce
# Create your tests here.

numeros = [2, 3, 5, 2]

multiplica = lambda x, y: x*y

total = reduce(multiplica, numeros)

print(total)