def noMult(x, y):
    product=0
    for i in range (y): 
        product = product + x 
    return product

def exponent(x, y):
    product = 1
    for i in range (y):
        product = product * x
    return product


def square(x):
    return exponent(x,x)

def main():
    x = int(input("enter a number: "))
    y = int(input("Enter another number: "))
    result = noMult(x,y)
    print(result)
    result = exponent(x,y)
    print (result)
    result = square(x)
    print (result)
#only ask for input in the main
 
main()