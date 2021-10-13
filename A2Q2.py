import random
i=0
u=0
c=0
while(i<5):
    print('Enter the number of your sellection: ')
    print('1. sang')
    print('2. kaqz')
    print('3. gheichi')
    a=int(input())
    b=random.randint(1,3)
    if((a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2)):
        u += 1
    elif((b==1 and a==3) or (b==2 and a==1) or (b==3 and a==2)):
        c += 1
    print("User: ",u)
    print("Computer: ",c)
    i += 1
if(u>c):
    print("User WON!!")
elif(c>u):
    print("Computer WON!!")
elif(c==u):
    print("DRAW!!!")