""" 
    Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su factorial.
"""

print("-------------------------------------------")
print("FACTORIAL DE UN NUMERO N")
n = int(input("Ingrese un numero:"))
factorial=1

for i in range(2, n+1):
    factorial = factorial * i 

print(f"El factorial del numero {n} es : {factorial}")