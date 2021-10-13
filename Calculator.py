import math

n=-1
while(n!=0):
    check=True
    print("Please enter the number of your sellection: ")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. log")
    print("6. sin")
    print("7. cos")
    print("8. tan")
    print("9. cot")
    print("0. exit")
    n=int(input())
    if(n<0 or n>9):
        print("Choose number between 0_9")
        check=False
    else:
        if(n==0):
            break
        a=float(input("Enter the number: "))
        if(n>=1 and n<5):
            b=float(input("Enter the second number: "))
            if(n==1):
                res=a+b
            elif(n==2):
                res=a-b
            elif(n==3):
                res=a*b
            elif(n==4):
              if(b!=0):
                  res=a/b
              else:
                  print("Math ERROR!!")
                  check=False
        elif(n==5):
            res=math.log10(a)
        elif(n==6):
            res=math.sin(math.radians(a))
        elif(n==7):
            res=math.cos(math.radians(a))
        elif(n==8):
            res=math.tan(math.radians(a))
        elif(n==9):
            if(math.tan(math.radians(a))!=0):
                res=1/math.tan(math.radians(a))
            else:
                print("Math ERROR!!")
                check=False
    if(check==True):
         print(res)
    print("if you want to try again press 1 else press any key: ")
    con=input()
    if(con!=1):
        break
    