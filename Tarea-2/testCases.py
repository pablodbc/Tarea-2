'''
Created on Jan 26, 2017

@author: Pablo Betancourt
@author: Jonathan Reyes
'''
import unittest
from Tarea2 import *


class runTestCases(unittest.TestCase):

    def testCalcularPrecio(self):
        formato = '%d/%m/%Y %H:%M'
        inicio = datetime.strptime("25/01/2017 22:00", formato)
        final  = datetime.strptime("25/01/2017 22:14", formato)
        checkDatos(inicio, final)
        assert(calcularPrecio(Tarifa(1,2), [inicio,final]) == 1)
        
    def testCalcularPrecioUnaHoraUnMinuto(self):
        formato = '%d/%m/%Y %H:%M'
        inicio = datetime.strptime("25/01/2017 22:00", formato)
        final  = datetime.strptime("25/01/2017 23:01", formato)
        checkDatos(inicio, final)
        assert(calcularPrecio(Tarifa(1,2), [inicio,final]) == 2)
    
    def testCalcularPrecioFinDeSemana(self):
        formato = '%d/%m/%Y %H:%M'
        inicio = datetime.strptime("07/01/2017 22:00", formato)
        final  = datetime.strptime("08/01/2017 23:00", formato)
        checkDatos(inicio, final)
        assert(calcularPrecio(Tarifa(1,2), [inicio,final]) == 50)


if name == "__main__":
    unittest.main()
