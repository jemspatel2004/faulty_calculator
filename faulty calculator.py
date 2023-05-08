#faulty calculater.

while True:     #here use a while loop.


    a=float(input("enter number a:"))    
    b=float(input("enter number b:"))

    c=float(input("select your function:\n1)+\n2)-\n3)*\n4)/\n5)Exit\n"))  #here also use int()

    if c==1:
        if a==56 and b==9:             #fault is a 56+9=77
            print("the answer is 77")
            break
        else:
            print("the answer is",a+b)
            break
    elif c==2:
        print("the answer is",a-b)
        break
    elif c==3:
        if a==43 and b==3:            #fault is a 43*3=555
            print("the answer is 555")
            break
        else:
            print("the answer is",a*b)
            break
    elif c==4:
        if a==56 and b==6:
            print("the answer is 4")     #fault is a 56/6=4
            break
        else:
            print("the answer is",a/b)
            break                         #to break while loop.

    elif c==5:
        print("visit again")
        break

    else:
        print("sorry not found this number.please,enter again")
        break
        

