import random
while(True):
    print("Enter the number of your sellection: ")
    print("1. UP")
    print("2. DOWN")
    u=int(input())
    c1=random.randint(1,2)
    c2=random.randint(1,2)
    print("Computer1: ",c1)
    print("Computer2: ",c2)
    if(u!=c1 and u!=c2):
        print("User WON!!")
        break
    elif(c1!=u and c1!=c2):
        print("Computer1 WON!!")
        break
    elif(c2!=u and c2!=c1):
        print("Computer2 WON!!")
        break
    else:
        print("DRAW!!!....Try again")