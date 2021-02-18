#write a program to input a number and print its cube root.#
def Program11():
    num=float(input("Enter a number:-"))
    num_cube=num*num*num
    print("The cube of",num,"is",num_cube)
#write a program to input a number and print its square root.#
def Program12():
    num=float(input("Enter a number:-"))
    num_sqrt=num**0.5
    print("The square root of",num,"is",num_sqrt)
#Write a program that input an integer in range 0-999 and then print if the integer entered is a 1/2/3 digit number.#
def Program13():
    num=int(input("Enter a number b/w 0....999:-"))
    if num<0:
        print("Invalid entry . Valid range is 0 to 999")
    elif num<10:
        print("Single digit numbered in entered")
    elif num<100:
        print("Two digit numbered in entered")
    elif num<=999:
        print("Three digit number in entered")
    else:
        print("Invalid entry. Valid range is 0 to 999.")
#write a program that input an integer in range 0-999 and then print if the ineger enterd is 1/2/3 digit number. use nested if statement#
def Program14():
    num=int(input("Enter a number b/w 0....999:-"))
    if num<0 or num>999:
        print("Invalid entry . Valid range is 0 to 999")
    else:
        if num<10:
            print("Single digit numbered in entered")
        else:
            if num<100:
                print("Two digit numbered in entered")
            else :
                print("Three digit number in entered")
#Write a progarm to print cube of number in range 15 to 20#
def Program15():
    for i in range(15,21):
        print("Cuber of the number",i,end="")
        print("is",i**3)
#Write a program to print root of every alternate number in range 1 to 10#
def Program16():
    for i in range(1,10,2):
        print("Square root of",i,"is",(i**0.5))
#Write a program that multiplies two integer number without using the * operator , using repeated addition.#
def Program17():
    n1=int(input("Enter the first number:-"))
    n2=int(input("Enter the second number:-"))
    product=0
    count=n1
    while count>0:
        count=count-1
        product=product+n2
    print("The product of",n1,"and",n2,"is",product)

while True:
    print("1.Program1.1")
    print("2.Program1.2")
    print("3.Progeam1.3")
    print("4.Progeam1.4")
    print("5.Progeam1.5")
    print("6.Progeam1.6")
    print("7.Progeam1.7")
    print("8.Exit")
    ch=int(input("Enter your choise:-"))
    if ch==1:
        Program11()
    elif ch==2:
        Program12()
    elif ch==3:
        Program13()
    elif ch==4:
        Program14()
    elif ch==5:
        Program15()
    elif ch==6:
        Program16()
    elif ch==7:
        Program17()
    elif ch==8:
        break
    else:
        print("Invalid Choise!")
