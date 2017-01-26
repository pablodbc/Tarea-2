'''
Created on Jan 24, 2017

@author: Pablo Betancourt
@author: Jonathan Reyes
'''
from datetime import *

# Clase Tarifa que contiene el precio a pagar por hora tanto en un fin de semana como en un dia habil.

class Tarifa:
    def __init__ (self,diaHabil,diaFinSemana):
        self.precioSemana = diaHabil
        self.precioFinSemana = diaFinSemana

# Funcion que retorna el costo total de un servicio.
# Recibe el objeto tarifa y una lista de dos elementos con el momento inicial y final del servicio.

def calcularPrecio(tarifa,tiempoDeServicio):
    costoTotal = 0
    delta = timedelta(seconds = 3600)
    inicio = tiempoDeServicio[0]
    final  = tiempoDeServicio[1]
    while(inicio < final):
        if(inicio.weekday() == 5 or inicio.weekday() == 6): #Si es un fin de semana
            costoTotal += tarifa.precioFinSemana
        else:
            costoTotal += tarifa.precioSemana
        inicio += delta
    return costoTotal

def checkDatos(inicio, final):
    try:
        # Se chequea que la hora final sea mayor o igual a la inicial
        check = final >= inicio
        assert(check)
        # Se chequea que el servicio cumpla un tiempo minimo de 15 minutos
        # y un maximo de 7 dias
        delta = final - inicio
        checkMin = (delta.days == 0 and delta.seconds >= 900) or (delta.days > 0)
        assert(checkMin)
        checkMax = delta.days <= 7
        assert(checkMax)
    except:
        if(not check):
            print("El final de servicio no puede ocurrir antes que el inicio")
        elif (not checkMin):
            print("La duracion del servicio debe ser mayor o igual a 15 minutos")
        elif (not checkMax):
            print("La duracion del servicio no debe ser mayor a 7 dias")
