def geometric(a,b):
    for i in range(0,10):
        print(a)
        a = a*b
geometric(int(input("Enter first term of the series ")),int(input("Enter Common Ratio ")))