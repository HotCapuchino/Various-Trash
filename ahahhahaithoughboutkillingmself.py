import random
from math import sqrt


def quickPower(number, power):
    if power == 0:
        return 1
    elif power % 2 != 0:
        return number * quickPower(number, power - 1)
    else:
        return quickPower(number * number, power / 2)


def isPrime(number):
    if number == 0:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generatePrime(size):
    limit_number = 2 ** size - 1
    num1 = 0
    num2 = 0
    while not isPrime(num1):
        num1 = random.randint(3, limit_number)
    while not isPrime(num2) and num2 != num1:
        num2 = random.randint(3, limit_number)
    return num1, num2


def generatePublicExp(Euler, size):
    for i in range(int(Euler / size), Euler):
        if Euler % i != 0:
            return i


def generatePrivateExp(Euler, publicExp):
    for i in range(Euler):
        if (publicExp * i) % Euler == 1:
            return i


def encrypt(src):
    encrypted_text = []
    for i in src:
        encrypted_text.append(quickPower(ord(i), publicExp) % module)
    return encrypted_text


def decrypt(src):
    decrypted_text = []
    for i in src:
        decrypted_text.append(chr(quickPower(i, privateExp) % module))
    return decrypted_text


def checkRequirements(privateExp, publicExp, num1, num2, Euler):
    for i in [privateExp, publicExp, num1, num2, Euler]:
        if i is None:
            return False
    if num1 == num2:
        return False
    if Euler == 0:
        return False
    if privateExp == publicExp:
        return False
    return True


print("Enter the size of number in bytes: ", end="")
size = int(input())
num1, num2 = generatePrime(size)
module = num1 * num2
Euler = (num1 - 1) * (num2 - 1)
publicExp = generatePublicExp(Euler, size)
privateExp = generatePrivateExp(Euler, publicExp)
if checkRequirements(privateExp, publicExp, num1, num2, Euler):
    print("num1: ", num1)
    print("num2: ", num2)
    print("module: ", module)
    print("Euler: ", Euler)
    print("publicExp: ", publicExp)
    print("privateExp: ", privateExp)
    print("Public Key: ", publicExp, " ", module)
    print("Private Key: ", privateExp, " ", module)
    publicKey = (publicExp, module)
    privateKey = (privateExp, module)
    print("Now enter text, you want to de encrypted: ", end="")
    text = input()
    src = encrypt(text)
    print("Encrypted text: ", end="")
    for i in src:
        print(i, end=" ")
    print("\nDecrypted text: ", end="")
    for i in decrypt(src):
        print(i, end="")
else:
    print("Error occured while generating RSA key, please try again!")
