num = int(input("type a number: "))
for x in range(0,num*10,num):
    if x == 0:
        continue
    print(str(x//num)+" x "+str(num)+" = " +str(x))

