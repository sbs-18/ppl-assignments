import random
def numcheck():
    i = random.randint(1,100)
    while True:
        j = int(input("Choose a number "))
        if j>i:
            print("Choose a smaller number")
        elif j<i:
            print("Choose a greater number")
        else:
            print("Correct")
            break
numcheck()