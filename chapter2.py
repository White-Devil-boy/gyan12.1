#Progarm that read a line and print its statistics like:#
def Program21():
    line=input("Enter the line:-")
    lowercount=uppercount=0
    digitcount=alphacount=0
    for a in line:
        if a .islower():
            lowercount+=1
        elif a.isupper():
            uppercount+=1
        elif a.isdigit():
            digitcount+=1
        if a.isalpha():
            alphacount+=1
    print("Number of uppercase letters:-",uppercount)
    print("Number of lowercase letters:-",lowercount)
    print("Number of alphabets:-",alphacount)
    print("Number of digit:-",digitcount)
#write a  program to create a dictionary conatining names of competition winner student as keys and number of ther win as value#
def Program22():
    n=int(input("How many Student?"))
    CompWinners={}
    for a in range(n):
        key=input("Name of Student:-")
        value=int(input("Number of competitions won:-"))
        CompWinners[key]=value
    print("The dictionary now is:-")
    print(CompWinners)
#Given three list as list1=['a','b','c'],list2=['h','i','t'],list3=['0','1','2'].Write a program that add list 2 and 3 to list1 as single element. The resultant list should be in the orber of list3, element of list1,list2#
def Program23():
    list1=['a','b','c']
    list2=['h','i','t']
    list3=['0','1','2']
    print("Originally:-")
    print("List1=",list1)
    print("List2=",list2)
    print("List3=",list3)
    #adding list 2 as single element at the end of list1#
    list1.append(list2)
    #adding list 3 as single element at the end of list1#
    list1.insert(0,list3)
    print("After adding to lists the individual element ,list now is;-")
    print(list1)
#Given three list as list1=['a','b','c'],list2=['h','i','t'],list3=['0','1','2'].Write a program that adds individual element of list 2 and 3 to list1. The resultant list should be in the orber of list3, element of list1,list2#
def Program24():
    list1=['a','b','c']
    list2=['h','i','t']
    list3=['0','1','2']
    print("Originally:-")
    print("List1=",list1)
    print("List2=",list2)
    print("List3=",list3)
    #adding element of list1 at the end of list3#
    list3.extend(list1)
    #adding element of list2 at the end of list3#
    list3.extend(list2)
    print("After adding element of two lists individual  ,list now is;-")
    print(list3)
#Write a program that find an element's index/position in atuple WITHOUT using index()#
def Program25():
    tuple1=('a','p','p','l','e')
    char=input("Enter a single letter without quotes:-")
    if char in tuple1:
        count=0
        for a in tuple1:
            if a!=char:
                count+=1
            else:
                break
        print(char,"is at index",count,"in",tuple1)
    else:
        print(char,"is NOT in",tuple1)
#Write a progaram that check the presnce of a value inside a dictionary and print its key.#
def Program26():
    info={'Divyanshu':'Maths','Abhishek':'Bio','Yash':'Com','Sweeti':'Comp'}
    inp=input("Enter the value to be searched for:-")
    inp = info.values():
        for a in info:
            if info[a]==inp:
                print("The key of the given value is :-",a)
                break
        else:
            print("Given value does not exist in dictionary")
# same a progarm 26 but can work in diferent case#
def Program27():
    info={'Divyanshu':'Maths','Abhishek':'Bio','Yash':'Com','Sweeti':'Comp'}
    inp=input("Enter the value to be searched for:-")
    for a in info:
        if info[a].upper()==inp.upper():
                print("The key of the given value is :-",a)
                break
        else:
            print("Given value does not exist in dictionary")
#Program to sort a list using Bubble sort#
def Progarm28():
    list=[15,6,13,22,3,52,2]
    print("Original list is:-",list)
    n=len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print("List after sorting:-",list)
#Progam to sort a sequence using insertion sort#
def Program29():
    list=[15,6,13,22,3,52,2]
    print("Original list is:-",list)
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j=j-1
        else:
            list[j+1]=key
    print("List`after sorting:-",list)
            
while True:
    print("1.Program2.1")
    print("2.Program2.2")
    print("3.Progeam2.3")
    print("4.Progeam2.4")
    print("5.Progeam2.5")
    print("6.Progeam2.6")
    print("7.Progeam2.7")
    print("8.Progeam2.8")
    print("9.Progeam2.9")
    print("10.Exit")
    ch=int(input("Enter your choise(1..10):-"))
    if ch==1:
        Program21()
    elif ch==2:
        Program22()
    elif ch==3:
        Program23()
    elif ch==4:
        Program24()
    elif ch==5:
        Program25()
    elif ch==6:
        Program26()
    elif ch==7:
        Program27()
    elif ch==8:
        Progarm28()
    elif ch==9:
        Program29()
    elif ch==10:
        break
    else:
        print("Invalid Choise!")
