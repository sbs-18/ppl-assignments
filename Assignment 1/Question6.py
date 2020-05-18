def divsum(n):
    divsum = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            divsum+=i
    return divsum
        
def amicable(r):
    i = 4
    while r>0:
        if i == divsum(divsum(i)) and i!=divsum(i):
            print(i,divsum(i))
            i = divsum(i) + 1
            r-=1
        i+=1
amicable(10)