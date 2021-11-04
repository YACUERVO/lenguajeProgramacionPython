#Valores infinitos
import math
from decimal import Decimal


infinitoPositivo= float("inf")
print(infinitoPositivo)
print(f"Es infinito: {math.isinf(infinitoPositivo)}")

infinitoNegativo=float("-inf")
print(infinitoNegativo)
print(f"Es infinito: {math.isinf(infinitoNegativo)}")

#Moduclo math
infinitoPositivo = math.inf
print(infinitoPositivo)
print(f"Es infinito: {math.isinf(infinitoPositivo)}")

infinitoNegativo = -math.inf
print(infinitoNegativo)
print(f"Es infinito: {math.isinf(infinitoNegativo)}")

#Modulo Decimal
infinitoPositivo=Decimal('Infinity')
print(infinitoPositivo)
print(f"Es infinito: {math.isinf(infinitoPositivo)}")

infinitoNegativo=Decimal('-Infinity')
print(infinitoNegativo)
print(f"Es infinito: {math.isinf(infinitoNegativo)}")