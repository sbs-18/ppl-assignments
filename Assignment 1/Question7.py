def cubearm(a):
    p=0
    while a>0:
        p+=pow(a%10,3)
        a=int(a/10)
    return p
def arm(a,b):
    for i in range(a,b+1):
        if i==cubearm(i):
            print(i)
arm(int(input("Enter starting value of the range ")),int(input("Enter ending value of the range ")))