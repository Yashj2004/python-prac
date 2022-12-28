def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def add(a,b):
    return a+b
def divide(a,b):
    try:
        return a/b
    except:
        return "not defined"

a=int(input())
b=int(input())
c=input()
if(c=='*'): 
    print(multiply(a,b))
elif(c=='+'):
    print(add(a,b))
elif(c=='-'):
    print(subtract(a,b))
else:
    print(divide(a,b))

