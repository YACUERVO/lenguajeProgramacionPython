from decimal import Decimal
import decimal
import math

#NaN Not a number (No es un numero)
a=float("NaN")
print(a)
print(f"Es NaN (not a number):  {math.isnan(a)}")

a=Decimal("NaN")
print(a)
print(f"Es NaN (not a number):  {math.isnan(a)}")


