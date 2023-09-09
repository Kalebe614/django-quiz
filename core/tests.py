from django.test import TestCase
from functools import reduce
# Create your tests here.

numeros = [2, 3, 5, 2]
frutas = ['banana', 'pera', 'banana']


frutas.append('abacate')
frutas2 =['Caqui']

frutas2.extend(frutas)
print(frutas2.count('banana'))