import random
en=input("enter:")
def user():
    if en=="r":
        return 1
    elif en=="s":
        return 2
    else:
        return 3

def ai():
    return random.randint(1,3)

a=user()
b=ai()




if a==b:
    print("math is draw..!")
elif a==1 and b==2:
    print("scissor")
    print("you win..!")
elif a==2 and b==3:
    print("paper..!\n")
    print("i am win..!")
elif a==3 and b==1:
    print("rock..!\n")
    print("you win..!")
elif a==1 and b==3:
    print("paper..!\n")
    print("i am win..!")            
elif a==2 and b==1:
    print("rock..!|n")
    print("you win..!")
else:
    print("scissor")
    print("i am win")
            
    



