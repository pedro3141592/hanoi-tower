h = mov = l = j = 0
a = []
b = []
c = []
def putA(n):
    a.append(n)
def putB(n):
    b.append(n)
def putC(n):
    c.append(n)
def takeA():
    return a.pop()
def takeB():
    return b.pop()
def takeC():
    return c.pop()
def show():
    print("A: ", end = "")
    for ci in range(0,len(a)):
        print(a[ci],end = " ")
    print("\n")
    print("B: ", end = "")
    for ci in range(0,len(b)):
        print(b[ci],end = " ")
    print("\n")
    print("C: ", end = "")
    for ci in range(0,len(c)):
        print(c[ci], end = " ")  
    print("\n")
    print("\n")
def hanoi():
    global h, j
    while (j != 1):
        try:
            h = int(input("How many disks do you want to play with (between 1 and 16): "))
            if  h < 1 or h > 16:
                print("Write a valid number!")
            else:
                j = 1
        except:
            ValueError
            print("Write a int!")
    l = h  
    for k in range(l,0,-1):
        putA(k)
def lookA():
    if(len(a)>0):
        return a[len(a)-1]
    else:
        return 0
def lookB():
    if(len(b)>0):
        return b[len(b)-1]
    else:
        return 0
def lookC():
    if(len(c)>0):
        return c[len(c)-1]
    else:
        return 0
def AB():
    if(len(a)==0):
        putA(takeB())
    elif(len(b)==0):
        putB(takeA())
    elif(lookA() < lookB()):
        putB(takeA())
    elif(lookB() < lookA()):
        putA(takeB())
def AC():
    if(len(a)==0):
        putA(takeC())
    elif(len(c)==0):
        putC(takeA())
    elif(lookA() < lookC()):
        putC(takeA())
    elif(lookC() < lookA()):
        putA(takeC())
def BC():
    if(len(b)==0):
        putB(takeC())
    elif(len(b)==0):
        putC(takeB())
    elif(lookB() < lookC()):
        putC(takeB())
    elif(lookC() < lookB()):
        putB(takeC())
def even():  
    global mov
    while(len(c) != h):
        AB()
        show()
        mov += 1
        if(len(c) == h):
            break
        AC()
        show()
        mov += 1
        if(len(c) == h):
            break   
        BC()
        show()
        mov += 1
        if(len(c) == h):
            break      
def odd():
    global mov
    while(len(c) != h):
        AC()
        show()
        mov += 1
        if(len(c) == h):
            break
        AB()
        show()
        mov += 1
        if(len(c) == h):
            break   
        BC()
        show()
        mov += 1
        if(len(c) == h):
            break      
hanoi()
show()
if(h % 2 == 0):
    even()
else:
    odd()
print(f"The algorithm used {mov} movements to resolve hanoi tower with {h} disks")