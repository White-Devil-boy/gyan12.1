li=[20,10,30,10,40,50,60,7,8]
def Add():
    item=int(input("Enter the item:"))
    li.append(item)
def Minimum():
    min=li[0]
    index=0
    for i in range(1,len(li)):
        if min>li[i]:
            min=li[i]
            index=i
    print("The minimum value in the list",li,"is",min,"and the index position is",index)
def Maximum():
    max=li[0]
    index=0
    for i in range(1,len(li)):
        if max<li[i]:
            max=li[i]
            index=i
    print("The maximum value in the list",li,"is",max,"and the index position is",index)
def Average():
    length=len(li)
    sum=0
    for i in range(0,length):
        sum=sum+li[i]
    avg=sum/length
    print("The average of the list",li,"is",avg)
def Search():
    item=int(input("Enter the element that you want to search:"))
    length=len(li)
    for i in range(0,length):
        if item==li[i]:
            index=i
            print("Item Found!",index,"is its index position")
    else:
        print("Item not found ")
def Frequency():
    item=int(input("Enter the number to find it's frequency"))
    length=len(li)
    count=0
    for i in range(length):
        if item==li[i]:
            count=count+1
    if count==0:
        print(item,"not found in list")
    else:
        print("frequency of ",item,"is",count)
def Cancatenation():
    li2=eval(input("Enter the new list"))
    li3=li+li2
    print(li,"+",li2,"=",li3)
def Replicating():
    print("1.Want to Replicate the Existing list")
    print("2.Want to Replicate a new list")
    ch=int(input("Enter your choise(1-2):"))
    if ch==1:
        num=int(input("Enter the Number of time you want to replicate the list"))
        li4=li*num
        print(li,"*",num,"=",li4)
    elif ch==2:
        li5=eval(input("Enter the new list"))
        num=int(input("Enter the Number of time you want to replicate the list"))
        li6=li5*num
        print(li5,"*",num,"=",li6)
    else:
        ("Invalid Choice!")
def Slicing():
    start=int(input("Enter the Starting Position"))
    stop=int(input("Enter the last+1 Position"))
    step=int(input("Enter the Step to add"))
    slic=li[start:stop:step]
    print(slic)
def index():
    item=int(input("Enter the Item to Found"))
    temp=li.index(item)
    print(temp)
def Extend():
    li8=eval(input("Enter the new list that you want to add to existing list"))
    li.extend(li8)
    print(li)
def Insert():
    position=int(input("Enter the index of the element before which the second argument is to added"))
    item=int(input("Enter the item to be added"))
    li.insert(position,item)
    print(li)
def Remove():
    value=int(input("Enter the element that you want to remove"))
    li.remove(value)
    print(li)
def Clear():
    li.clear()
def Count():
    item=int(input("Enter the element that you want to count"))
    li.count(item)
    print(li)
def Reverse():
    li.reverse()
    print(li)
def Sort():
    li.sort()
    print(li)
list=[]
while True:
    print("1.Add an item to list:")
    print("2.The Minimum element in the list")
    print("3.The Maximum element in the list")
    print("4.The average of the element of the list")
    print("5.To find an item in the list")
    print("6.To find the frequency of an element")
    print("7.Cancatenation by adding new list")
    print("8.Replicating a new list or exaisting list")
    print("9.Slicing the Existing list")
    print("10.To find the element using (the found mothod)")
    print("11.To add element to exising list using(Extend method)")
    print("12.To add elemnt to the existing list using(insert method)")
    print("13. To delete the first matching element given by user")
    print("14. To empty the list using (Clear method)")
    print("15. To count the given element using (count method)")
    print("16. To reverse the element of the list using (Reverse method)")
    print("17.To sort the list using (Sort Method)")
    ch=int(input("Enter your choise(1-12):"))
    if ch == 1:
        Add()
    elif ch==2:
        Minimum()
    elif ch==3:
        Maximum()
    elif ch==4:
        Average()
    elif ch==5:
        Search()
    elif ch==6:
        Frequency()
    elif ch==7:
        Cancatenation()
    elif ch==8:
        Replicating()
    elif ch==9:
         Slicing()
    elif ch==10:
        index()
    elif ch==11:
        Extend()
    elif ch==12:
        Insert()
    elif ch==13:
        Remove()
    elif ch==14:
        Clear()
    elif ch==15:
        Count()
    elif ch==16:
        Reverse()
    elif ch==17:
        Sort()
    elif ch==18:
        break
    else:
        print("Invalid choise!")
