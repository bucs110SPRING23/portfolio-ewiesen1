def foo(x,y,z):
    print (x,y,z)

foo(1,2,3)
foo(2,1,3)
#foo(3,2) yields an error - not enough parameters

def bar(x=0, y=2, z=3):
    print (x,y,z)

bar(1,2,3)
bar(1,2)
bar(z=1,x=2)
bar()
