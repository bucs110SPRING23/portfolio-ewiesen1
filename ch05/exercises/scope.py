#num1 = int(input("Enter number "))

def noMult(num1, num2):
    product=0
    for i in range (num2): 
        product = product + num1 
    print(product)     
print(noMult(6, 7))


def exponent(num3, exp):
    product = 1
    for i in range (exp):
        product = product * num3
    print(product)
print(exponent(4, 3))

def square(a):
    exponent(a,a)
print(square(4))

