
#exception handling for a function ask(), if a number is not input, the function asks the user again
def ask():
    while True:
        p1=(input("Enter a number\n"))
        try:
            print(int(p1)**2)
            
        except:
            print("Character entered is not a number, try again\n")
        else:
            print("All done")
            break

ask()
#Raising exceptions for file handling, if the file is not found in the given directory
try:
    file = open("Assignment.txt","r")
    for line in file:
        print(line)
except:
    print("File Doesn't exist")
