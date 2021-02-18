#Program to add two number through a function#
def calSum(x,y):
    s=x+y
    return s
#Program to calculate simple interest using function interest() that can receve principal amount,time and rate and return calculated simple interest.Do specify default value for rate and time as 10% 2 years respectibvely#
def interest(principal,time=2,rate=0.10):
    return principal*rate*time
#program that receives two number in afunction and return the result of all arithmetic (+,-,*,/,%) pn these number)
def arCal(x,y):
    return x+y,x-y,x*y,x/y,x%y
while True :
    print("1.Program3.1(calSum())")
    print("2.Program3.2")
    print("3.Program 3.3")
    print("4.Exit")
    ch=int(input("Enter your choise 1..4:-"))
    if ch==1:
        num1=int(input("Enter First number:-"))
        num2=int(input("Enter Second number:-"))
        sum=calSum(num1,num2)
        print("Sum of two given number is",sum)
    elif ch==2:
        prin=float(input("Enter principal amount:-"))
        print("Simple interest with default ROI and time values is:-")
        si1=interest(prin)
        print("Rs.",si1)
        roi=float(input("Enter the rate of interest(ROI)"))
        time=int(input("Enter time in Year"))
        print("Simple interest with your provided ROI and time interval is:-")
        si2=interest(prin,time,roi/100)
        print("Rs.",si2)
    elif ch==3:
        num1=int(input("Enter the First Number:-"))
        num2=int(input("Enter the Second Number:-"))
        add,sub,mult,div,mod=arCal(num1,num2)
        print("Sum of given numbers:-",add)
        print("Subtraction of given numbers:-",sub)
        print("Product of given numbers:-",mult)
        print("Division of given numbers:-",div)
        print("Modulo of given numbers:-",mod)
    elif ch==4:
        break
    else:
        ("Invalid Choise!")

   
 

