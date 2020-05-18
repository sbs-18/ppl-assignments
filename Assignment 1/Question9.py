def harsum(n):
    harsum = 0.0
    c = 0
    for i in range(1,n+1):
        if n%i==0:
            harsum+=(1/i)
            c+=1
    if int(c/harsum) == c/harsum:
        return True
    else:
        return False
def harmonic():
    i = 0
    c = 1
    while i<10:
        if harsum(c):
            i+=1
            print(c)
        c+=1
harmonic()