row=10
for i in range(1,row+1):
    print("*",end="")
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

row=6
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
row=6
for i in range(row,0,-1):
    for j in range(0,i):
         print(i,end="")
    print()
rows=5
for i in range(1,5):
    for j in range(1,i+1):
        print(i*j,end="")
    print()
name="akal"
age=22
print("Name:",name)
print("Age:",age)
name="Akalya"
age=22
print("Name:{}".format(name))
print("Age:{}".format(age))
def add(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
row=5
add(row)


    
