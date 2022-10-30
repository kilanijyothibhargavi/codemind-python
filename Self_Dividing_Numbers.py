x = int(input())
y = int(input())
for i in range(x,y+1):
    a = i%10
    b = i//10
    if i<10:
        print(i,end=" ")
    elif i>10:
        if a==0 or b==0:
            continue
        elif i%a==0 and i%b==0:
            print(i,end=" ")
            