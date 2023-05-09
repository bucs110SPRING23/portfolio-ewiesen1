def foo():
    local_var = 5
    x = 2

def foo():
    local_var = 5
    #print(x) # does not exist because every local variable is deleted after the function ends
global_var = 5 #global scope


#f(x) = y
#functions must return a value

def foo():
    x=5
    return x, 6 #returns a value of 5, x ceases to exist

y, z = foo()
print(y)


####

def foo():
    x = 5
    print(x*x)

def foo2():
    x = 5
    return x*x

print(foo()) #None
print(foo2()) #25

#nested functions execute from the inside out
#if you don't have a return in your function, it will return None


########

def foo_bar(): #conventional python form
    x=5
    y=6
    return x*y

#10000 line program
# name collisons
# #global variables never leave memory while the program is running
var = 5

def start(var):
    print (var)


def dosomething():
    print (var)

def main(): #main function
    x = 5
    start(x)
    start(x)
    dosomething()

#must call your main in global scope, at the END
main()