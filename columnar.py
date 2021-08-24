#321910306060
plain=input("Enter a string")
key=input("Enter a key")
order=int(input("Enter order"))
orderlist=str(order)
add_x=len(key)-(len(plain)%len(key))
plain+=" "*add_x
l=[]
for i in range(0,(len(plain)//len(key))):
    l1=[]
    for j in range(0,len(key)):
        l1.append(plain[(j+(i*len(key)))])
    l.append(l1)
for i in range(1,(len(key)+1)):
    c=orderlist.index(str(i))
    for j in range(0,len(l)):
        print(l[j][c],end="")