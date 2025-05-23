from math import sqrt

# I es la vaina de la raiz cuadrada
def isPrime(n, i):
    if n < 2:
        return False
    if i < 2:
        return True
    if n % i == 0:
        return False
    return isPrime(n, i - 1)


# take in the number
n = input().split()
mult = 1
inputList = list(map(int, n))

# calculate answer
for number in inputList:
    if isPrime(number, int(sqrt(number))):  # Corregido aquí
        mult = mult * number

# print answer
print(mult)

