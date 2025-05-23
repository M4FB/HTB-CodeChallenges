# take in the number
n = input().split()
x = int(input())

lista = list(map(int,n))
# calculate answer
numeroRecur = 0
suma = 0

for numero in lista:
    suma = suma + numero * (x ** numeroRecur)
    numeroRecur = numeroRecur + 1 


# print answer
print(suma)
