num = int(input())
rem=0
temp=0
while num:
    rem=num%10
    temp = num//10
    num = rem+temp
    if rem%num==0:
        print(num)
        break
    